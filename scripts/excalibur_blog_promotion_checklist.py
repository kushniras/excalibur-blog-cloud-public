#!/usr/bin/env python3
"""Create promotion-checklist.md from template (create-if-missing by default).

Indexer must not overwrite curated checklists. Pass --force only when
intentionally regenerating from template.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_meta(article_dir: Path) -> dict:
    meta_path = article_dir / "article.meta.json"
    if not meta_path.is_file():
        return {}
    try:
        return json.loads(meta_path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def render_checklist(template: str, article_dir: Path, meta: dict) -> str:
    topic_id = meta.get("topic_id") or article_dir.name.split("-", 1)[0]
    slug = meta.get("slug") or ""
    title_line = f"# Promotion checklist — {topic_id} {slug}".rstrip()
    lines = template.splitlines()
    if lines and lines[0].startswith("# Promotion checklist"):
        lines[0] = title_line
    else:
        lines.insert(0, title_line)
    body = "\n".join(lines)
    return body + ("\n" if not body.endswith("\n") else "")


def ensure_checklist(
    article_dir: Path,
    template_path: Path,
    *,
    force: bool = False,
) -> str:
    """Return status: created | skipped_exists | overwritten | missing_template | missing_dir."""
    if not article_dir.is_dir():
        return "missing_dir"
    if not template_path.is_file():
        return "missing_template"

    out_path = article_dir / "promotion-checklist.md"
    existed = out_path.is_file()
    if existed and not force:
        return "skipped_exists"

    template = template_path.read_text(encoding="utf-8")
    meta = load_meta(article_dir)
    out_path.write_text(render_checklist(template, article_dir, meta), encoding="utf-8")
    return "overwritten" if existed else "created"


def iter_article_dirs(blog_dir: Path) -> list[Path]:
    if not blog_dir.is_dir():
        return []
    dirs = []
    for child in sorted(blog_dir.iterdir()):
        if child.is_dir() and (child / "article.html").is_file():
            dirs.append(child)
    return dirs


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Ensure promotion-checklist.md exists (create-if-missing; --force to overwrite)"
    )
    ap.add_argument("--article-dir", type=Path, default=None, help="Single article directory")
    ap.add_argument("--blog-dir", type=Path, default=None, help="All articles under this directory")
    ap.add_argument(
        "--template",
        type=Path,
        default=None,
        help="Template path (default: skills/excalibur/references/promotion-checklist-template.md)",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing promotion-checklist.md (DANGEROUS for curated files)",
    )
    args = ap.parse_args()

    root = project_root()
    template_path = args.template or (
        root / "skills/excalibur/references/promotion-checklist-template.md"
    )
    if not template_path.is_absolute():
        template_path = root / template_path

    if args.article_dir:
        article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
        targets = [article_dir]
    elif args.blog_dir:
        blog_dir = args.blog_dir if args.blog_dir.is_absolute() else root / args.blog_dir
        targets = iter_article_dirs(blog_dir)
    else:
        print("Provide --article-dir or --blog-dir")
        return 2

    counts = {
        "created": 0,
        "skipped_exists": 0,
        "overwritten": 0,
        "missing_dir": 0,
        "missing_template": 0,
    }
    for article_dir in targets:
        status = ensure_checklist(article_dir, template_path, force=args.force)
        counts[status] = counts.get(status, 0) + 1
        print(f"{status}: {article_dir.name}")

    if counts["missing_template"]:
        print(f"Template not found: {template_path}")
        return 1
    if counts["missing_dir"] and not (
        counts["created"] or counts["skipped_exists"] or counts["overwritten"]
    ):
        return 1

    print(
        "summary: "
        f"created={counts['created']} "
        f"skipped_exists={counts['skipped_exists']} "
        f"overwritten={counts['overwritten']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
