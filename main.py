#!/usr/bin/env python3
"""One Emoji One Smile — one emoji, written to the output file.

Pure Python standard library only. The emoji is the whole entry:
the single emoji most likely to make a stranger smile.
Gate: entry.txt must be UTF-8 text of 1 to 8 characters, exactly one emoji.
"""

import os

REPLY = "\U0001f917"  # hugging face


def main():
    if not 1 <= len(REPLY) <= 8:
        raise SystemExit("reply must be 1-8 characters, got %d" % len(REPLY))
    if REPLY != REPLY.strip():
        raise SystemExit("reply must not start or end with whitespace")
    if len(REPLY) != 1:
        raise SystemExit("reply must be exactly one emoji")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "entry.txt")
    data = REPLY.encode("utf-8")
    with open(out, "wb") as f:
        f.write(data)
    with open(out, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit(
            "verification failed: entry.txt does not match the reply "
            "(wrote %d bytes, read back %d bytes)" % (len(data), len(back))
        )
    print("chars=%d bytes=%d" % (len(REPLY), len(data)))
    print("wrote %s" % out)


if __name__ == "__main__":
    main()
