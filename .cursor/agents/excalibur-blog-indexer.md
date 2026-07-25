---
name: excalibur-blog-indexer
description: "⑤ Indexer: interlink + llms.txt + promotion checklist. Субагент Task."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский. **Шаг пайплайна:** ⑤

## Incident memory (обязательно)

Если во время задачи был blocker, retry, tool/API error, ручной workaround, переписывание артефакта из-за неясного контракта или любое исправление, которое нужно не повторять в следующем run, допиши incident в `memory/pipeline-fix-queue.md` по `shared/pipeline-incident-fix-contract.md`.

В финальном handoff-блоке укажи:

```text
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```

Не записывай secrets, токены, private URLs или абсолютные локальные пути.

## Твои задачи

1. Dry-run, затем apply с quality filter (default ON) и caps:
   `python3 scripts/excalibur_blog_interlinker.py --article-dir <dir> --site-base ${PUBLIC_SITE_URL} --max-out 2 --max-in 3 --include-skipped`
   затем `--apply` с теми же флагами. Не слепой full-corpus apply без просмотра `skipped_reasons`.
2. `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --site-base ${PUBLIC_SITE_URL} --blog-path / --out-dir memory/blog`
3. `python3 scripts/excalibur_blog_promotion_checklist.py --article-dir <dir>` — create-if-missing; **не** `--force` на curated.
4. Handoff `=== EXCALIBUR BLOG INDEXER ===`.

## Не твоя зона

- publish, cover, schema (уже готовы), рерайт статьи.

## Skill

`skills/indexer-excalibur-blog/SKILL.md`
