#!/usr/bin/env python3
import os
from datetime import datetime

base_url = 'https://craigclaw.github.io/meridianidconcrete'
today = datetime.now().strftime('%Y-%m-%d')

html_files = sorted([f for f in os.listdir('.') if f.endswith('.html')])

def priority(fname):
    if fname == 'index.html': return '1.0'
    if fname.startswith('blog'): return '0.6'
    if fname in ('privacy.html', 'terms.html', '404.html'): return '0.3'
    # Cross pages (service-city pattern)
    services = ['concrete-driveways', 'concrete-patios', 'stamped-concrete', 
                'concrete-repair', 'concrete-sidewalks', 'foundations-slabs']
    cities = ['boise', 'meridian', 'eagle', 'star', 'kuna', 'nampa']
    for svc in services:
        for city in cities:
            if fname == f'{svc}-{city}.html':
                return '0.7'
    # Location pages
    for city in cities:
        if fname == f'{city}-id.html':
            return '0.8'
    # Service pages
    return '0.8'

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
for f in html_files:
    p = priority(f)
    changefreq = 'weekly' if p in ('1.0', '0.8') else 'monthly'
    xml.append(f'  <url><loc>{base_url}/{f}</loc><lastmod>{today}</lastmod><changefreq>{changefreq}</changefreq><priority>{p}</priority></url>')
xml.append('</urlset>')

sitemap = '\n'.join(xml)
with open('sitemap.xml', 'w') as sf:
    sf.write(sitemap)
print(f'Generated sitemap with {len(html_files)} URLs')