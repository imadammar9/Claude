# Staff handbooks

Source for the two internal staff handbooks in `handbooks/`, styled like the Tadawa Secretary Handbook V3 (sticky search sidebar, reading progress, numbered chapter cards, callouts, foldable step-by-step workflows, print styles).

| Output | Content source | Google Doc |
| --- | --- | --- |
| `handbooks/secretary-nursing-handbook-ar.html` | `secretary_ar.py` | دليل عمل السكرتارية والتمريض – تداوى – نسخة منقحة 2026-10-28 |
| `handbooks/family-doctor-handbook-en.html` | `family_doctor_en.py` | Tadawa Family Doctor Workflow Handbook – Revised 2026-10-28 |

Each output is one self-contained HTML file (logo embedded, no external requests), so it can be shared on Drive or WhatsApp and opened offline.

Rebuild after editing a content file:

```bash
python3 -I tools/handbooks/build.py tools/handbooks/secretary_ar.py handbooks/secretary-nursing-handbook-ar.html
python3 -I tools/handbooks/build.py tools/handbooks/family_doctor_en.py handbooks/family-doctor-handbook-en.html
```

`style.css` is the V3 stylesheet unchanged; small additions live in `EXTRA` inside `build.py`.
The pages carry `noindex, nofollow` and `/handbooks/` is disallowed in `robots.txt`, but anything in this repo is still reachable by URL once the site is deployed.
