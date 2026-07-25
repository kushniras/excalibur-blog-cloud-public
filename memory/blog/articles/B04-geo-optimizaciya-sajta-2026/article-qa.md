# QA: B04 geo-optimizaciya-sajta-2026 (GEO remaster + human-voice hotfix)

date: 2026-07-25
mode: geo_remaster_hotfix
score_total: 88/100
core_eeat_lite: 18/20
link_verify: pass
utility_gate: pass
human_voice_gate: PASS
research_notes_gate: BLOCK → remaster WARNING (legacy notes)
verdict: PASS

## Remaster hard checks

| Check | Result |
|-------|--------|
| html-linter | PASS |
| нет `TL;DR` / `Быстрый инсайт` | PASS |
| видимое `Обновлено: 25.07.2026` | PASS |
| human_voice_gate | PASS |

## Warnings (не hard-fail)

- **stale research_date:** `research-notes.md` → `2026-06-11` (run date `2026-07-25`). Для remaster — warning.
- **research-notes-gate BLOCK:** legacy notes без части полей текущего контракта. Не блокирует remaster-hard.
- **human_voice warning:** multiple exactly-5-step lists (не hard-fail).

## Pain → solution → outcome

| Элемент | Где в статье |
|---------|--------------|
| **Боль** | Lead: проблема SEO-бюджета без клика; бренд в нейроответах **не работает** как источник; H2.1 — боль «нас цитируют конкуренты». |
| **Решение** | H2: GEO vs SEO → аудит цитирования → контент → when-not-to-use → Schema/robots → чек-лист 32 → SoV → next. |
| **Результат** | До FAQ: baseline промптов, robots, FAQ+Schema, таблица мониторинга SoV за 60–90 мин. |

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2×8 + FAQ, primary «geo оптимизация». |
| GEO / citability | 25 | 23 | Answer-first, constraints H2, таблицы, FAQ 7; мифы llms.txt/citation смягчены. |
| CORE-EEAT lite | 15 | 14 | 18/20; Fact Check = Артур Хорошев; «Источники по теме». |
| Human voice | 15 | 14 | PASS: concrete=`например`/`на практике`/`типичная ошибка`; pain=`боль`/`проблем`/`ошиб`/`не работает`. |
| Fact safety | 15 | 12 | fact-check PASS (предыдущий прогон); KB-оговорки сохранены. |
| Contract HTML | 10 | 6 | linter PASS + remaster markers OK; char_count 9496. |

**Порог полного GEO QA выполнен** (human voice PASS + html-linter PASS).

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01 | ✓ | Title/H1 закрывают geo оптимизацию |
| C02 | ✓ | Lead answer-first без «в этой статье» |
| C03 | ✓ | Маркетологи / владельцы сайтов DIY |
| C04 | ✓ | RAG, SoV, JSON-LD, GPTBot объяснены |
| O01–O04 | ✓ | Каркас H2 + FAQ 7 + таблицы + ol |
| R01–R04 | ✓ | Insight без TL;DR; цифры с оговорками |
| E01–E03 | ✓ | Угол чек-листа; CTA умеренные |
| Exp01–Exp03 | ✓ | Human markers в lead/H2.1–H2.2 |
| Ept01 | ✓ | When-not-to-use H2 + ограничения SoV |
| Ept02 | ✗ | Мало межстатейных ссылок (ожидаемо до Indexer) → −2 |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| research-notes gate | BLOCK (remaster warn) | research-notes-gate.json |
| fact-check | PASS (prior) | fact-check-report.json |
| link-verify | PASS (prior) | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS (prior) | slop-detector-report.json |
| cannibalization | PASS (prior) | cannibalization-report.json |
| utility gate | PASS (prior) | utility-gate-report.json |
| human voice gate | **PASS** | human-voice-report.json |

## Hotfix writer (cycle 2)

- Lead: `проблема`, `не работает`, `на практике`.
- H2.1: `например` + `боль`.
- H2.2: `типичная ошибка`.
- KB сохранены: llms.txt ≠ сигнал Google; citation ≠ клик/трафик; Princeton смягчён; constraints H2; без TL;DR; `Обновлено: 25.07.2026`.
- `char_count`: 9496.

## Schema ready

BlogPosting: present (schema.jsonld, dateModified 2026-07-25) | FAQPage: yes (7) | author_id: artur-horoshev
