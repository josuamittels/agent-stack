# Configured documentation publication

Read when a documentation task includes publication or project instructions authorize recurring updates to an existing site. Resolve target, output directory, credentials and authorization from that project. Keep this procedure reusable; a hosting profile does not authorize deployment to an unrelated site.

## Build for the host

For a file-based web host, use a static export. In Next.js, configure `output: 'export'`, directory-style routes with `trailingSlash: true` where appropriate, and a supported image strategy. Replace server-only redirects with actual host rules. Build with the project's command. Generate Pagefind inside the exported directory after the build, not only inside the source `public/` directory after export has already finished.

For Agent Stack, `npm run build` from `docs/` runs Next.js export and `scripts/postbuild.mjs`. The output is `docs/out/`, including `_pagefind/`, sitemap and robots. The Apache rules in `docs/public/.htaccess` preserve the old Write URL and serve the exported 404 page. Preview the static output with a static HTTP server; `next start` is for a server build and does not preview this export.

## Local profile

Use the blank [.env.example](../.env.example) to configure a local `.env.local` in this skill directory. Keep the actual file ignored, owner-readable, and outside public output. The publisher reads literal values without sourcing a shell, expanding `$`, or logging the profile. Installed packages contain only the blank example. Do not copy a profile between unrelated projects.

The profile fields are:

| Field | Purpose |
| --- | --- |
| `DOCS_DEPLOY_HOST` | Exact authorized server hostname, used for TLS verification. |
| `DOCS_DEPLOY_PORT` | Explicit FTPS port, normally 21. |
| `DOCS_DEPLOY_PROTOCOL` | `ftps`, meaning explicit TLS, not implicit FTPS. |
| `DOCS_DEPLOY_USER` / `DOCS_DEPLOY_PASSWORD` | Local connection credentials. |
| `DOCS_DEPLOY_REMOTE_DIR` | Site destination relative to the authenticated account, often `/` for a confined account. |
| `DOCS_DEPLOY_URL` | Public HTTPS site origin. |
| `DOCS_DEPLOY_SOURCE` | Public export path relative to the target project, inside `docs/`. |
| `DOCS_DEPLOY_SITE_ID` | Stable identifier guarding against another site's deployment manifest. |

The bundled [publisher](../scripts/deploy_docs.py) supports explicit FTPS with verified control/data TLS and TLS-session reuse. It uses Python 3.10+ standard-library modules. SFTP on a custom port needs an appropriate separately verified client; do not silently switch protocols or disable verification. Preserve authorization and report a concrete connection failure if the configured protocol cannot work.

## Publish and verify

From the target project root, with the appropriate available Python interpreter:

```sh
python src/skills/create-docs/scripts/deploy_docs.py --project-root . --probe
python src/skills/create-docs/scripts/deploy_docs.py --project-root . --plan
python src/skills/create-docs/scripts/deploy_docs.py --project-root .
```

For Agent Stack, `npm run deploy` from `docs/` performs the final command. Supply `--env-file` when the authorized profile is elsewhere. Use a working Python interpreter rather than changing system Python settings.

The probe only reads the destination listing. The plan builds and inventories public output without uploading. Normal publication always rebuilds, then uploads changed files based on a site-specific hash manifest. It uploads assets before pages and the homepage last, checks transfer sizes, and renames temporary files into place. Publication is per-file rather than a transaction across the entire site. The manifest updates only after all transfers succeed.

Unknown existing files are preserved. On first setup, inspect any colliding files. Only when the user's scope authorizes replacing those files, use `--adopt-existing` with their exact relative names. Originals are backed up under the target project's ignored `.local/docs-deploy/`. A preinstalled welcome page can be adopted for an explicitly authorized initial site replacement. Do not adopt arbitrary files or directories. A retry tolerates identical files left by an interrupted upload. No remote deletion or automatic pruning occurs, so record retained obsolete files if routes are removed; a cleanup outside this upload needs a scoped decision.

Deployment results are recorded at `.local/docs-deploy/last-deployment.json` without credentials. Verify the public site over HTTPS, a changed nested route loaded directly, static asset responses, host redirects, and a real Pagefind search in a browser. Compare live bytes to the export when diagnosing a stale response. Keep missing or unsuccessful checks visible. Do not report publication complete from FTP success alone.

Routine updates covered by an existing project authorization do not need another permission question. A changed destination or an unmanaged-file conflict outside that authorization remains a separate matter. Runtime approval controls still apply; report an actual rejection and continue independent work rather than disguising a failed publication.
