#!/usr/bin/env python3
"""Assemble the static site: src/pages/*.html + src/partials/{head,header,footer}.html -> ./*.html

Usage:  python3 tools/build.py        (writes the root HTML files)
        python3 tools/build.py --check (fails if the root files are stale)

Each page in src/pages/ starts with a small front-matter block:
---
title_en: ...
title_ar: ...
desc_en: ...
desc_ar: ...
slug: index.html
hero_class: (optional) extra class for <body>
---
"""
import os, re, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

def parse(src):
    m = re.match(r'^---\n(.*?)\n---\n', src, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1); meta[k.strip()] = v.strip()
        src = src[m.end():]
    return meta, src

def render(tpl, meta):
    def rep(mo):
        key = mo.group(1)
        return meta.get(key, '')
    return re.sub(r'\{\{\s*([a-zA-Z0-9_]+)\s*\}\}', rep, tpl)

def build(check=False):
    head = read(P('src', 'partials', 'head.html'))
    header = read(P('src', 'partials', 'header.html'))
    footer = read(P('src', 'partials', 'footer.html'))
    stale = []
    for name in sorted(os.listdir(P('src', 'pages'))):
        if not name.endswith('.html'): continue
        meta, body = parse(read(P('src', 'pages', name)))
        meta.setdefault('slug', name)
        meta.setdefault('body_class', '')
        meta.setdefault('canonical', 'https://tadawa.com/' + ('' if meta['slug'] == 'index.html' else meta['slug']))
        out = render(head, meta) + render(header, meta) + body + render(footer, meta)
        target = P(meta['slug'])
        if check:
            if not os.path.exists(target) or read(target) != out: stale.append(meta['slug'])
        else:
            with open(target, 'w', encoding='utf-8') as f: f.write(out)
            print('wrote', meta['slug'], len(out), 'bytes')
    if check:
        if stale:
            print('STALE:', ', '.join(stale)); sys.exit(1)
        print('all pages up to date')

if __name__ == '__main__':
    build(check='--check' in sys.argv)
