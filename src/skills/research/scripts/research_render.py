"""Offline citation compilation and Markdown/LaTeX/Word/PDF conversion."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET
from zipfile import ZipFile, BadZipFile

from research_common import (APA, ResearchError, binary, check_document, citation_ids,
                             digest, dump, file_hash, load, pandoc, parse_markdown,
                             publish, require, run, walk)
from research_project import records


def citation_key(source_id):
    return "r" + digest(source_id)[:16]


def bibliography(sources):
    output, seen, dois = [], set(), set()
    types = {"journal_article": "article-journal", "article": "article-journal", "review": "article-journal",
             "book": "book", "book_chapter": "chapter", "report": "report", "webpage": "webpage",
             "dataset": "dataset", "preprint": "article", "conference_paper": "paper-conference"}
    for source in sources:
        sid = source["source_id"]
        key = citation_key(sid)
        require(key not in seen, "Duplicate source ID/citation-key collision")
        seen.add(key)
        csl = copy.deepcopy(source.get("csl", {}))
        require(isinstance(csl, dict), f"csl must be an object: {sid}")
        require(source["publication_type"] in types or isinstance(csl.get("type"), str) and csl["type"],
                f"Unknown publication_type needs an explicit CSL type: {sid}")
        require(not csl.get("id") or csl["id"] == key, f"CSL ID differs from generated key: {sid}")
        require(not csl.get("title") or csl["title"] == source["title"], f"CSL title conflicts with source: {sid}")
        csl.update(id=key, title=source["title"])
        csl.setdefault("type", types.get(source["publication_type"], "article"))
        if source.get("doi") and csl.get("DOI"):
            def doi_key(value):
                return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", str(value), flags=re.I).strip().lower()
            require(doi_key(source["doi"]) == doi_key(csl["DOI"]), f"CSL DOI conflicts with source: {sid}")
        mappings = {"journal_title": "container-title", "doi": "DOI", "article_url": "URL",
                    "url": "URL", "volume": "volume", "issue": "issue", "pages": "page", "publisher": "publisher"}
        for native, target in mappings.items():
            if source.get(native) is not None:
                csl.setdefault(target, source[native])
        if "author" not in csl and source.get("authors"):
            csl["author"] = []
            for author in source["authors"]:
                if isinstance(author, str):
                    csl["author"].append({"literal": author})
                else:
                    require(isinstance(author, dict) and any(k in author for k in ["literal", "family", "given"]), f"Use explicit CSL name objects or display-name strings: {sid}")
                    csl["author"].append({k: v for k, v in author.items() if k in {"literal", "family", "given", "suffix", "non-dropping-particle", "dropping-particle"}})
        if "issued" not in csl and source.get("year") is not None:
            require(type(source["year"]) is int and source["year"] > 0, f"Invalid publication year: {sid}")
            csl["issued"] = {"date-parts": [[source["year"]]]}
        doi = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", str(csl.get("DOI", "")), flags=re.I).strip().lower()
        if doi:
            require(doi not in dois, f"Duplicate DOI records; reconcile source pool first: {doi}")
            dois.add(doi)
        output.append(csl)
    return output


def resolve_style(style):
    path = APA if style in {"apa", "apa7"} else Path(style).expanduser().resolve()
    require(path.is_file(), f"Missing CSL file: {path}", "missing_style")
    try:
        root = ET.parse(path).getroot()
        require(root.tag == "{http://purl.org/net/xbiblio/csl}style", "Expected a CSL stylesheet")
        require(root.find("{*}citation") is not None and root.find("{*}bibliography") is not None,
                "Use a self-contained CSL style with citation and bibliography sections")
    except ET.ParseError as exc:
        raise ResearchError("invalid_style", str(exc)) from exc
    return path


def process_citations(ast, bib, style, executable=None):
    keys = citation_ids(ast)
    available = {r["id"] for r in bib}
    require(set(keys) <= available, f"Unknown/source-needed citation keys: {sorted(set(keys) - available)}", "unknown_citation")
    # Bibliography paths are local and invocation-controlled; never fetched from manuscript metadata.
    with tempfile.TemporaryDirectory(prefix="research-citations-") as tmp:
        path = Path(tmp) / "bibliography.json"
        path.write_text(dump(bib), encoding="utf-8")
        rendered = json.loads(pandoc(dump(ast), ["-f", "json", "-t", "json", "--citeproc",
                            "--bibliography", path, "--csl", resolve_style(style)], executable).stdout)
    return rendered, keys


def compile_project(args):
    project = args.project.resolve()
    inventory = records(project)
    bib = bibliography(inventory["sources"])
    key_map = {s["source_id"]: citation_key(s["source_id"]) for s in inventory["sources"]}
    outputs = {project / "bibliography.json": dump(bib), project / "citation-keys.json": dump(key_map)}
    if args.prepare:
        return {"outputs": publish(outputs, args.replace), "citation_keys": key_map}
    draft = project / "draft.md"
    text = draft.read_text(encoding="utf-8")
    ast = parse_markdown(text, args.pandoc)
    check_document(ast, project)
    require(citation_ids(ast), "Report has no machine-readable citations")
    brief = load(project / "brief.json")
    rendered, keys = process_citations(ast, bib, args.style or brief["citation_style"], args.pandoc)
    report = pandoc(dump(rendered), ["-f", "json", "-t", "markdown-citations", "--wrap=none"], args.pandoc).stdout
    cited = [s for s in inventory["sources"] if key_map[s["source_id"]] in keys]
    receipt = {"schema_version": 1, "status": "ok", "draft_sha256": file_hash(draft),
               "sources_sha256": file_hash(project / "sources.json"), "report_sha256": digest(report),
               "cited_keys": keys, "cited_source_ids": [s["source_id"] for s in cited],
               "key_map": key_map, "style_sha256": file_hash(resolve_style(args.style or brief["citation_style"])),
               "pandoc_version": run([binary("pandoc", args.pandoc), "--version"]).stdout.splitlines()[0]}
    outputs.update({project / "report.md": report, project / "cited-sources.json": dump(cited),
                    project / "citation-receipt.json": dump(receipt)})
    return {"outputs": publish(outputs, args.replace), **receipt}


def docx_signature(path):
    try:
        with ZipFile(path) as archive:
            xml = ET.fromstring(archive.read("word/document.xml"))
    except (BadZipFile, KeyError, ET.ParseError) as exc:
        raise ResearchError("invalid_docx", "Converter did not produce a Word document") from exc
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
          "m": "http://schemas.openxmlformats.org/officeDocument/2006/math"}
    return {"tables": len(xml.findall(".//w:tbl", ns)), "math": len(xml.findall(".//m:oMath", ns)),
            "images": len(xml.findall(".//w:drawing", ns)),
            "text": "".join(xml.itertext())}


def export_document(args):
    source = args.input.resolve()
    output = args.output.resolve()
    require(source.is_file(), f"Missing Markdown input: {source}")
    require(output != source, "Export cannot overwrite its Markdown input")
    if args.project:
        project_root = args.project.resolve()
        manifest = load(project_root / "manifest.json")
        protected = {project_root / "draft.md", project_root / "report.md"}
        protected.update((project_root / r["path"]).resolve() for r in manifest["sections"])
        require(output not in protected, "Project export cannot overwrite manuscript or section inputs")
    suffix = {"md": ".md", "latex": ".tex", "pdf": ".pdf", "docx": ".docx"}
    require(output.suffix.lower() == suffix[args.format], f"Expected {suffix[args.format]} destination")
    require(not output.exists() or args.replace, f"Output exists: {output}; use --replace", "output_exists")
    ast = parse_markdown(source.read_text(encoding="utf-8"), args.pandoc)
    assets = check_document(ast, source.parent)
    if citation_ids(ast):
        require(args.bibliography, "Unrendered citation keys require --bibliography", "missing_bibliography")
        ast, _ = process_citations(ast, load(args.bibliography), args.style or "apa", args.pandoc)
    elif args.bibliography:
        require(False, "--bibliography supplied but no citation keys found; export the compiled report without it")
    require(output not in assets, "Export cannot overwrite an input asset")
    version = run([binary("pandoc", args.pandoc), "--version"]).stdout.splitlines()[0]
    original_counts = {kind: sum(n.get("t") == kind for n in walk(ast)) for kind in ["Table", "Math", "Image"]}
    files = {}
    asset_outputs = []
    # Text exports carry their own local assets; binary exports embed the originals.
    if args.format in {"md", "latex"}:
        for node in walk(ast):
            if node.get("t") == "Image":
                from urllib.parse import unquote
                path = (source.parent / unquote(node["c"][2][0])).resolve()
                relative = Path(output.stem + "_assets") / (file_hash(path)[:16] + path.suffix.lower())
                target = output.parent / relative
                require(target != source, "Asset output collides with source")
                if not target.exists() or target.read_bytes() != path.read_bytes():
                    files[target] = path.read_bytes()
                asset_outputs.append({"path": str(target), "sha256": file_hash(path)})
                node["c"][2][0] = relative.as_posix()
    args_common = ["-f", "json", "--standalone", "--resource-path", str(source.parent)]
    if args.reference_doc:
        require(args.format in {"docx", "pdf"}, "--reference-doc applies to Word/PDF only")
        require(args.reference_doc.is_file(), "Missing Word reference document")
        args_common.extend(["--reference-doc", args.reference_doc.resolve()])
    backend = "pandoc"
    with tempfile.TemporaryDirectory(prefix="research-export-") as tmp:
        tmp = Path(tmp)
        target = tmp / ("report.docx" if args.format == "pdf" else "report" + suffix[args.format])
        writer = {"md": "markdown-citations", "latex": "latex", "docx": "docx", "pdf": "docx"}[args.format]
        pandoc(dump(ast), [*args_common, "-t", writer, "--wrap=none", "-o", target], args.pandoc, source.parent)
        require(target.is_file() and target.stat().st_size > 0, "Converter produced no output")
        if args.format in {"docx", "pdf"}:
            signature = docx_signature(target)
            require(signature["tables"] >= original_counts["Table"] and signature["math"] >= original_counts["Math"]
                    and signature["images"] >= original_counts["Image"], "Word conversion dropped tables, mathematics or images", "content_loss")
            with ZipFile(target) as archive:
                media = [n for n in archive.namelist() if n.startswith("word/media/")]
            require(not original_counts["Image"] or media, "Word conversion dropped images", "content_loss")
        if args.format == "pdf":
            if not args.soffice:
                raise ResearchError("missing_dependency", "PDF requires --soffice pointing to bundled LibreOffice resolved by the host", True)
            executable = binary("soffice", args.soffice)
            profile = (tmp / "profile").as_uri()
            run([executable, f"-env:UserInstallation={profile}", "--headless", "--convert-to", "pdf", "--outdir", tmp, target], timeout=180)
            target = tmp / "report.pdf"
            require(target.is_file() and target.read_bytes().startswith(b"%PDF-"), "LibreOffice did not produce a PDF")
            backend = "pandoc-docx+libreoffice"
        files[output] = target.read_bytes()
    receipt = {"schema_version": 1, "status": "ok", "format": args.format, "input": str(source),
               "input_sha256": file_hash(source), "output": str(output), "output_sha256": digest(files[output]),
               "backend": backend, "pandoc_version": version, "features": original_counts,
               "assets": [str(p) for p in assets],
               "asset_inputs": [{"path": str(p), "sha256": file_hash(p)} for p in assets],
               "asset_outputs": asset_outputs,
               "visual_review": "pending" if args.format in {"docx", "pdf"} else "not_applicable"}
    if args.format == "pdf":
        receipt["libreoffice_version"] = run([executable, "--version"]).stdout.strip()
    if args.project:
        project = args.project.resolve()
        require(source == project / "report.md", "Project exports must use the canonical compiled report.md")
        register = load(project / "exports.json")
        register["exports"] = [e for e in register["exports"] if e.get("output") != str(output)] + [receipt]
        # Updating the register is part of this explicit export; it is not permission to overwrite artifacts.
        require(project / "exports.json" not in files, "Output collides with export register")
    receipt_path = output.with_suffix(output.suffix + ".receipt.json")
    require(receipt_path != source, "Receipt collides with source")
    files[receipt_path] = dump(receipt)
    written = publish(files, args.replace)
    if args.project:
        publish({project / "exports.json": dump(register)}, replace=True)
    return {**receipt, "outputs": written}
