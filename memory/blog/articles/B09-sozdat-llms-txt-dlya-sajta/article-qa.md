# QA: B09 sozdat-llms-txt-dlya-sajta (GEO remaster)

date: 2026-07-25
mode: geo_remaster
score_total: 90/100
core_eeat_lite: 18/20
link_verify: pass
research_notes_gate: pass
utility_gate: pass
human_voice_gate: pass
verdict: PASS

## Remaster hard checks

| Check | Result |
|-------|--------|
| html-linter | PASS |
| нет `TL;DR` / `Быстрый инсайт` | PASS |
| видимое `Обновлено: 25.07.2026` | PASS |

## Warnings (не hard-fail remaster)

- **stale research_date:** `research-notes.md` → `2026-06-16` при run date `2026-07-25`. Gate PASS относительно своего `research-context.json` (`today_iso=2026-06-16`), но относительно remaster-даты — warning.
- Контент remaster явно фиксирует: Google Search не использует llms.txt как специальный сигнал.

## Pain → solution → outcome

| Элемент | Где в статье |
|---------|--------------|
| **Боль** | Lead: страх «без llms.txt пропаду из ответов нейросетей», непонятно что класть в файл. |
| **Решение** | H2: развести SEO-миф → 10–30 URL → Markdown → не смешивать robots/sitemap → выложить → llms-full/генератор → поддержка. |
| **Результат** | До FAQ: файл открывается по `/llms.txt`, H1+описания+разделы, нет конфликта с robots, Lighthouse без server error. |

## Scores

| Блок | Вес | Балл | Комментарий |
|------|-----|------|-------------|
| SEO structure | 20 | 19 | H2×7 + FAQ×6; −1 мало внутренних ссылок на блог. |
| GEO / citability | 25 | 23 | Insight без TL;DR, таблица, шаблон, workflow; миф Google снят. |
| CORE-EEAT lite | 15 | 14 | 18/20 |
| Human voice | 15 | 15 | PASS; markers: например / на практике / типичная ошибка / в реальном проекте / часто ломается |
| Fact safety | 15 | 13 | 4 facts, 3 verified, 1 unverified (Ahrefs 137210 — в research) |
| Contract HTML | 10 | 6 | linter PASS + remaster markers; −4 за stale research_date warning |

**Порог PASS выполнен** (score ≥80, CORE-EEAT ≥16, gates PASS; remaster-hard PASS).

## CORE-EEAT lite: 18/20

| ID | ✓/✗ | Примечание |
|----|-----|------------|
| C01–C04 | ✓ | llms txt интент; термины на пальцах |
| O01–O04 | ✓ | action outline; FAQ 6; table + ol |
| R01–R04 | ✓ | standalone answer; Google/Lighthouse/Ahrefs |
| E01–E03 | ✓ | low-cost housekeeping, не GEO-хак |
| Exp01–Exp03 | ✓ | 0 slop; human voice PASS |
| Ept01 | ✓ | шаблон + проверка |
| Ept02 | ✗ | межстатейная перелинковка — до Indexer |

## Script reports

| Скрипт | Verdict | Файл |
|--------|---------|------|
| research-notes gate | PASS | research-notes-gate.json |
| fact-check | PASS | fact-check-report.json |
| link-verify | PASS (5/0 fail) | link-verify.json |
| html-linter | PASS | html-linter-report.json |
| slop-detector | PASS (0 cliches, Flesch RU 80.9) | slop-detector-report.json |
| cannibalization | PASS | cannibalization-report.json |
| utility gate | PASS | utility-gate-report.json |
| human voice gate | PASS | human-voice-report.json |

## Link verify

- site-base: `https://mayai.ru`
- OK: Google AI optimization guide, Chrome Lighthouse llms.txt, llmstxt.org, kv-ai.ru/obuchenie-po-make, t.me/maya_pro

## Schema ready

BlogPosting: present (dateModified 2026-07-25) | FAQPage: yes (6) | author_id: artur-horoshev
