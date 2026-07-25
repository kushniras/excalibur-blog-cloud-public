---
name: indexer-excalibur-blog
description: Excalibur BLOG Indexer — interlink между статьями + llms.txt для AI crawlers.
---

# Excalibur BLOG — Indexer

После cover + schema.

## Shell

```bash
# Сначала dry-run (без --apply). Quality filter включён по умолчанию.
python3 scripts/excalibur_blog_interlinker.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --site-base https://mayai.ru \
  --max-out 2 --max-in 3 \
  --include-skipped

# --apply только после просмотра report / skipped_reasons
python3 scripts/excalibur_blog_interlinker.py --apply \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --site-base https://mayai.ru \
  --max-out 2 --max-in 3

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base https://mayai.ru \
  --blog-path / \
  --out-dir memory/blog

# promotion-checklist: create-if-missing (не перезаписывает curated)
python3 scripts/excalibur_blog_promotion_checklist.py \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

Полный корпус: тот же dry-run → смотри `skipped_reasons` → `--apply` с `--max-out`/`--max-in`.  
Не делай слепой `--apply` на сырой отчёт без quality filter.

## Permalink (mayai.ru)

- Канон внутренних ссылок и llms: `https://mayai.ru/{slug}/` / href `/{slug}/`.
- Не использовать `/blog/{slug}/` в новых вставках (на сайте это только 301).

## Quality filter (в скрипте, default ON)

`excalibur_blog_interlinker.py` отбрасывает:

- generic/UI якоря (denylist: `один прогон`, `Reload Window`, `критерий готово`, `файл в проекте`, `настройка cursor`, `правило cursor`, …);
- byline «вайбкодинг» / автор курса;
- exclusion/negative contexts (`не тратьте…`, `ради формата`, …);
- low topic-overlap source/keyword ↔ target;
- short single-token generic anchors без overlap.

CLI:

- `--max-out N` / `--max-in N` — caps после фильтра (рекомендуется 2 / 3 на full-corpus);
- `--min-overlap` (default 1);
- `--include-skipped` — samples в JSON;
- `--no-quality-filter` — только для отладки, не для production apply.

## promotion-checklist.md

- Создавай через `excalibur_blog_promotion_checklist.py` (create-if-missing).
- **Не перезаписывай** существующий файл: curated checklists (B01–B10, GEO hubs) сохраняются.
- `--force` — только при явной необходимости регенерировать из template.

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` (created or skipped_exists)
