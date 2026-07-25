# Excalibur — GEO writing checklist

Адаптация практик из [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) + white-hat правил из Collider GEO KB (`shared/geo-collider-remediation-rules.md`) под Excalibur BLOG HTML.

## Answer-first (первые 60–100 слов)

- Первый `<p>` 350–500 символов: боль → прямой ответ → обещание пользы
- Primary query естественно в первых 100 словах (не stuffing)
- Можно вырезать первый абзац как самостоятельный ответ для AI Overview / Нейро / Алисы
- Яндекс/Алиса: утверждение → доказательство → ограничение → дата (не наоборот)

## Chunkable blocks (на цитирование)

- Минимум **3** блока по **40–60 слов** (определение, «коротко», итог секции)
- Один тезис на абзац; абзацы 3–6 предложений
- H2/H3 читаются как outline без body
- Списки `<ul>/<ol>` для шагов и сравнений
- В каждой крупной секции — constraints / when-not-to-use, если уместно

## Quotable statements

- 2–4 предложения с конкретикой (цифра+источник, named entity, дата)
- Формулировки standalone — без «как сказано выше»
- Источники в `research-notes.md`, в тексте — осторожные маркеры («по данным …», «на момент публикации»)
- Citation ≠ influence: не обещать «попадёте в ChatGPT», если нет измерения; разделять discoverability / citation / absorption

## FAQ (GEO + schema)

- 5–7 пар `<h3>` + `<p>`; вопрос = формулировка из queries/PAA
- Ответ: прямое первое предложение, затем нюанс
- FAQ дублирует видимый контент (для FAQPage JSON-LD)

## Snippet patterns


| Тип          | Паттерн                                                                            |
| ------------ | ---------------------------------------------------------------------------------- |
| Definition   | «[Термин] — это … Важно, потому что …» (40–60 слов)                                |
| How-to       | H2 + текстовая схема-цепочка (`<blockquote>` + `→`) + нумерованный `<ol>` с шагами |
| Comparison   | H2 + сравнительная таблица `<table>` + вердикт эксперта `<blockquote>`             |
| Listicle     | H2 + `<ul>` с parallel phrasing                                                    |
| Visual Media | Внедрено 1–3 `<img>` с подробным `alt` и курсивной подписью `<i>` снизу            |


## Яндекс / Google AI / multi-engine

- Title 50–65 символов, Description 120–160 (в `article.meta.json`)
- Internal links 2–3 из карточки темы
- Нет hidden schema-only FAQ — всё видно в HTML
- Свежесть: видимая строка `Обновлено: ДД.ММ.ГГГГ` в теле + `dateModified` в schema; актуальные версии/цены только из research
- `llms.txt` — навигация для части агентов; **не** позиционировать как сигнал Google AI
- Structured data — для понимания сущности / eligibility Search experiences, не как «GEO-хак»
- Не плодить thin URL под каждую fan-out формулировку (scaled content abuse)

## E-E-A-T & Author Attribution (Авторитетность и Авторы)

- Автор статьи выбран из единого реестра `shared/authors-registry.json` (сейчас: `artur-horoshev`; другие id — только после добавления в реестр)
- Имя автора в Fact Check Box, `article.meta.json` и `schema.jsonld` совпадают с одним `author_id` из реестра
- В статью встроен блок «Мнение эксперта» (`<blockquote>` или отдельный блок) с цитатой выбранного автора

## Anchor Text Diversification (Анкоры перелинковки)

- В `article.meta.json` заполнен блок `"anchor_variants"` (3-5 естественных фраз для ссылок на эту статью из других текстов)
- Использованы разнообразные анкоры (прямые, разбавленные, брендовые) вместо одного и того же коммерческого ключа
- Запущен `excalibur_blog_interlinker.py --apply` для автоматического связывания по диверсифицированным анкорам

## Anti patterns

- Нет «в этой статье вы узнаете»
- Нет стены текста без H2 > 400 слов
- Нет generic AI conclusion («подводя итог», «в заключение»)
- Нет служебных ярлыков `TL;DR` / `Быстрый инсайт` в insight-блоке
- Нет date-only bump без содержательного обновления
- Нет гарантий цитирования AI и путаницы citation с трафиком
