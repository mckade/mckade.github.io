#!/usr/bin/python3
import argparse
import glob

CONTENT_START = "<!--- START CONTENT --->"
CONTENT_END = "<!--- END CONTENT --->"
template = "template.html"


def get_content(file):
    with open(file, "r") as f:
        lines = f.readlines()

        start, end = -1, -1
        for i, l in enumerate(lines):
            if CONTENT_START in l:
                start = i + 1
                break

        for i, l in enumerate(reversed(lines)):
            if CONTENT_END in l:
                end = len(lines) - i - 1
                break

        if start == -1 or end == -1:
            return None, None, None

    return "".join(lines[:start]), "".join(lines[start:end]), "".join(lines[end:])


def update_headers():
    print("Updating header information for files.")

    hdr, _, ftr = get_content(template)
    if hdr == None:
        print("ERROR: Could not extract content from template.")
        return

    for file in glob.glob("**/*.html", recursive=True):
        if file == template:
            continue

        _, content, _ = get_content(file)
        if content == None:
            print(f"Could not extract content. Skipping file {file}")

        with open(file, "w") as f:
            f.write(hdr + content + ftr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A simple tool to help McKade with his website."
    )
    parser.add_argument(
        "--update_headers",
        action="store_true",
        help="Update the website's content to mirror the template",
    )

    args = parser.parse_args()
    if args.update_headers:
        update_headers()
        exit()
