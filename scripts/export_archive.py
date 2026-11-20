"""Export the KBL Supabase CSV dumps into a browsable Git archive. Usage: python3 -I export_archive.py <csv_dir> <repo_dir>"""
import csv, json, os, re, sys, base64, html as H
csv.field_size_limit(10**9)
src, out = sys.argv[1], sys.argv[2]
rd = lambda f: list(csv.DictReader(open(os.path.join(src, f), encoding='utf-8')))
emails, previews, assets = rd('kbl_emails_rows.csv'), {r['key']: r for r in rd('kbl_email_previews_rows.csv')}, rd('kbl_email_assets_rows.csv')
seqs, meta = rd('kbl_sequences_rows.csv'), rd('kbl_report_meta_rows.csv')
def w(p, data, mode='w'):
    p = os.path.join(out, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, mode, **({} if 'b' in mode else {'encoding': 'utf-8', 'newline': '\n'})) as f: f.write(data)
ext = {'image/webp': 'webp', 'image/gif': 'gif', 'image/png': 'png', 'image/jpeg': 'jpg'}
amap = {}
for a in assets:
    name = f"{a['id']}.{ext.get(a['mime'], 'bin')}"; amap[a['id']] = name
    w(f'assets/images/{name}', base64.b64decode(a['data_base64']), 'wb')
slug = lambda s: re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:60] or 'untitled'
def folder(e, d):
    if e['type'] == 'broadcast': return f"emails/broadcasts/{(e['source_date'] or 'undated')[:4]}"
    if e['type'] == 'sequence': return f"emails/sequences/S{e['sequence_id']}-{slug(d.get('sequenceName') or '')}"
    return 'emails/notifications'
pct = lambda v: '' if v in (None, '') else f"{float(v)*100:.2f}%"
rows, index = [], []
for e in emails:
    d = json.loads(e['data']); f = d.get('features', {}); key = e['key']
    base = f"{folder(e, d)}/{(e['source_date'] + '_') if e['source_date'] else ''}{key}_{slug(e['subject'])}"
    p = previews.get(key)
    if p:
        page = re.sub(r'/api/email-assets/([a-f0-9]{64})', lambda m: '../' * base.count('/') + 'assets/images/' + amap.get(m.group(1), m.group(1)), p['html'])
        w(base + '.html', f"<!doctype html><meta charset=utf-8><title>{H.escape(e['subject'])}</title><body style='max-width:720px;margin:auto;font-family:sans-serif'><p><b>{key}</b> · {H.escape(e['subject'])}</p><hr>{page}</body>")
    fm = {k: e[k] for k in ['key','type','name','subject','sender','source_date','source_hour','source_minute','family','word_count','sent','opens','clicks','goals','unsubs','spam','bounces']}
    fm.update(open_rate=pct(d.get('openRate')), click_rate=pct(d.get('clickRate')), revenue_field_usd=(int(e['revenue_field_cents'])/100 if e['revenue_field_cents'] else e['revenue_field_cents']),
              weekday=(d.get('date') or {}).get('weekdayName'), sequence=d.get('sequenceName'), step=d.get('stepIndex'), status=d.get('status'))
    md = '---\n' + ''.join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in fm.items()) + '---\n\n' + f"# {e['subject']}\n\n" + e['body_text'].strip() + '\n'
    if p: md += f"\n\n---\n[Rendered HTML with images]({os.path.basename(base)}.html)\n"
    w(base + '.md', md)
    rows.append({**fm, **{k: f.get(k) for k in ['subjectChars','subjectWords','paragraphs','imageCount','linkCount','questions','exclamations','ps','urgency','discount','free','storyCue','teachingCue','personalizedSubject','questionSubject','emojiSubject']}, 'path': base + '.md'})
    index.append(fm | {'path': base})
w('data/emails.jsonl', ''.join(json.dumps({**json.loads(e['data']), 'previewHtml': previews.get(e['key'], {}).get('html')}, ensure_ascii=False) + '\n' for e in emails))
cols = list(rows[0].keys())
import io; buf = io.StringIO(); cw = csv.DictWriter(buf, cols, lineterminator='\n'); cw.writeheader(); cw.writerows(rows); w('data/emails.csv', buf.getvalue())
w('data/sequences.json', json.dumps([json.loads(s['data']) for s in seqs], ensure_ascii=False, indent=1))
for m in meta: w(f"data/report_meta/{m['key']}.json", json.dumps(json.loads(m['value']), ensure_ascii=False, indent=1))
w('data/assets.json', json.dumps([{k: a[k] for k in ['id','mime','size_bytes','width','height']} | {'file': 'assets/images/' + amap[a['id']], 'metadata': json.loads(a['metadata'])} for a in assets], indent=1))
def tbl(items):
    s = '| Key | Date | Subject | Sent | Open | Click | Revenue field |\n|---|---|---|---:|---:|---:|---:|\n'
    return s + ''.join(f"| [{i['key']}]({i['path']}.md) | {i['source_date'] or ''} {i['weekday'] or ''} | {i['subject'].replace('|','/')} | {i['sent']} | {i['open_rate']} | {i['click_rate']} | {i['revenue_field_usd'] or ''} |\n" for i in items)
bc = sorted([i for i in index if i['type']=='broadcast'], key=lambda i: (i['source_date'] or '', i['key']))
w('INDEX.md', f"# Email index\n\n{len(index)} emails: {len(bc)} broadcasts, {sum(i['type']=='sequence' for i in index)} sequence steps, {sum(i['type']=='notification' for i in index)} notifications.\n\n## Broadcasts\n\n" + tbl(bc) + "\n## Sequences\n\n" + tbl([i for i in index if i['type']=='sequence']) + "\n## Notifications\n\n" + tbl([i for i in index if i['type']=='notification']))
w('README.md', f"""# Mike Salemi (KBL) email archive

Private archive of the {len(index)} retained Kartra emails used by `mike-salemi-email-intelligence`, exported from Supabase project `vkkkarpobwdjkcxasxvr`.

- `INDEX.md` — every email with date, subject, sent, open and click rate.
- `emails/` — one `.md` per email (metrics in front-matter + plain text body) and one `.html` rendered preview with images.
- `assets/images/` — the {len(assets)} stored email images.
- `data/emails.csv` — one row per email with metrics and content features (open in Excel/Sheets).
- `data/emails.jsonl` — full records, including preview HTML. `data/sequences.json`, `data/report_meta/` — sequences and report metadata.

Rates are opens/sent and clicks/sent as reported by Kartra. `revenue_field_usd` is Kartra's per-email revenue credit, not reconciled sales. Times are the Pacific source clock.

Regenerate: export the Supabase `kbl_*` tables as CSV, then `python3 scripts/export_archive.py <csv_dir> .`
""")
print(len(index), 'emails', len(assets), 'assets')
