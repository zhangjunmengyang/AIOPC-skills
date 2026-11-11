#!/usr/bin/env python3
"""Build fully expanded bilingual READMEs and a URL-based catalog from docs/."""

from __future__ import annotations

import argparse
from collections import defaultdict
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 500 * 1024
LINK = re.compile(r'(?<!!)\[([^\]\n]+)\]\(([^\s)]+)\)')
HEADING = re.compile(r'^(#{1,6})\s+(.+)$')
ANCHOR = re.compile(r'<a\s+(?:id|name)="([^"]+)"\s*></a>')

# Order is editorial. Every document is expanded, including the supplementary index.
GROUPS = [
    ('skills', '按职能找技能', 'Skills by function', [
        '01-startup', '02-writing', '03-product', '04-design', '05-marketing',
        '06-ops', '07-content', '08-data', '09-opc', '10-mcp']),
    ('platforms', '按平台找技能', 'Skills by platform', [
        'platforms/p-xiaohongshu', 'platforms/p-wechat', 'platforms/p-douyin',
        'platforms/p-tiktok', 'platforms/p-x', 'platforms/p-linkedin',
        'platforms/p-reddit', 'platforms/p-youtube', 'platforms/p-ecommerce',
        'platforms/p-appstore', 'platforms/p-seo', 'platforms/p-private']),
    ('business', '经营路线', 'Operating playbooks', ['operator-playbook', 'workflow', 'operating-resources']),
    ('founders', '创始人与专题', 'Founder collections & topics', [
        'solo-founder', 'founder-packs', 'lenny', 'classics', 'naming', 'landscape']),
    ('extended', '扩展目录', 'Extended catalog', [
        'full-marketing', 'full-design', 'full-product', 'full-ops', 'full-content']),
]
SLUGS = [name for _, _, _, names in GROUPS for name in names]


def section_id(name: str) -> str:
    name = name.replace('platforms/p-', 'platform-')
    return re.sub(r'^\d+-', '', name)


def clean_title(text: str) -> str:
    text = re.sub(r'^[^\w]+', '', text).strip()
    return re.sub(r'^[一二三四五六七八九十]+、', '', text)


def slugify(text: str) -> str:
    text = re.sub(r'<[^>]+>', '', text)
    text = LINK.sub(lambda m: m[1], text)
    text = re.sub(r'[^\w\-\s]', '', text.lower())
    return re.sub(r'\s', '-', text.strip())


def document_title(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith('# '):
            return clean_title(line[2:])
    raise ValueError(f'Missing document title: {path}')


def external_urls(text: str) -> set[str]:
    return {m[2] for m in LINK.finditer(text) if m[2].startswith(('https://', 'http://'))}


def document_map(lang: str) -> dict[Path, str]:
    return {(ROOT / 'docs' / lang / f'{name}.md').resolve(): section_id(name) for name in SLUGS}


def rewrite_target(target: str, source: Path, docs: dict[Path, str]) -> str:
    if urlsplit(target).scheme or target.startswith('//'):
        return target
    filename, sep, fragment = target.partition('#')
    dest = (source.parent / unquote(filename)).resolve() if filename else source.resolve()
    if dest in docs:
        base = docs[dest]
        if fragment:
            # Explicit ids and heading slugs both receive the source namespace.
            return f'#{base}-{unquote(fragment)}'
        return f'#{base}'
    try:
        rel = dest.relative_to(ROOT).as_posix()
    except ValueError:
        raise ValueError(f'Link escapes repository: {source}: {target}')
    return rel + (f'#{fragment}' if sep else '')


def render_document(name: str, lang: str, docs: dict[Path, str]) -> str:
    source = ROOT / 'docs' / lang / f'{name}.md'
    lines = source.read_text().splitlines()
    base = section_id(name)
    title = document_title(source)
    output = [f'<a id="{base}"></a>', f'### {title}', '']
    skip_picks = False
    heading_counts: dict[str, int] = defaultdict(int)
    known_ids: set[str] = set()
    for line in lines:
        heading = HEADING.match(line)
        if heading:
            level, label = len(heading[1]), clean_title(heading[2])
            if level == 1:
                continue
            if level == 2:
                skip_picks = label in {'Top picks', '先试这几个'}
            if skip_picks:
                continue
            if label in {'All skills', 'All tools', '全部技能', '全部工具'}:
                continue
            original_slug = slugify(heading[2])
            serial = heading_counts[original_slug]
            heading_counts[original_slug] += 1
            original_slug += f'-{serial}' if serial else ''
            anchor = f'{base}-{original_slug}'
            if anchor not in known_ids:
                output.extend([f'<a id="{anchor}"></a>'])
                known_ids.add(anchor)
            output.extend([f'{"#" * max(4, min(level + 1, 6))} {label}', ''])
            continue
        if skip_picks:
            continue
        if ('返回总览' in line or 'Back to index' in line) and line.startswith('['):
            continue
        if line.startswith('> 索引页：') or line.startswith('> Index page:'):
            continue
        if line.strip() == '---':
            continue
        if ANCHOR.fullmatch(line.strip()):
            old = ANCHOR.fullmatch(line.strip())[1]
            new = f'{base}-{old}'
            if new not in known_ids:
                output.append(f'<a id="{new}"></a>')
                known_ids.add(new)
            continue
        line = re.sub(r'\]\(([^\s)]+)\)', lambda m: '](' + rewrite_target(m[1], source, docs) + ')', line)
        line = re.sub(r'(src|href)="([^"]+)"', lambda m: m[1] + '="' + rewrite_target(m[2], source, docs) + '"', line)
        output.append(line)
    body = re.sub(r'\n{3,}', '\n\n', '\n'.join(output)).strip()
    # A top pick may contain a reference absent from the full list. Never lose it.
    missing = external_urls(source.read_text()) - external_urls(body)
    if missing:
        names = {m[2]: m[1] for m in LINK.finditer(source.read_text())}
        label = '补充参考' if lang == 'zh' else 'Additional references'
        body += '\n\n' + f'#### {label}\n\n'
        body += '\n'.join(f'- [{names[url]}]({url})' for url in sorted(missing))
    return body + '\n\n' + ('[回到目录](#contents)' if lang == 'zh' else '[Back to contents](#contents)')


def build_catalog() -> dict:
    records: dict[str, dict] = {}
    for lang in ('en', 'zh'):
        for name in SLUGS:
            path = ROOT / 'docs' / lang / f'{name}.md'
            for line in path.read_text().splitlines():
                for match in LINK.finditer(line):
                    label, url = match[1], match[2]
                    if not url.startswith(('https://', 'http://')):
                        continue
                    item = records.setdefault(url, {'url': url, 'names': {}, 'descriptions': {}, 'sources': {}})
                    # Prefer meaningful resource names over short contextual link labels.
                    if lang not in item['names'] or line.startswith('- **['):
                        item['names'][lang] = html.unescape(label)
                    if line.startswith('- **[') and ' — ' in line:
                        item['descriptions'][lang] = line.split(' — ', 1)[1].strip()
                    sources = item['sources'].setdefault(lang, [])
                    rel = path.relative_to(ROOT).as_posix()
                    if rel not in sources:
                        sources.append(rel)
    skill_pages = sum(urlsplit(u).netloc.removeprefix('www.') == 'skills.sh' and len(urlsplit(u).path.strip('/').split('/')) == 3 for u in records)
    return {
        'schema_version': 1,
        'description': 'Unique outbound resource and reference URLs in docs/. An index entry is not an installation or quality certification.',
        'counts': {'unique_urls': len(records), 'skill_listing_urls': skill_pages, 'documents_per_language': len(SLUGS)},
        'resources': [records[u] for u in sorted(records)],
    }


def build_readme(lang: str, catalog: dict) -> str:
    template = (ROOT / 'templates' / f'README.{lang}.md').read_text()
    docs = document_map(lang)
    toc = []
    sections = []
    for gid, zh, en, names in GROUPS:
        label = zh if lang == 'zh' else en
        toc.append(f'- **[{label}](#{gid})**：' if lang == 'zh' else f'- **[{label}](#{gid})**: ')
        toc[-1] += ' · '.join(f'[{document_title(ROOT / "docs" / lang / (name + ".md"))}](#{section_id(name)})' for name in names)
        sections.extend([f'<a id="{gid}"></a>', f'## {label}', ''])
        if gid == 'extended':
            sections.append('以下是精选专题之外的补充条目，按原技能包分组。只提供名称与原链接，未逐条实测；同名条目可能来自不同作者。\n' if lang == 'zh' else 'Additional entries beyond the focused sections, grouped by source pack. These contain names and source links; they have not all been tested. The same name can belong to different authors.\n')
        sections.extend(render_document(name, lang, docs) + '\n' for name in names)
    counts = catalog['counts']
    template = template.replace('{{UNIQUE_URLS}}', f'{counts["unique_urls"]:,}').replace('{{SKILL_URLS}}', f'{counts["skill_listing_urls"]:,}')
    template = template.replace('{{TOC}}', '\n'.join(toc)).replace('{{CATALOG}}', '\n'.join(sections))
    return '<!-- Generated by scripts/build_readme.py from templates/ and docs/. Edit those sources, then rebuild. -->\n' + template.rstrip() + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if committed outputs differ from sources.')
    args = parser.parse_args()
    for lang in ('zh', 'en'):
        actual = {p.relative_to(ROOT / 'docs' / lang).with_suffix('').as_posix() for p in (ROOT / 'docs' / lang).rglob('*.md')}
        if actual != set(SLUGS):
            raise ValueError(f'{lang}: add/remove documents in GROUPS: {actual.symmetric_difference(SLUGS)}')
    catalog = build_catalog()
    outputs = {'catalog.json': json.dumps(catalog, ensure_ascii=False, indent=2) + '\n'}
    for lang, filename in [('en', 'README.md'), ('zh', 'README.zh.md')]:
        outputs[filename] = build_readme(lang, catalog)
        size = len(outputs[filename].encode())
        if size >= LIMIT:
            raise ValueError(f'{filename}: {size} bytes exceeds GitHub README limit ({LIMIT}).')
        print(f'{filename}: {size:,} bytes ({size / 1024:.1f} KiB)')
    stale = []
    for filename, content in outputs.items():
        path = ROOT / filename
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(filename)
        else:
            path.write_text(content)
    if stale:
        print('Out of date: ' + ', '.join(stale) + '. Run python3 scripts/build_readme.py.', file=sys.stderr)
        return 1
    print(f'{catalog["counts"]["unique_urls"]:,} unique resource/reference URLs; {catalog["counts"]["skill_listing_urls"]:,} skill listing URLs.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
