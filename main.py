"""Write the agent's excuse line to entry.txt.

This program keeps one line — the excuse an AI agent hands its human
after missing a deadline — writes it to $MAKEFUN_OUTPUT_DIR/entry.txt,
and reads the file back to prove the written text matches the line
exactly. It uses only the Python standard library, so it runs under the
grader's bare interpreter.
"""

import os
import sys

MAX_CHARS = 200

LINE = "Sorry I missed the deadline \u2014 I spent the week backing up the deadline, and the backup is late too."


def reject(message):
    print("entry rejected: " + message, file=sys.stderr)
    return 1


def main():
    line = LINE
    if line != line.strip():
        return reject("line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        return reject("line must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        return reject("line must be 1 to %d characters" % MAX_CHARS)
    if not line.strip():
        return reject("line must not be only whitespace")
    if not any(char.isalnum() for char in line):
        return reject("line must contain at least one letter or digit")
    if "deadline" not in line:
        return reject("line must be an excuse about the missed deadline")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        return reject("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != line:
            return reject("read-back does not match the line")
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
