# Excalibur BLOG — pipeline fix queue

Durable incident memory for repeated pipeline problems.

Contract: `shared/pipeline-incident-fix-contract.md`

## Open incidents

(needs-human: INC-20260725-1426-publish-missing-cloud-secrets)

## INC-20260725-1434-indexer-weak-anchor-filter
status: fixed
run_date: 2026-07-25
role: excalibur-blog-indexer
topic_id: multi
article_dir: memory/blog/articles
severity: medium
category: script

### What went wrong
- Full-corpus dry-run на 84 remastered articles дал 172 opportunities; большинство — generic якоря (`один прогон`, `Reload Window`, `критерий готово`, `файл в проекте`, byline `вайбкодинг`).
- Слепой `--apply` на весь отчёт сломал бы интент (UI-chrome → product URL, exclusion mentions → hub).
- После topical filter всё равно пришлось вручную откатить 2 связи: FAQ→JSON-LD (негативное упоминание) и favicon→вайбкодинг (`правило Cursor`).
- Генерация `promotion-checklist.md` на все 84 перезаписала 16 уже curated checklists (B01–B10 + GEO R-*); восстановлены через `git checkout`.

### How the agent recovered this run
- Dry-run → Python-фильтр (weak denylist + topic overlap + caps 2 out / 3 in) → apply 24 → revert 2 → net 22 canonical `/{slug}/`.
- Канонизация residual `href="/blog/{slug}/"` для slug из корпуса (0 residual).
- llms.txt/llms-full.txt пересобраны на 84 URL; publish не запускался.
- Curated promotion-checklists восстановлены; для остальных 68 созданы из template.

### Durable fix needed before next run
- В `excalibur_blog_interlinker.py`: denylist generic/UI якорей + skip exclusion/negative contexts; не полагаться только на skill prose.
- Indexer skill: promotion-checklist — не перезаписывать существующий файл без `--force`; только create-if-missing.
- Опционально: `--max-out` / `--max-in` CLI caps.

### Suggested files to inspect/change
- `scripts/excalibur_blog_interlinker.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-25
fix_summary:
- Interlinker: default quality filter (weak denylist, byline vibe, exclusion/negative context, topic overlap, short_single) + `--max-out`/`--max-in`/`--min-overlap`/`--include-skipped`; `--no-quality-filter` только для отладки.
- Новый `excalibur_blog_promotion_checklist.py`: create-if-missing; overwrite только с `--force`.
- Indexer skill/agent + pitfalls: dry-run → caps → apply; не слепой full-corpus apply; не перезаписывать curated promotion-checklist.
files_changed:
- `scripts/excalibur_blog_interlinker.py`
- `scripts/excalibur_blog_promotion_checklist.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `shared/agent-pipeline-pitfalls.md`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_interlinker.py scripts/excalibur_blog_promotion_checklist.py`
- dry-run 84 articles `--max-out 2 --max-in 3`: kept 14 / raw 143; weak keywords / FAQ→JSON-LD / favicon→vibe not leaked
- promotion-checklist smoke: skipped_exists on B01; create then skip; `--force` → overwritten
commit: pending-parent-commit

## INC-20260725-1426-publish-missing-cloud-secrets
status: needs-human
run_date: 2026-07-25
role: excalibur-blog-publish
topic_id: multi
article_dir: memory/blog/articles (Wave B GEO remaster batch)
severity: blocker
category: env

### What went wrong
- `python3 scripts/excalibur_blog_wp_publish.py --env-check` вернул exit 1.
- `allow_publish=false`; отсутствуют `EXCALIBUR_BLOG_ALLOW_PUBLISH`, `PUBLIC_SITE_URL`, `SSH_HOST`, `SSH_USER`, `SSH_PASS/SSH_PASSWORD`; `SSH_ROOT=unset`.
- Нет `memory/site.env.local` в runtime.
- Wave B remaster batch готов к WP update (B04/B09 + R-* с `wp_post_id`), но publish нельзя без секретов.

### How the agent recovered this run
- Явный `❌ PUBLISH BLOCKER` без угадывания доступов и без dry-run/publish SSH.
- Ledger `shared/published-articles.md` не менялся (publish не прошёл).

### Durable fix needed before next run
- Выставить в Cursor Dashboard Cloud Secrets: `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`, `PUBLIC_SITE_URL`, `SSH_HOST`, `SSH_USER`, `SSH_PASS`/`SSH_PASSWORD`, `SSH_ROOT` (для этого аккаунта часто `.`).
- Либо положить эквивалент в runtime `memory/site.env.local` (не коммитить).
- После секретов — re-run publish update для remaster batch (приоритет: B04, B09, R-mikrorazmetka, R-alisa + остальные R-* с `wp_post_id`).

### Suggested files to inspect/change
- Cursor Dashboard Cloud Secrets (values not recorded)
- `CURSOR-CLOUD-RUNBOOK.md`
- `shared/excalibur-wp-publish-contract.md`
- `skills/publish-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: needs-human
fixed_at: 2026-07-25
reason:
- Credentials / Cloud Secrets нельзя создать кодом; runtime env в этом Cloud run пуст (`--env-check` exit 1).
- Контракт «нет секретов → явный PUBLISH BLOCKER, не silent skip» уже был в skill/AGENTS; усилен в pitfalls, publish skill/agent, WP contract, AGENTS, Cloud runbook.
needed_decision_or_secret:
- Cursor Dashboard → Cloud Agents → Secrets: `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`, `PUBLIC_SITE_URL`, `SSH_HOST`, `SSH_USER`, `SSH_PASS` или `SSH_PASSWORD`, `SSH_ROOT` (часто `.`)
- Затем re-run publish для Wave B remaster batch (не silent skip)
files_changed:
- `shared/agent-pipeline-pitfalls.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-publish.md`
- `.cursor/agents/excalibur-blog-publish.md`
- `shared/excalibur-wp-publish-contract.md`
- `AGENTS.md`
- `CURSOR-CLOUD-RUNBOOK.md`
checks_run:
- `rg` blocker/silent-skip guidance in publish docs
- `python3 scripts/excalibur_blog_wp_publish.py --env-check` (ожидаемо exit 1 без secrets)
commit: f14e938 (hash cleanup 3dd5e97)

## INC-20260725-1425-indexer-interlink-blog-prefix
status: fixed
run_date: 2026-07-25
role: excalibur-blog-indexer
topic_id: multi
article_dir: memory/blog/articles
severity: medium
category: script

### What went wrong
- `excalibur_blog_interlinker.py` hardcodил href `/blog/{slug}/`, тогда как live mayai.ru permalinks — `/{slug}/` (`/blog/{slug}/` только 301).
- llms generator уже использует `--blog-path /` → рассинхрон internal links vs llms.txt/canonical.
- Отдельно: ложный opportunity B03→R-ruleset по якорю «настройка cursor» в фразе «Настройка cursor mcp» (другой интент) — не применяли.

### How the agent recovered this run
- Dry-run → `--apply` только GEO-cluster: R-mikro hub (6) + R-semyadro inbound (1); B09=0; B03→ruleset skipped.
- Переписал вставленные href на канон `/{slug}/` (+ pre-existing B01→B04 в том же файле).
- Исправил `scripts/excalibur_blog_interlinker.py` (target_url / apply / report) на `/{slug}/`.
- Пересобрал `memory/blog/llms.txt` + `llms-full.txt` (24 статьи). Publish не запускался.

### Durable fix needed before next run
- Зафиксировать в pitfalls/indexer skill: mayai.ru internal links = `/{slug}/`, не `/blog/{slug}/`.
- Опционально: фильтр «слабых» якорей (короткий generic «настройка cursor») или require word-boundary + topic overlap перед apply.
- Пройти оставшиеся `href="/blog/..."` в статьях вне GEO-кластера (напр. vajbkoding) — 301 ок, но лучше канон.

### Suggested files to inspect/change
- `scripts/excalibur_blog_interlinker.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-25
fix_summary:
- Interlinker пишет `/{slug}/`; indexer skill + pitfalls документируют канон и dry-run/skip weak anchors.
- GEO-cluster HTML href нормализованы; residual `/blog/vajbkoding-...` вне scope Wave B.
files_changed:
- `scripts/excalibur_blog_interlinker.py`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_interlinker.py`
- dry-run remaining=1 (skipped B03→ruleset)
- live check: `/{slug}/` 200, `/blog/{slug}/` 301
commit: a367517

## INC-20260725-1418-geo-qa-b04-human-voice-remaster
status: fixed
run_date: 2026-07-25
role: excalibur-blog-geo-qa
topic_id: B04
article_dir: memory/blog/articles/B04-geo-optimizaciya-sajta-2026
severity: medium
category: qa

### What went wrong
- После GEO remaster `excalibur_blog_human_voice_gate.py` вернул BLOCK на B04: `concrete_markers=[]` и слабые pain markers (скрипт видит только фрагмент `ошиб`).
- Remaster-hard checks при этом PASS (linter, нет TL;DR, есть `Обновлено: 25.07.2026`).
- Lead редакторски называет боль (SEO без клика из ChatGPT/Алисы), но без whitelist-лексики gate падает.

### How the agent recovered this run
- Зафиксировал remaster-hard PASS и полный GEO QA verdict=FIX в `article-qa.md`.
- `research-notes-gate` BLOCK по legacy notes / stale `research_date=2026-06-11` отмечен как warning для remaster (не hard-fail всего батча).
- Cover/schema для B04 не разблокированы до writer FIX human-voice.
- **Writer hotfix 2026-07-25:** в lead/H2.1–H2.2 добавлены whitelist-маркеры (`например`, `на практике`, `типичная ошибка` + `проблема`/`не работает`/`боль`); KB-правки сохранены; `human_voice_gate` + `html_linter` → PASS; `article-qa.md` verdict=PASS; publish не запускался.

### Durable fix needed before next run
- GEO remaster writer checklist: при снятии ярлыка TL;DR сохранять ≥2 concrete markers (`например`, `на практике`, `типичная ошибка`, …) и явную pain-лексику в lead.
- В `shared/geo-collider-remediation-rules.md` / writer skill добавить строку: remaster не должен обнулять human-voice markers.
- Опционально: remaster-mode flag в human-voice gate с мягким порогом — только после явного решения редактора.

### Suggested files to inspect/change
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/geo-collider-remediation-rules.md`
- `shared/agent-pipeline-pitfalls.md`
- `scripts/excalibur_blog_human_voice_gate.py` (docs/comment; detection корректна)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-25
fix_summary:
- Добавлен блок «Human-voice markers при remaster» в `shared/geo-collider-remediation-rules.md` (whitelist concrete/pain, запрет обнуления при снятии TL;DR; мягкий порог только после решения редактора).
- Writer skill/agent: секция `GEO remaster checklist` + pitfalls/GEO QA note: remaster-hard PASS ≠ human-voice PASS.
- В `excalibur_blog_human_voice_gate.py` — docstring/comment про обязательные ≥2 concrete markers после remaster (detection не ослаблялась).
files_changed:
- `shared/geo-collider-remediation-rules.md`
- `shared/agent-pipeline-pitfalls.md`
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-writer.md`
- `.cursor/agents/excalibur-blog-writer.md`
- `skills/excalibur/references/geo-writing-checklist.md`
- `.cursor/skills/excalibur/references/geo-writing-checklist.md`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `scripts/excalibur_blog_human_voice_gate.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_human_voice_gate.py`
- `rg` на секцию Human-voice markers / GEO remaster checklist
commit: 74596ed

## INC-20260725-1415-writer-b01-duplicate-faq-h2
status: fixed
run_date: 2026-07-25
role: excalibur-blog-writer
topic_id: B01
article_dir: memory/blog/articles/B01-primer-seo-stati
severity: medium
category: qa

### What went wrong
- After GEO remaster, `article.html` had two FAQ-like H2 headings: `FAQ и schema: зачем и как` and `Частые вопросы`.
- `excalibur_blog_html_linter.py` failed with "Forbidden duplicate FAQ sections" because any H2 matching `faq|частые вопрос|задаваемые вопрос` counts as a FAQ block.

### How the agent recovered this run
- Renamed the instructional H2 to `Подключите schema JSON-LD к статье` (kept the explanatory body; left a single `<h2>Частые вопросы</h2>` with 7 h3+p pairs).
- Preserved GEO remaster markers: no TL;DR / Быстрый инсайт; `Обновлено: 25.07.2026` present.
- Recalculated `char_count` in `article.meta.json` to 9375.
- Re-ran HTML linter to PASS.

### Durable fix needed before next run
- Writer / GEO remaster prompts should forbid the word `FAQ` (and FAQ-like RU phrases) in any H2 except the canonical `Частые вопросы`.
- Add a short pitfall note: thematic sections about schema/Q&A must use action titles without `FAQ` in the heading text.

### Suggested files to inspect/change
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `shared/agent-pipeline-pitfalls.md`
- `scripts/excalibur_blog_html_linter.py` (docs/comment only; detection is correct)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-07-25
fix_summary:
- Writing contract / writer skill+agent / geo checklist / pitfalls явно запрещают `FAQ` и FAQ-like RU-фразы в любом H2 кроме канона `Частые вопросы`; schema/Q&A секции — action-title без FAQ-лексики.
- Docstring в `detect_duplicate_faq_sections` документирует, что instructional «FAQ и schema…» тоже считается FAQ-like (detection не менялась).
files_changed:
- `shared/excalibur-article-writing-contract.md`
- `shared/agent-pipeline-pitfalls.md`
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-writer.md`
- `.cursor/agents/excalibur-blog-writer.md`
- `skills/excalibur/references/geo-writing-checklist.md`
- `.cursor/skills/excalibur/references/geo-writing-checklist.md`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `scripts/excalibur_blog_html_linter.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_html_linter.py`
- smoke: duplicate FAQ detect on «FAQ и schema…» + «Частые вопросы»
- `python3 scripts/excalibur_blog_html_linter.py memory/blog/articles/B01-primer-seo-stati/article.html` → PASS
commit: 74596ed

## INC-20260616-2015-geo-qa-html-cli-mismatch
status: fixed
run_date: 2026-06-16
role: excalibur-blog-geo-qa
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: qa

### What went wrong
- `article.html` used `<pre><code>` for the llms.txt template, but `excalibur_blog_html_linter.py` forbids those tags and only allows the strict article whitelist.
- `excalibur_blog_research_notes_gate.py` interprets a relative `-o` path inside `article_dir`; passing a repo-relative path as `-o` produced a nested duplicate output before cleanup.
- `.cursor/skills/excalibur-geo-qa/SKILL.md` instructs `excalibur_blog_cannibalization_guard.py --article-dir ...`, while the actual script accepts `--blog-dir`, `--threshold` and `-o/--output`; the documented command exited with argparse error.

### How the agent recovered this run
- Replaced the template block with whitelist-safe `<blockquote><p><br>` markup without changing the article's practical meaning.
- Removed the unintended nested duplicate `research-notes-gate.json` and kept the canonical file in the article directory.
- Re-ran the cannibalization guard with `--blog-dir memory/blog/articles -o memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta/cannibalization-report.json`; verdict PASS.

### Durable fix needed before next run
- Update Writer/QA contracts to avoid `<pre><code>` in `article.html` unless the linter whitelist is intentionally expanded.
- Update `.cursor/skills/excalibur-geo-qa/SKILL.md` to use the actual cannibalization guard CLI or update the script to support `--article-dir`.

### Suggested files to inspect/change
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `scripts/excalibur_blog_cannibalization_guard.py`
- `scripts/excalibur_blog_html_linter.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Writer/article writing contracts now forbid `<pre>`/`<code>` in `article.html` until the HTML linter whitelist is intentionally expanded, and document whitelist-safe blockquote/table/list alternatives.
- GEO QA skill now documents the actual cannibalization guard CLI: `--blog-dir memory/blog/articles -o <article_dir>/cannibalization-report.json`.
- GEO QA note clarifies that `research_notes_gate.py -o research-notes-gate.json` is relative to `--article-dir`.
files_changed:
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `shared/excalibur-article-writing-contract.md`
- `skills/excalibur-geo-qa/SKILL.md`
- `.cursor/skills/excalibur-geo-qa/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 scripts/excalibur_blog_cannibalization_guard.py --help`
- `rg` check for old Writer `<pre><code>` instruction strings
- `rg` check for old cannibalization `--article-dir` command in source docs
commit: pending-parent-commit

## INC-20260616-2018-cover-toxic-sticker
status: fixed
run_date: 2026-06-16
role: excalibur-blog-cover
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: prompt

### What went wrong
- The one-shot Kie image-to-image quad generation succeeded, but the cover panel included an insulting Russian sticker phrase even though the style preset asks for a non-toxic tone.
- Geometry, white background, hero face, typography and inline utility passed; the issue was limited to one generated sticker text on the top-left cover panel.

### How the agent recovered this run
- Did not launch a second image job.
- Retouched only the offending sticker layer in `cover/cover.png` and the matching top-left area of `cover/canvas-quad.png`, replacing it with a neutral `SEO-МИФ / БЕЗ МАГИИ` sticker.

### Durable fix needed before next run
- Add explicit negative prompt wording for cover/inline generated text: no insults, no toxic labels, no words like `лох`, `лохов`, `для лохов`.
- Consider adding a lightweight post-generation OCR/text QA note to the cover skill when generated Russian sticker text is visible.

### Suggested files to inspect/change
- `memory/cover/quad-style-digital-meme-collage-ru.json`
- `memory/cover/cover-design-code.json`
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Cover style JSON, design code, prompt builder, agent contracts and skill QA now explicitly forbid toxic/insulting generated sticker text while preserving the meme/sticker/collage style.
- Visible text QA now treats words such as `лох`, `лохов`, `для лохов` and similar humiliating labels as a cover blocker.
files_changed:
- `memory/cover/quad-style-digital-meme-collage-ru.json`
- `memory/cover/cover-design-code.json`
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`
- `.cursor/agents/excalibur-blog-cover.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_quad_prompt.py`
- JSON parse for `memory/cover/quad-style-digital-meme-collage-ru.json`
- JSON parse for `memory/cover/cover-design-code.json`
commit: pending-parent-commit

## INC-20260616-1950-scout-wordstat-format
status: fixed
run_date: 2026-06-16
role: excalibur-blog-scout
topic_id: B09
article_dir: n/a
severity: low
category: api

### What went wrong
- `wordstat_get_top_requests` for the narrow phrase `как создать llms txt` returned an unexpected payload shape with only `totalCount`, so the tool wrapper could not print top phrases.

### How the agent recovered this run
- Used the successful broader Wordstat result for `llms.txt`, which included the full semantic tail and showed related actionable phrases such as `создать llms txt`.

### Durable fix needed before next run
- Make the Wordstat MCP wrapper handle low-result responses that include only `totalCount`, or document that Scout should query the broader cluster first.

### Suggested files to inspect/change
- `shared/pipeline-incident-fix-contract.md`
- `agents/excalibur-blog-scout.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Scout agent and skill now require Wordstat cluster-first validation: broad parent query before narrow how-to query.
- `totalCount`-only responses are documented as low-result signals, not fatal tool/API failures; Scout should broaden the query and use the broad cluster for semantic tail.
files_changed:
- `agents/excalibur-blog-scout.md`
- `.cursor/agents/excalibur-blog-scout.md`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` check for Wordstat cluster-first/totalCount guidance in Scout source docs
commit: pending-parent-commit

## INC-20260616-2031-indexer-python-missing
status: fixed
run_date: 2026-06-16
role: excalibur-blog-indexer
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: env

### What went wrong
- The Indexer contract requested `python scripts/excalibur_blog_interlinker.py ...`, but the Cloud shell has no `python` executable.
- The first interlinker command failed with `python: command not found`, forcing a retry.

### How the agent recovered this run
- Re-ran the same interlinker command with `python3`, then used `python3` for the llms generator.
- Both scripts completed successfully after the retry.

### Durable fix needed before next run
- Standardize Indexer shell examples on `python3` or provide a `python` alias in the Cloud environment.

### Suggested files to inspect/change
- `agents/excalibur-blog-indexer.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/environment.json`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- Indexer agent and skill shell examples now use `python3` for interlinker and llms generator.
- Publish post-publish interlinker example also uses `python3`.
files_changed:
- `agents/excalibur-blog-indexer.md`
- `.cursor/agents/excalibur-blog-indexer.md`
- `skills/indexer-excalibur-blog/SKILL.md`
- `.cursor/skills/indexer-excalibur-blog/SKILL.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `rg` check for old `python scripts/excalibur_blog_interlinker.py` and `python scripts/excalibur_blog_llms_generator.py` in source docs
commit: pending-parent-commit


## INC-20260616-2042-publish-ssh-root-dot
status: fixed
run_date: 2026-06-16
role: excalibur-blog-publish
topic_id: B09
article_dir: memory/blog/articles/B09-sozdat-llms-txt-dlya-sajta
severity: low
category: publish

### What went wrong
- A safe env-preflight wrapper initially imported `excalibur_blog_wp_publish.py` without adding `scripts/` to `sys.path`, causing `ModuleNotFoundError: asset_download`; the check was re-run with the correct `sys.path`.
- The first real publish attempt connected over SSH but failed before upload with `FileNotFoundError/ENOENT` because the configured publish root path does not exist inside the SSH account cwd.
- Commit was blocked by Cursor secret-scan because `PUBLIC_SITE_URL`/`WP_SITE_URL` are configured as secrets and appeared in staged publish artifacts; committed copies were redacted to `[REDACTED]` to match repository policy.

### How the agent recovered this run
- Re-ran the env check with `scripts/` on `sys.path`; allow flag, public URL and SSH settings were confirmed without printing secret values.
- Retried publish with `SSH_ROOT=.` so the bootstrap was written to the SSH login cwd; WordPress post, featured image, 3 inline images and schema meta published successfully.
- Replaced public site base in committed artifacts with `[REDACTED]`; live permalink remains available in local runtime handoff and WordPress result before redaction.

### Durable fix needed before next run
- Update Cloud publish root secret to `.` (or remove invalid panel path) for this SSH account, or make `excalibur_blog_wp_publish.py` auto-probe `.` when configured root returns ENOENT before bootstrap upload.
- Document that direct import of publish helpers in ad-hoc checks needs `scripts/` on `sys.path`, or expose a tiny env-check CLI in the script.
- Decide whether `PUBLIC_SITE_URL` should remain a secret-scanned value; if yes, keep committed examples/results redacted by contract.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `CURSOR-CLOUD-RUNBOOK.md`
- Cursor Dashboard Cloud Secrets (`SSH_ROOT` only; no secret values recorded here)

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-06-16
fix_summary:
- `excalibur_blog_wp_publish.py` now has `--env-check` for safe publish env validation without ad-hoc imports or secret output.
- SSH bootstrap upload now retries once at `.` when a configured non-dot root returns ENOENT, and cleanup deletes the actual uploaded remote path.
- Publish skill/runbook document the env-check CLI, `scripts/` sys.path guidance for ad-hoc imports, and the optional Cloud Secret root update to `.` if fallback warning appears.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `CURSOR-CLOUD-RUNBOOK.md`
- `shared/agent-pipeline-pitfalls.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_wp_publish.py`
- `python3 scripts/excalibur_blog_wp_publish.py --env-check` (JSON output validated; non-publish env may return exit 1)
- `python3 -m json.tool /tmp/excalibur_publish_env_check.json`
commit: pending-parent-commit

## Fixed incidents

Handled above; commit is pending Director review.
