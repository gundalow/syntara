"""MkDocs hook: rewrite edit URLs for symlinked docs to point to the real path."""

import os
import re
from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page


def on_page_markdown(
    markdown: str,
    *,
    page: Page,
    config: MkDocsConfig,
    files: Files,
) -> str:
    src_path = Path(page.file.abs_src_path)
    real_path = os.path.realpath(src_path)

    if real_path != os.path.abspath(src_path):
        repo_root = os.path.dirname(config["docs_dir"])
        real_rel = os.path.relpath(real_path, repo_root)
        repo_url = config.get("repo_url", "").rstrip("/")
        edit_uri = config.get("edit_uri", "")
        if repo_url and edit_uri:
            if match := re.match(r"(edit/[^/]+/)", edit_uri):
                edit_prefix = match.group(1)
            else:
                edit_prefix = "edit/devel/"
            page.edit_url = f"{repo_url}/{edit_prefix}{real_rel}"

    return markdown
