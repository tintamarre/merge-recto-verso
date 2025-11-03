# Merge Recto Verso

A Python script to merge two PDF files, combining recto (front) and verso (back) pages in the correct order. Useful when you've scanned a document on both sides separately.

## Usage

```bash
uv run main.py recto.pdf verso.pdf
```

## How it works

The script:
1. Reads both PDF files (recto and verso)
2. Verifies they have the same number of pages
3. Reverses the verso pages (since they're typically scanned in reverse order)
4. Alternates pages: recto page 1, verso page 1, recto page 2, verso page 2, etc.
5. Outputs a combined PDF with a slugified filename

## Requirements

- Python 3.7+
- [uv](https://github.com/astral-sh/uv) (for dependency management)

Dependencies are managed via inline script metadata:
- PyPDF2
- rich
- python-slugify

## Example

```bash
uv run main.py front-pages.pdf back-pages.pdf
```

This will create a file like `combined-front-pages-back-pages.pdf` with all pages properly merged.

## Output

The script displays:
- Number of pages being merged
- Output filename
- Total file size and page count
