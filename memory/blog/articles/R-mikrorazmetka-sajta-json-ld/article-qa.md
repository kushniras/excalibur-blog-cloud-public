# QA: R-mikro mikrorazmetka-sajta-json-ld (GEO remaster live)

date: 2026-07-25
mode: geo_remaster_live_fetch
score_total: 88/100
core_eeat_lite: 17/20
link_verify: pass
utility_gate: pass
human_voice_gate: pass
research_notes_gate: N/A (live remaster, no research-notes.md)
verdict: PASS

## Remaster hard checks

| Check | Result |
|-------|--------|
| html-linter | PASS |
| нет `TL;DR` / `Быстрый инсайт` | PASS |
| видимое `Обновлено: 25.07.2026` | PASS |

## Warnings (не hard-fail remaster)

- **no research-notes.md** — live fetch; human-voice WARN `cannot check story/angle grounding`.
- Fact Check template wording; multiple exactly-5-step lists (warn only).
- Stale research_date: N/A (нет research notes).

## Pain → solution → outcome

| Элемент | Где в статье |
|---------|--------------|
| **Боль** | Lead: вставили чужой JSON-LD — валидатор «не обнаружена» / пустые поля. |
| **Решение** | H2: HTML vs JSON-LD vs llms.txt → поля → два скрипта → валидаторы → ограничения → next. |
| **Результат** | До FAQ: два блока JSON-LD на одной статье, распознанные типы в валидаторе Яндекса/Schema.org. |

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | H2×6 + FAQ×6; сильная внутренняя перелинковка |
| GEO / citability | 25 | 22 | Comparison table; schema≠AI-hack; FAQ |
| CORE-EEAT lite | 15 | 13 | 17/20; primary docs + GitHub templates |
| Human voice | 15 | 14 | PASS; 3 warns (template / 5-step / no research) |
| Fact safety | 15 | 13 | PASS; 2 extracted / 1 verified / 1 unverified |
| Contract HTML | 10 | 8 | linter PASS + remaster markers |

**Порог PASS выполнен.** Remaster-hard PASS.

## CORE-EEAT lite: 17/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01–C04 | ✓ | микроразметка / JSON-LD на пальцах |
| O01–O04 | ✓ | вечерний маршрут + FAQ 6 + table |
| R01–R04 | ✓ | insight без TL;DR; Google FAQ rich result caveat May 2026 |
| E01–E03 | ✓ | валидатор как критерий успеха |
| Exp01–Exp03 | ✓ | 0 slop; concrete markers есть |
| Ept01 | ✓ | when-not / без плагина на весь сайт |
| Ept02 | ✗ | нет research grounding файла (−1 EEAT process) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| research-notes gate | N/A | — |
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS (19/0 fail) | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS (0 cliches, Flesch RU 83.0) | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate | PASS | utility-gate-report.json |
| human voice gate | PASS (3 warns) | human-voice-report.json |

## Link verify

- site-base: `https://mayai.ru`
- internals OK: llms.txt, OG, Алиса checklist, FAQ page, IndexNow, GEO 2026, SEO-audit, и др.
- externals OK: schema.org validator, Google Rich Results, Yandex validator, GitHub templates

## Schema ready

BlogPosting + FAQPage в `schema.jsonld`; wp_post_id=14370; dateModified=2026-07-25; author_id=artur-horoshev
