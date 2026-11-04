#!/usr/bin/env python3
"""Assemble the static site.

src/pages/**/*.html  + src/partials/*.html  ->  ./**/*.html

Each page starts with a front-matter block:
---
title_en / title_ar / desc_en / desc_ar
nav: care | organizations | locations | resources | company   (active top-level menu)
hero: light | brand | ink   (optional, body class)
---
Inside pages and partials:
  {{base}}            relative prefix to the site root ("" at root, "../" one level down)
  {{> name}}          include src/partials/name.html (rendered with the same context)
  {{key}}             any front-matter key
Usage: python3 tools/build.py [--check]
"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, 'src', 'pages'); PARTS = os.path.join(ROOT, 'src', 'partials')
SITE = 'https://tadawa.com/'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

def parse(src):
    m = re.match(r'^---\n(.*?)\n---\n', src, re.S); meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line: k, v = line.split(':', 1); meta[k.strip()] = v.strip()
        src = src[m.end():]
    return meta, src

_partials = {}
def partial(name):
    if name not in _partials: _partials[name] = read(os.path.join(PARTS, name + '.html'))
    return _partials[name]

def render(tpl, ctx, depth=0):
    if depth > 8: raise RuntimeError('include loop')
    tpl = re.sub(r'\{\{>\s*([a-zA-Z0-9_-]+)\s*\}\}', lambda m: render(partial(m.group(1)), ctx, depth + 1), tpl)
    return re.sub(r'\{\{\s*([a-zA-Z0-9_]+)\s*\}\}', lambda m: ctx.get(m.group(1), ''), tpl)

def build(check=False):
    stale, written = [], 0
    for dirpath, _, files in os.walk(PAGES):
        for name in sorted(files):
            if not name.endswith('.html'): continue
            src_path = os.path.join(dirpath, name)
            rel = os.path.relpath(src_path, PAGES).replace(os.sep, '/')
            meta, body = parse(read(src_path))
            depth = rel.count('/')
            ctx = dict(meta)
            ctx['base'] = '../' * depth
            ctx['slug'] = rel
            ctx['canonical'] = SITE + ('' if rel == 'index.html' else rel)
            ctx['body_class'] = ' '.join(filter(None, ['page-' + rel.replace('/', '-').replace('.html', ''), 'nav-' + meta.get('nav', ''), 'hero-' + meta.get('hero', 'light')]))
            ctx['body'] = render(body, ctx)
            out = render(partial('layout'), ctx)
            target = os.path.join(ROOT, rel)
            os.makedirs(os.path.dirname(target), exist_ok=True)
            if check:
                if not os.path.exists(target) or read(target) != out: stale.append(rel)
            else:
                with open(target, 'w', encoding='utf-8') as f: f.write(out)
                written += 1
    if check:
        if stale: print('STALE:', ', '.join(stale)); sys.exit(1)
        print('all pages up to date')
    else:
        print('wrote', written, 'pages')

if __name__ == '__main__':
    build(check='--check' in sys.argv)
