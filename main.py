# /// script
# dependencies = [
#   "PyPDF2",
#   "rich",
#   "python-slugify",
# ]
# ///

import sys
from PyPDF2 import PdfReader, PdfWriter
from rich import print
from slugify import slugify


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} recto.pdf verso.pdf", file=sys.stderr)
        sys.exit(1)

    recto_path = sys.argv[1]
    verso_path = sys.argv[2]

    try:
        recto_reader = PdfReader(recto_path)
        verso_reader = PdfReader(verso_path)
    except Exception as e:
        print(f"Error reading PDFs: {e}", file=sys.stderr)
        sys.exit(1)

    recto_count = len(recto_reader.pages)
    verso_count = len(verso_reader.pages)

    if recto_count != verso_count:
        print(
            f"Error: page count mismatch ({recto_count} != {verso_count})",
            file=sys.stderr,
        )
        sys.exit(1)

    output_path = (
        slugify(
            f"combined-{recto_path.rsplit('.', 1)[0]}-{verso_path.rsplit('.', 1)[0]}"
        )
        + ".pdf"
    )

    print(f"Merging {recto_count} recto and {verso_count} verso pages.")

    writer = PdfWriter()

    # verso file is scanned in reverse order
    verso_pages = list(reversed(verso_reader.pages))

    for r_page, v_page in zip(recto_reader.pages, verso_pages):
        writer.add_page(r_page)
        writer.add_page(v_page)

    with open(output_path, "wb") as out_f:
        writer.write(out_f)

    file_size = sys.getsizeof(out_f)

    print(f"Combined PDF written to [red]{output_path}[/red]")
    print(f"Total size: {file_size} KB and {len(writer.pages)} pages.")


if __name__ == "__main__":
    main()
