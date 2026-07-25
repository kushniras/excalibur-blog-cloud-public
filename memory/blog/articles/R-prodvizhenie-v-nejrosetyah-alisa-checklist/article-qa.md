# QA: R-alisa prodvizhenie-v-nejrosetyah-alisa-checklist (GEO remaster live)

date: 2026-07-25
mode: geo_remaster_live_fetch
score_total: 89/100
core_eeat_lite: 18/20
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
- Fact Check template; multiple exactly-5-step lists (warn only).
- Stale research_date: N/A.

## Pain → solution → outcome

| Элемент | Где в статье |
|---------|--------------|
| **Боль** | Lead: статья в топ-15, конкурент в ответе Алисы; страх агентства «под ключ». |
| **Решение** | H2: SEO vs нейросети → индекс/извлекаемость → таблица цитат → Вебмастер → DIY vs агентство → next. |
| **Результат** | До FAQ: отметки по 5–10 запросам, раздел видимости в Вебмастере (или «недостаточно данных»), одна страница с H2-вопросом + ответ 40–80 слов + FAQ. |

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 18 | H2×6 + FAQ×6; citation≠клик разведены |
| GEO / citability | 25 | 23 | Чеклист Алисы; 2 таблицы; Wordstat цифры с датой |
| CORE-EEAT lite | 15 | 14 | 18/20 |
| Human voice | 15 | 14 | PASS; story Оли + markers; 3 warns |
| Fact safety | 15 | 12 | PASS; 4 extracted / 1 verified / 3 unverified |
| Contract HTML | 10 | 8 | linter PASS + remaster markers |

**Порог PASS выполнен.** Remaster-hard PASS.

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01–C04 | ✓ | продвижение в нейросетях / Алиса на пальцах |
| O01–O04 | ✓ | вечерний DIY + FAQ 6 + tables |
| R01–R04 | ✓ | 46,5 млн / даты Вебмастера; без гарантий «в Алису за сутки» |
| E01–E03 | ✓ | таблица цитат как первый результат |
| Exp01–Exp03 | ✓ | 0 slop; human markers |
| Ept01 | ✓ | constraints / не агентство первым шагом |
| Ept02 | ✗ | нет research-notes grounding (−1 process) |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| research-notes gate | N/A | — |
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS (12/0 fail) | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS (0 cliches, Flesch RU 63.7) | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate | PASS | utility-gate-report.json |
| human voice gate | PASS (3 warns) | human-voice-report.json |

## Link verify

- site-base: `https://mayai.ru`
- internals OK: GEO 2026, IndexNow, llms.txt, SEO-audit, Wordstat, вайбкодинг
- externals OK: GitHub skills, ClawHub, kv-ai, Telegram, author page

## Schema ready

BlogPosting + FAQPage в `schema.jsonld`; wp_post_id=14332; dateModified=2026-07-25; author_id=artur-horoshev
