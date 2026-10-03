# EPUB edition

The finished guide is a single file named `togaf-hands-on-guide.epub`. It is
generated rather than committed because an EPUB is a binary ZIP archive, which
some pull-request tools cannot accept or review.

## Build it locally

From the repository root, run:

```bash
python3 scripts/build_epub.py
```

The command creates `epub/togaf-hands-on-guide.epub`. The builder uses only the
Python standard library, so it does not require package installation.

## Download it from GitHub Actions

1. Open the repository's **Actions** tab.
2. Select the latest successful **Build EPUB** run.
3. Download the `togaf-hands-on-guide` artifact.
4. Unzip the downloaded artifact to get the single EPUB file.

The workflow rebuilds the book for every pull request and push. This keeps the
downloadable copy aligned with the Markdown course without storing a binary in
Git.
