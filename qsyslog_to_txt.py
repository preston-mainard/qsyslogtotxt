#!/usr/bin/env python3
"""
qsyslog_to_txt.py

Converts Q-SYS .qsyslog files (gzip-compressed tar archives) into
a single readable .txt file by extracting and concatenating all text
content from the archive.

Usage:
    python qsyslog_to_txt.py <input.qsyslog> [output.txt]

If no output path is given, the output file is created alongside the
input with a .txt extension.
"""

import sys
import os
import tarfile
from pathlib import Path


def convert(input_path, output_path=None):
    if output_path is None:
        output_path = Path(input_path).with_suffix(".txt")

    lines = []

    with tarfile.open(input_path, "r:gz") as tar:
        for member in sorted(tar.getmembers(), key=lambda m: m.name):
            if not member.isfile():
                continue

            f = tar.extractfile(member)
            if f is None:
                continue

            try:
                content = f.read().decode("utf-8", errors="replace").rstrip("\n")
            except Exception:
                continue

            lines.append(f"--- {member.name} ---")
            lines.append(content)
            lines.append("")

    output_text = "\n".join(lines) + "\n"

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(output_text)

    line_count = output_text.count("\n")
    print(f"Converted: {input_path}")
    print(f"Output:    {output_path} ({line_count} lines)")


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input.qsyslog> [output.txt]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.isfile(input_path):
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    convert(input_path, output_path)


if __name__ == "__main__":
    main()
