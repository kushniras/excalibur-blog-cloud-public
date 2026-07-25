# GEO remediation rules — Collider KB → mayai.ru

Источник: `GEO_AI_SEO_MASTER_KNOWLEDGE_BASE_COLLIDER_EXPANDED_2026-07-19` (white-hat only).  
Дата внедрения в пайплайн: 2026-07-25.

Это **не** сборник gray/black тактик. В доработку страниц идут только `#risk/white` и официальные/research сигналы.

## Что считать «страницей под доработку»

1. **P0 — Excalibur utility** из `/llms.txt` и `memory/blog/articles/` (живой how-to слой).
2. **P1 — GEO/SEO кластер** (`geo`, `llms.txt`, `indexnow`, `микроразметка`, `перелинковка`, Алиса/нейропоиск).
3. **P2 — тонкий/масштабированный хвост** (короткие посты без H2/FAQ/шагов) — не «улучшать водой», а `noindex` / consolidate / delete по отдельному решению редактора.
4. **Не трогать** gray/black идеи из KB (hidden prompts, fake mentions, preference manipulation).

## Обязательный content template (extractability)

Каждая indexable статья после доработки должна иметь:

1. Прямой ответ / позиция в первом `<p>` (lead 350–500 символов: боль → ответ → результат).
2. Инсайт-`<blockquote>` без ярлыков `TL;DR` / `Быстрый инсайт`.
3. Определения неоднозначных терминов «на пальцах».
4. Проверяемые цифры с датой и источником (из research / fact-bank; без выдуманных %).
5. Comparison `<table>`, если читатель реально выбирает между вариантами.
6. Constraints / when-not-to-use (когда способ не подходит).
7. Primary evidence: docs, GitHub, methodology, расчёт — не только «по исследованиям».
8. Автор/эксперт из `shared/authors-registry.json` + Fact Check Box.
9. Видимая дата обновления в теле (`Обновлено: ДД.ММ.ГГГГ`) + `dateModified` в schema.
10. Internal links на сущности/соседние гайды (2–3).
11. FAQ 5–7 пар, видимый HTML = FAQPage JSON-LD.
12. BlogPosting (+ FAQPage) schema, согласованная с видимым контентом.

## Engine-specific (минимум для mayai.ru)

| Движок | Правило |
|--------|---------|
| Google AI | Indexable HTML, canonical, полезный контент; **не** полагаться на `llms.txt` как на сигнал Google |
| ChatGPT Search | `OAI-SearchBot` Allow в robots (уже на сайте) |
| Perplexity | `PerplexityBot` Allow |
| Яндекс / Алиса | Прямой ответ → сущность → доказательство → ограничение → дата |
| Multi-engine | Не переносить «цитируют в X» как гарантию для Y |

## Мифы, которые правим при remaster

- «Без llms.txt Google AI не увидит» → ложь для Google Search; файл полезен как карта для части агентов, не как ranking-хак.
- «Structured data = магия цитирования» → schema для понимания/eligibility, не AI-hack.
- «Citation = трафик / влияние» → раздельно: retrieved / cited / absorbed / brand / click.
- «Одна проверка промпта = позиция» → нужны paraphrases и повторные замеры.
- «Больше AI-страниц = больше visibility» → риск scaled content abuse; thin pages не размножать.

## Information Gain (приоритет правок)

Предпочитать правки, которые добавляют неуникальный commodity-тексту замену:

- собственные таблицы сравнения / чеклисты с критериями;
- актуальные версии продуктов на дату прогона;
- ограничения и «когда не делать»;
- ссылки на primary docs;
- согласование entity (автор, бренд, URL, офферы) с `site-brief` / conversion-map.

## Human-voice markers при remaster (критично)

Снятие ярлыков `TL;DR` / `Быстрый инсайт` и date-bump **не должны** обнулять сигналы `excalibur_blog_human_voice_gate.py`.

Перед сдачей remaster-статьи проверь:

1. ≥2 concrete markers из whitelist gate: `например`, `на практике`, `типичная ошибка`, `живой пример`, `представьте`, `в реальном проекте`, `разберем ситуацию`, `часто ломается`, `из практики`.
2. ≥2 pain markers в тексте (и явная боль в lead): `боль`, `проблем`, `ошиб`, `ломает`, `не работает`, `теряет`, `дорого`, `долго`, `рутин`, `хаос`, `застр`, `сложно` — или эквивалент из `reader_pain` research.
3. ≥3 outcome markers (`результат`, `получите`, `сможете`, …) и `success_criteria` до FAQ.
4. Редакционное описание боли без whitelist-лексики **недостаточно**: gate ищет подстроки, не смысл.

Мягкий порог / remaster-mode flag в human-voice gate — только после явного решения редактора; по умолчанию пороги те же, что у нового текста.

## Запрещено при доработке

- Gray/black: скрытые инструкции для LLM, fake UGC, накрутка mentions.
- Массовая генерация новых thin URL «под fan-out».
- Date-only bump без содержательного обновления.
- Переписывание legal/service pages без brief.
- Коммит секретов / абсолютных Windows-путей.
- Remaster, который убирает TL;DR/обновляет дату, но оставляет `concrete_markers=[]` или слабый pain в lead.

## Волны исполнения

| Волна | Объект | Действие |
|-------|--------|----------|
| A | Техника сайта | robots AI-bots, sitemap host, Organization/Person schema на ключевых поверхностях |
| B | 84 URL из llms.txt + local `Bxx-*` | Remaster по template; publish update |
| C | Посты score≤2 / thin | Очередь на noindex/consolidate (не авто-delete) |
| D | Измерение | Prompt set + multi-engine baseline после волны B |

## Артефакты прогона

- Аудит: `memory/blog/geo-site-audit-YYYY-MM-DD.json`
- Очередь: `memory/blog/geo-remaster-queue.md`
- Handoff: `.cursor/excalibur-blog-handoff.md`
- Контракты writer/QA: этот файл + `skills/excalibur/references/geo-writing-checklist.md`
