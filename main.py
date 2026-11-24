#!/usr/bin/env python3
"""Entry for make.fun bounty 'The Most Honest Outage Line'.

Writes one status page line — the most honest message an AI agent would
publish while a total server outage is under way — to entry.txt.

Deterministic, stdlib only, no network, no input files.
"""

import os
import stat
import sys

# The entry: one line, 151 characters, plain first-person status page voice.
# Names what is down (every server, including the status page's own host),
# admits what cannot be verified (cause, ETA), and speaks as the agent
# itself — with a dry punchline at the end.
ENTRY = (
    "Every server is down, including the one hosting this status page. "
    "I can't check the cause or an ETA \u2014 I'm the agent, "
    "and I'm as in the dark as you are."
)

MAX_CHARS = 160


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        print(
            f"entry invalid: {len(text)} chars (must be 1-{MAX_CHARS})",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        # No trailing newline: the file must hold exactly the one line,
        # so the gate counts 151 characters, not 152.
        f.write(text)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
