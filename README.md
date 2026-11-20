# Mike Salemi (KBL) email archive

Private archive of the 1042 retained Kartra emails used by `mike-salemi-email-intelligence`, exported from Supabase project `vkkkarpobwdjkcxasxvr`.

- `PLAYBOOK.md` — patterns, offers, timing and Mike's voice, computed from these emails.
- `INDEX.md` — every email with date, subject, sent, open and click rate.
- `emails/` — one `.md` per email (metrics in front-matter + plain text body) and one `.html` rendered preview with images.
- `assets/images/` — the 438 stored email images.
- `data/emails.csv` — one row per email with metrics and content features (open in Excel/Sheets).
- `data/emails.jsonl` — full records, including preview HTML. `data/sequences.json`, `data/report_meta/` — sequences and report metadata.

Rates are opens/sent and clicks/sent as reported by Kartra. `revenue_field_usd` is Kartra's per-email revenue credit, not reconciled sales. Times are the Pacific source clock.

Regenerate: export the Supabase `kbl_*` tables as CSV, then `python3 scripts/export_archive.py <csv_dir> .`
