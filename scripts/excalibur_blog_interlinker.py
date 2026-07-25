#!/usr/bin/env python3
"""Excalibur BLOG Interlinker: Hub-and-Spoke internal linking manager.

Scans articles in memory/blog/articles/, matches keywords to other articles,
and generates linking recommendations or automatically injects links.

Quality filters (default ON) drop weak/UI/generic anchors, byline mentions,
negative/exclusion contexts, low topic-overlap pairs, and enforce optional
per-article inbound/outbound caps before --apply.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


# Generic / UI-chrome anchors that must not become product/hub links.
WEAK_KEYWORD_EXACT = frozenset(
    {
        "один прогон",
        "reload window",
        "критерий готово",
        "файл в проекте",
        "run once",
        "один экран",
        "watch updates",
        "local plugins",
        "favicon.ico",
        "правило cursor",
        "настройка cursor",
        "промпт cursor",
        "5–15 фраз",
        "5-15 фраз",
        "лимит в день",
        "часовой пояс",
        "временный слот",
        "статус в sheets",
        "sheets и пуш",
        "черновик на диске",
        "черновик seo",
        "тестовая заявка",
        "ответ на заявку",
        "монтаж эфира",
    }
)

# Single-token keywords shorter than this (chars) need strong topic overlap
# or a product-like shape; otherwise skipped as short_single.
SHORT_SINGLE_MAX_LEN = 8

STOPWORDS = frozenset(
    {
        "и",
        "или",
        "для",
        "на",
        "в",
        "во",
        "с",
        "со",
        "по",
        "к",
        "от",
        "из",
        "как",
        "что",
        "это",
        "the",
        "a",
        "an",
        "to",
        "of",
        "for",
        "and",
        "or",
        "in",
        "on",
        "with",
        "ai",
        "seo",
        "geo",
        "mcp",
        "api",
        "url",
        "http",
        "https",
        "com",
        "ru",
        "www",
        "статья",
        "сайт",
        "сайта",
        "курс",
        "автора",
        "автор",
    }
)

BYLINE_CONTEXT_RE = re.compile(
    r"(автор\s+курса|ceo\b|byline|автор[:\s]|курс[аеу]?\s+по)",
    re.IGNORECASE,
)

# Negative / exclusion mention near the matched anchor.
NEGATIVE_CONTEXT_RE = re.compile(
    r"("
    r"не\s+трать\w*"
    r"|не\s+нужн\w*"
    r"|не\s+стоит\w*"
    r"|не\s+надо\b"
    r"|не\s+следует\w*"
    r"|не\s+использу\w*"
    r"|не\s+ставь\w*"
    r"|не\s+делайте\w*"
    r"|не\s+для\b"
    r"|без\s+\w{0,20}"
    r"|ради\s+формата"
    r"|уже\s+нет\s+в\s+выдач"
    r"|исключ\w*"
    r"|негатив\w*"
    r"|не\s+ссыла\w*"
    r")",
    re.IGNORECASE,
)

TOKEN_RE = re.compile(r"[a-zа-яё0-9]{3,}", re.IGNORECASE)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def normalize_keyword(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip().lower())


def tokenize(*parts: str) -> set[str]:
    tokens: set[str] = set()
    for part in parts:
        if not part:
            continue
        # Slug-style separators → spaces
        text = str(part).replace("-", " ").replace("_", " ").replace("/", " ")
        for tok in TOKEN_RE.findall(text.lower()):
            if tok in STOPWORDS:
                continue
            tokens.add(tok)
    return tokens


def load_all_articles(blog_dir: Path) -> list[dict[str, Any]]:
    articles = []
    if not blog_dir.is_dir():
        return articles

    for article_dir in blog_dir.iterdir():
        if not article_dir.is_dir():
            continue
        meta_path = article_dir / "article.meta.json"
        html_path = article_dir / "article.html"
        if meta_path.is_file() and html_path.is_file():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                html_content = html_path.read_text(encoding="utf-8")
                articles.append({
                    "topic_id": meta.get("topic_id", article_dir.name),
                    "slug": meta.get("slug", ""),
                    "title": meta.get("title") or meta.get("h1", ""),
                    "primary_query": meta.get("primary_query", ""),
                    "secondary_queries": meta.get("secondary_queries", []),
                    "anchor_variants": meta.get("anchor_variants", []),
                    "html_path": html_path,
                    "meta_path": meta_path,
                    "html_content": html_content,
                    "dir_name": article_dir.name,
                })
            except Exception as e:
                print(f"Error loading {article_dir.name}: {e}")
    return articles


def article_topic_tokens(article: dict[str, Any]) -> set[str]:
    secondary = article.get("secondary_queries") or []
    anchors = article.get("anchor_variants") or []
    return tokenize(
        article.get("slug", ""),
        article.get("title", ""),
        article.get("primary_query", ""),
        article.get("dir_name", ""),
        " ".join(secondary) if isinstance(secondary, list) else str(secondary),
        " ".join(anchors) if isinstance(anchors, list) else str(anchors),
    )


def find_linking_opportunities(articles: list[dict[str, Any]], site_base: str) -> list[dict[str, Any]]:
    suggestions = []
    # Normalize site base URL
    site_base = site_base.rstrip("/")

    for target in articles:
        target_slug = target["slug"]
        if not target_slug:
            continue

        # Prefer /{slug}/ when blog_path is root; never hardcode mayai.ru (forbidden customer target).
        target_url = f"{site_base}/{target_slug}/"
        # Prioritize natural anchor variants for diversification, then primary, then secondary queries
        raw_keywords = target.get("anchor_variants", []) + [target["primary_query"]] + target["secondary_queries"]
        # Remove duplicates while preserving order
        seen = set()
        keywords = []
        for k in raw_keywords:
            if k and k.strip():
                k_clean = k.strip()
                if k_clean not in seen:
                    seen.add(k_clean)
                    keywords.append(k_clean)

        if not keywords:
            continue

        for source in articles:
            if source["topic_id"] == target["topic_id"]:
                continue  # Don't link to itself

            source_html = source["html_content"]
            # Check if source already links to target slug
            if target_slug in source_html:
                continue  # Already linked

            for keyword in keywords:
                # Find occurrences of keyword in source HTML, avoiding inside existing <a> tags or headings
                # Handle multi-word phrases vs single words for Russian word endings
                if " " in keyword:
                    pattern = re.compile(rf"\b({re.escape(keyword)})\b", re.IGNORECASE)
                else:
                    pattern = re.compile(rf"\b({re.escape(keyword)}[а-яё]*)\b", re.IGNORECASE)

                matches = list(pattern.finditer(source_html))
                for match in matches:
                    start_idx, end_idx = match.span()
                    matched_text = match.group(1)

                    # Simple validation: make sure it's not inside a tag (e.g. href="...") or within <a>...</a>
                    # We can check if there's an open <a> before this match that isn't closed yet.
                    # Or simpler: if the match is inside <...> or immediately surrounded by <a>
                    before = source_html[:start_idx]
                    after = source_html[end_idx:]

                    # Check if inside a tag
                    if before.count("<") > before.count(">"):
                        continue  # Inside tag attributes/brackets

                    # Check if inside <a>...</a>
                    # Count open and close <a> tags before match
                    open_a = before.lower().count("<a ") + before.lower().count("<a>")
                    close_a = before.lower().count("</a>")
                    if open_a > close_a:
                        continue  # Inside an active anchor link

                    # Check if inside heading tags like <h2>, <h3>
                    open_h = before.lower().count("<h1") + before.lower().count("<h2") + before.lower().count("<h3")
                    close_h = before.lower().count("</h1>") + before.lower().count("</h2>") + before.lower().count("</h3")
                    if open_h > close_h:
                        continue  # Inside a heading tag

                    # Found a valid opportunity!
                    suggestions.append({
                        "source_topic_id": source["topic_id"],
                        "source_dir": source["dir_name"],
                        "source_slug": source["slug"],
                        "target_topic_id": target["topic_id"],
                        "target_dir": target["dir_name"],
                        "target_slug": target["slug"],
                        "target_url": target_url,
                        "keyword": keyword,
                        "matched_text": matched_text,
                        "context": source_html[max(0, start_idx-60):min(len(source_html), end_idx+60)].strip().replace("\n", " "),
                        "start_idx": start_idx,
                        "end_idx": end_idx,
                    })
                    break  # Suggest one link per source-target-keyword pair to prevent over-linking
    return suggestions


def filter_suggestions_for_article(
    suggestions: list[dict[str, Any]],
    article_dir: Path | None,
    articles: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    if not article_dir:
        return suggestions
    article_dir = article_dir.resolve()
    selected = None
    for article in articles:
        if article["html_path"].parent.resolve() == article_dir:
            selected = article
            break
    if not selected:
        raise ValueError(f"article-dir not found in loaded articles: {article_dir}")
    topic_id = selected["topic_id"]
    # New article indexing needs both outbound links from it and inbound links to it.
    return [
        suggestion
        for suggestion in suggestions
        if suggestion["source_topic_id"] == topic_id or suggestion["target_topic_id"] == topic_id
    ]


def suggestion_skip_reason(
    sug: dict[str, Any],
    articles_by_topic: dict[str, dict[str, Any]],
    *,
    min_overlap: int,
) -> str | None:
    """Return skip reason code or None if suggestion is acceptable."""
    keyword_norm = normalize_keyword(sug.get("keyword", ""))
    matched_norm = normalize_keyword(sug.get("matched_text", ""))
    context = sug.get("context") or ""

    if keyword_norm in WEAK_KEYWORD_EXACT or matched_norm in WEAK_KEYWORD_EXACT:
        return "weak_keyword"

    # Byline / course-author mentions (e.g. «автор курса … вайбкодингу»).
    if "вайбкодинг" in keyword_norm or "вайбкодинг" in matched_norm:
        if BYLINE_CONTEXT_RE.search(context):
            return "byline_vibe"
        # Bare vibe keyword without topical product intent is still weak.
        return "weak_keyword"

    if NEGATIVE_CONTEXT_RE.search(context):
        return "exclusion_mention"

    source = articles_by_topic.get(sug["source_topic_id"], {})
    target = articles_by_topic.get(sug["target_topic_id"], {})
    source_tokens = article_topic_tokens(source)
    target_tokens = article_topic_tokens(target)
    keyword_tokens = tokenize(sug.get("keyword", ""), sug.get("matched_text", ""))
    overlap = (source_tokens | keyword_tokens) & target_tokens
    # Prefer keyword↔target topical fit; source tokens help hub/spoke cohesion.
    keyword_target_overlap = keyword_tokens & target_tokens
    score = len(keyword_target_overlap) if keyword_target_overlap else len(overlap)

    words = keyword_norm.split()
    is_short_single = len(words) == 1 and len(keyword_norm) <= SHORT_SINGLE_MAX_LEN
    if is_short_single and score < max(min_overlap, 1):
        return "short_single"

    if score < min_overlap:
        return "low_topic_overlap"

    return None


def filter_quality_suggestions(
    suggestions: list[dict[str, Any]],
    articles: list[dict[str, Any]],
    *,
    min_overlap: int = 1,
    max_out: int | None = None,
    max_in: int | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, int]]:
    """Apply weak-anchor / exclusion / overlap filters and optional degree caps.

    Returns (kept, skipped_with_reason, reason_counts).
    Caps keep longer / more specific keywords first.
    """
    articles_by_topic = {a["topic_id"]: a for a in articles}
    kept: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    reason_counts: dict[str, int] = defaultdict(int)

    for sug in suggestions:
        reason = suggestion_skip_reason(sug, articles_by_topic, min_overlap=min_overlap)
        if reason:
            skipped.append({**sug, "skip_reason": reason})
            reason_counts[reason] += 1
            continue
        kept.append(sug)

    # Prefer multi-word / longer anchors when capping.
    def specificity(s: dict[str, Any]) -> tuple[int, int]:
        kw = s.get("keyword") or ""
        return (len(kw.split()), len(kw))

    kept.sort(key=specificity, reverse=True)

    out_counts: dict[str, int] = defaultdict(int)
    in_counts: dict[str, int] = defaultdict(int)
    # One link per source→target pair after quality filter.
    seen_pairs: set[tuple[str, str]] = set()
    capped: list[dict[str, Any]] = []

    for sug in kept:
        pair = (sug["source_topic_id"], sug["target_topic_id"])
        if pair in seen_pairs:
            skipped.append({**sug, "skip_reason": "duplicate_pair"})
            reason_counts["duplicate_pair"] += 1
            continue
        if max_out is not None and out_counts[sug["source_topic_id"]] >= max_out:
            skipped.append({**sug, "skip_reason": "max_out"})
            reason_counts["max_out"] += 1
            continue
        if max_in is not None and in_counts[sug["target_topic_id"]] >= max_in:
            skipped.append({**sug, "skip_reason": "max_in"})
            reason_counts["max_in"] += 1
            continue
        seen_pairs.add(pair)
        out_counts[sug["source_topic_id"]] += 1
        in_counts[sug["target_topic_id"]] += 1
        capped.append(sug)

    # Stable order for apply: by source then start_idx
    capped.sort(key=lambda s: (s["source_dir"], s["start_idx"]))
    return capped, skipped, dict(reason_counts)


def apply_interlinks(suggestions: list[dict[str, Any]], articles: list[dict[str, Any]]) -> int:
    applied_count = 0
    # Group suggestions by source article path to modify each file once
    by_source: dict[Path, list[dict[str, Any]]] = {}

    for sug in suggestions:
        src_article = next((a for a in articles if a["topic_id"] == sug["source_topic_id"]), None)
        if src_article:
            by_source.setdefault(src_article["html_path"], []).append(sug)

    for html_path, sugs in by_source.items():
        # Sort suggestions in reverse order of index so offset changes don't affect previous indices
        sugs.sort(key=lambda s: s["start_idx"], reverse=True)
        content = html_path.read_text(encoding="utf-8")

        for sug in sugs:
            # Re-verify that context matches just in case
            matched_text = sug["matched_text"]
            start = sug["start_idx"]
            end = sug["end_idx"]

            if content[start:end] == matched_text:
                link_html = f'<a href="/{sug["target_slug"]}/">{matched_text}</a>'
                content = content[:start] + link_html + content[end:]
                applied_count += 1

        html_path.write_text(content, encoding="utf-8")
        print(f"Applied {len(sugs)} internal links to {html_path.name}")

    return applied_count


def main() -> int:
    ap = argparse.ArgumentParser(description="Excalibur BLOG Hub-and-Spoke Interlinker")
    ap.add_argument("--blog-dir", type=Path, default=None, help="Path to articles/ directory")
    ap.add_argument("--article-dir", type=Path, default=None, help="Limit suggestions to one article as source or target")
    ap.add_argument("--site-base", type=str, default="https://example.com", help="Base site URL")
    ap.add_argument("--apply", action="store_true", help="Directly edit html files to apply links")
    ap.add_argument("--output", type=Path, default=None, help="Output path for JSON suggestions report")
    ap.add_argument(
        "--max-out",
        type=int,
        default=None,
        help="Max outbound new links per source article after quality filter (e.g. 2)",
    )
    ap.add_argument(
        "--max-in",
        type=int,
        default=None,
        help="Max inbound new links per target article after quality filter (e.g. 3)",
    )
    ap.add_argument(
        "--min-overlap",
        type=int,
        default=1,
        help="Minimum topic-token overlap (keyword/source ↔ target); default 1",
    )
    ap.add_argument(
        "--no-quality-filter",
        action="store_true",
        help="Disable weak-anchor / exclusion / overlap filters (not recommended)",
    )
    ap.add_argument(
        "--include-skipped",
        action="store_true",
        help="Include skipped suggestions (+ reasons) in JSON report",
    )
    args = ap.parse_args()

    root = project_root()
    blog_dir = args.blog_dir or root / "memory/blog/articles"
    if not blog_dir.is_absolute():
        blog_dir = root / blog_dir

    if not blog_dir.is_dir():
        print(f"Blog directory not found: {blog_dir}")
        return 1

    articles = load_all_articles(blog_dir)
    print(f"Loaded {len(articles)} articles from memory.")

    raw_suggestions = find_linking_opportunities(articles, args.site_base)
    article_dir = args.article_dir
    if article_dir and not article_dir.is_absolute():
        article_dir = root / article_dir
    raw_suggestions = filter_suggestions_for_article(raw_suggestions, article_dir, articles)
    print(f"Raw opportunities (pre-filter): {len(raw_suggestions)}")

    skipped: list[dict[str, Any]] = []
    reason_counts: dict[str, int] = {}
    if args.no_quality_filter:
        suggestions = raw_suggestions
        print("Quality filter: OFF (--no-quality-filter)")
    else:
        suggestions, skipped, reason_counts = filter_quality_suggestions(
            raw_suggestions,
            articles,
            min_overlap=max(0, args.min_overlap),
            max_out=args.max_out,
            max_in=args.max_in,
        )
        print(
            f"Quality filter: kept {len(suggestions)} / {len(raw_suggestions)} "
            f"(skipped_reasons={reason_counts or '{}'}"
            f"{f', max_out={args.max_out}' if args.max_out is not None else ''}"
            f"{f', max_in={args.max_in}' if args.max_in is not None else ''})"
        )

    print(f"Found {len(suggestions)} internal linking opportunities.")

    report: dict[str, Any] = {
        "site_base": args.site_base,
        "total_articles": len(articles),
        "raw_opportunities": len(raw_suggestions),
        "opportunities_found": len(suggestions),
        "quality_filter": not args.no_quality_filter,
        "min_overlap": args.min_overlap,
        "max_out": args.max_out,
        "max_in": args.max_in,
        "skipped_reasons": reason_counts,
        "suggestions": [
            {
                "source": s["source_dir"],
                "target": s["target_dir"],
                "keyword": s["keyword"],
                "context": s["context"],
                "link_replacement": f'<a href="/{s["target_slug"]}/">{s["matched_text"]}</a>',
            }
            for s in suggestions
        ],
    }
    if args.include_skipped and skipped:
        report["skipped_samples"] = [
            {
                "source": s["source_dir"],
                "target": s["target_dir"],
                "keyword": s["keyword"],
                "context": s["context"],
                "skip_reason": s.get("skip_reason"),
            }
            for s in skipped[:40]
        ]

    output_path = args.output or root / "memory/blog/interlink-suggestions.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Saved suggestions report to {output_path.relative_to(root) if root in output_path.parents else output_path}")

    if args.apply and suggestions:
        applied = apply_interlinks(suggestions, articles)
        print(f"Successfully applied {applied} internal links across articles.")
    elif args.apply and not suggestions:
        print("Nothing to apply after quality filter.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
