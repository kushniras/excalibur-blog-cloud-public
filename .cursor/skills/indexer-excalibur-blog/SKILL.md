---
name: indexer-excalibur-blog
description: Excalibur BLOG Indexer — interlink между статьями + llms.txt для AI crawlers.
---

# Excalibur BLOG — Indexer

После cover + schema.

## Shell

```bash
# Сначала dry-run (без --apply), затем --apply по нужным --article-dir
python3 scripts/excalibur_blog_interlinker.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --site-base https://mayai.ru

python3 scripts/excalibur_blog_interlinker.py --apply \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --site-base https://mayai.ru

python3 scripts/excalibur_blog_llms_generator.py \
  --blog-dir memory/blog/articles \
  --site-base https://mayai.ru \
  --blog-path / \
  --out-dir memory/blog
```

## Permalink (mayai.ru)

- Канон внутренних ссылок и llms: `https://mayai.ru/{slug}/` / href `/{slug}/`.
- Не использовать `/blog/{slug}/` в новых вставках (на сайте это только 301).
- Перед apply отбрасывай слабые якоря (например generic «настройка cursor» вне интента target).

## Выход

- обновлённый `article.html` (контекстные ссылки)
- `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- `promotion-checklist.md` из `skills/excalibur/references/promotion-checklist-template.md`
