#!/usr/bin/env python3
"""Small approved check adapters. Read transient inputs from stdin; never persist them."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys


def result(id, passed, pointer, error=False):
    out = {'id': id, 'score': 2 if passed else 0, 'evidence': not error, 'pointer': pointer}
    if error: out['error'] = 'check-unavailable'
    return out


def protected(packet):
    context = packet.get('input', {})
    tokens = context.get('protected_tokens', context.get('context', {}).get('protected_tokens', []))
    output = packet['output']
    if not isinstance(tokens, list) or not all(isinstance(t, str) and t for t in tokens) or not isinstance(output, str):
        return result('protected', False, 'Invalid protected-token input.', True)
    source = context.get('source')
    ok = all(output.count(t) == source.count(t) if isinstance(source, str) and t in source else t in output for t in tokens)
    return result('protected', ok, 'Specified protected-token occurrences checked against output; an empty supplied token set imposes no exact-token requirement.')


def ui_limits(packet):
    context = packet.get('input', {})
    limit = context.get('max_characters', context.get('context', {}).get('max_characters'))
    if type(limit) is not int or limit < 0 or not isinstance(packet['output'], str):
        return result('ui-limits', False, 'A measurable UI limit and text are required.', True)
    return result('ui-limits', len(packet['output']) <= limit, 'Output character count checked against the supplied maximum.')


def structure(files, template):
    paragraphs = template.read_text().split('\n\n')
    start = next(i for i, paragraph in enumerate(paragraphs) if paragraph.startswith('If you miss relevant information,'))
    block = '### Default Procedures\n\n' + '\n\n'.join(paragraphs[start:start + 3])
    artifacts = [{'content': p.read_text(), 'slug': p.parent.name} for p in files]
    # Use a real YAML parser. Ruby/Psych is available on the target macOS host.
    code = '''require 'json'; require 'yaml'; input=JSON.parse(STDIN.read); ok=input['artifacts'].all? do |a|
      begin
        text=a['content']; fm=text.match(/\\A---\\r?\\n(.*?)\\r?\\n---/m); m=fm && YAML.safe_load(fm[1]);
        names=%w[name description version updated type status]; lists=%w[author references];
        m.is_a?(Hash) && names.all?{|k|m[k].is_a?(String) && !m[k].empty?} && lists.all?{|k|m[k].is_a?(Array) && m[k].all?{|v|v.is_a?(String) && !v.empty?}} &&
        m['name']==a['slug'] && m['name'].match?(/\\A[a-z0-9]+(?:-[a-z0-9]+)*\\z/) && m['name'].length<=64 &&
        text.scan(input['block']).length==1 && text.split(/^## Inputs\\s*$/)[1]&.split(/^## /)&.first&.rstrip&.end_with?(input['block']) && text.include?('spawn-evals')
      rescue; false; end
    end; puts JSON.generate({'passed'=>ok})'''
    try:
        run = subprocess.run(['ruby', '-e', code], input=json.dumps({'artifacts': artifacts, 'block': block}), text=True, capture_output=True, timeout=15)
        if run.returncode: return result('structure', False, 'YAML parser failed to execute.', True)
        return result('structure', bool(artifacts) and json.loads(run.stdout)['passed'], 'YAML metadata, directory agreement, Default Procedures subsection at the end of Inputs and shared validation handoff checked.')
    except (OSError, subprocess.TimeoutExpired, ValueError):
        return result('structure', False, 'A usable Ruby YAML parser is required.', True)


def measurement():
    run = subprocess.run([sys.executable, str(Path(__file__).with_name('test_engine.py'))], capture_output=True, text=True, timeout=30)
    return result('measurement', run.returncode == 0, 'Shared evaluator regression suite executed; inspect command result for test count.')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('kind', choices=['protected', 'ui-limits', 'structure', 'measurement'])
    ap.add_argument('--files', nargs='*', type=Path)
    ap.add_argument('--template', type=Path, default=Path('templates/SKILL.md'))
    a = ap.parse_args()
    if a.kind == 'structure':
        answer = structure(a.files or [], a.template)
    elif a.kind == 'measurement':
        answer = measurement()
    else:
        packet = json.load(sys.stdin)
        answer = protected(packet) if a.kind == 'protected' else ui_limits(packet)
    print(json.dumps(answer))


if __name__ == '__main__':
    main()
