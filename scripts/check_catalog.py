#!/usr/bin/env python3
"""Offline integrity checks; this does not claim upstream URLs are installable."""

from collections import Counter
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from build_readme import LIMIT, SLUGS, slugify

ROOT = Path(__file__).resolve().parents[1]
MD_LINK = re.compile(r'!?\[[^\]\n]*\]\(([^\s)]+)\)')
HTML_LINK = re.compile(r'(?:src|href)="([^"]+)"')
HTML_ID = re.compile(r'<[^>]+\b(?:id|name)="([^"]+)"')


def prose(text):
    return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.M | re.S)


def targets(text):
    text = prose(text)
    return MD_LINK.findall(text) + HTML_LINK.findall(text)


def externals(text):
    return {url for url in targets(text) if url.startswith(('https://', 'http://'))}


def anchors(text):
    text = prose(text)
    ids = set(HTML_ID.findall(text))
    counts = Counter()
    for title in re.findall(r'^#{1,6}\s+(.+)$', text, flags=re.M):
        base = slugify(title)
        number = counts[base]
        counts[base] += 1
        ids.add(base + (f'-{number}' if number else ''))
    return ids


def main():
    errors = []
    files = list((ROOT / 'docs').rglob('*.md')) + list(ROOT.glob('*.md'))
    contents = {path.resolve(): path.read_text() for path in files}
    ids = {path: anchors(text) for path, text in contents.items()}
    for path, text in contents.items():
        for url in targets(text):
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not dest.is_relative_to(ROOT):
                errors.append(f'{path.relative_to(ROOT)}: link escapes repository: {url}')
            elif not dest.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing local target: {url}')
            elif parsed.fragment and dest.suffix == '.md' and unquote(parsed.fragment) not in ids.get(dest, set()):
                errors.append(f'{path.relative_to(ROOT)}: missing anchor: {url}')
    union = set()
    for name in SLUGS:
        zh = externals(contents[(ROOT / 'docs/zh' / f'{name}.md').resolve()])
        en = externals(contents[(ROOT / 'docs/en' / f'{name}.md').resolve()])
        if zh != en:
            errors.append(f'{name}: language URL mismatch: {sorted(zh ^ en)}')
        union.update(zh | en)
    readme_urls = {}
    for lang, filename in [('zh', 'README.zh.md'), ('en', 'README.md')]:
        text = contents[ROOT / filename]
        readme_urls[lang] = externals(text)
        expected = set().union(*(externals(contents[(ROOT / 'docs' / lang / f'{name}.md').resolve()]) for name in SLUGS))
        missing = expected - readme_urls[lang]
        if missing:
            errors.append(f'{filename}: source URLs absent from expanded README: {sorted(missing)}')
        if len(text.encode()) >= LIMIT:
            errors.append(f'{filename}: exceeds 500 KiB GitHub display limit')
        if '<details' in text.lower() or '{{' in text:
            errors.append(f'{filename}: folded content or an unresolved template placeholder')
        duplicate_ids = [key for key, count in Counter(HTML_ID.findall(text)).items() if count > 1]
        if duplicate_ids:
            errors.append(f'{filename}: duplicate explicit anchors: {duplicate_ids}')
        if '所有链接核验' in text or 'All links verified' in text:
            errors.append(f'{filename}: unsupported blanket verification claim')
    if readme_urls['zh'] != readme_urls['en']:
        errors.append(f'README language URL mismatch: {sorted(readme_urls["zh"] ^ readme_urls["en"])}')
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    rows = catalog['resources']
    urls = {item['url'] for item in rows}
    if urls != union or len(rows) != len(urls):
        errors.append('catalog.json: duplicated or missing source URLs')
    if catalog['counts']['unique_urls'] != len(urls):
        errors.append('catalog.json: incorrect unique URL count')
    for item in rows:
        if set(item['names']) != {'en', 'zh'} or set(item['sources']) != {'en', 'zh'}:
            errors.append(f'catalog.json: incomplete bilingual record: {item["url"]}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        print(f'{len(errors)} integrity error(s).', file=sys.stderr)
        return 1
    print(f'OK: {len(files)} Markdown files; local links and anchors valid.')
    print(f'OK: {len(SLUGS)} bilingual source pairs; {len(urls):,} unique source URLs fully expanded.')
    print('OK: catalog records, language parity, README size and no collapsed sections.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
