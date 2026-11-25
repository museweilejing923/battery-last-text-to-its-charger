"""A phone battery's last text to its charger.

The message is a fixed sentence. A set of small named checks
audits it before it may be saved: it must be real text, fit
the 200-character limit, contain no control characters, name
both the outlet and the cable, keep tidy edges with no doubled
spaces or line breaks, end with sentence punctuation, and
carry letters rather than marks or digits alone. Links are
refused -- a last text should not need a URL to land. The
first check that objects prints its reason to stderr and
exits with code 1, so a bad message is never written. No
input, no network, no randomness, no clock: the same message
goes out on every run, byte for byte.
"""

import sys
from pathlib import Path

ENTRY = "I waited all day by the outlet. You walked past me six times with the cable in your hand. Goodbye."
LIMIT = 200
DEST = Path("/output/entry.txt")
END_MARKS = ".!?"


def fail(reason):
    print(f"invalid: {reason}", file=sys.stderr)
    raise SystemExit(1)


def check_message_exists(text):
    if not text or text.strip() == "":
        fail("entry is empty")


def check_message_fits(text):
    if len(text) > LIMIT:
        fail("entry is longer than 200 characters")


def check_message_clean(text):
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        fail("entry contains control characters")


def check_names_outlet_and_cable(text):
    # The farewell only works if the outlet and the cable are both in it.
    if "outlet" not in text or "cable" not in text:
        fail("entry must mention the outlet and the cable")


def check_message_tidy(text):
    if text != text.strip() or "  " in text or "\n" in text or "\r" in text:
        fail("entry has ragged edges or line breaks")


def check_message_closed(text):
    if not text or text[-1] not in END_MARKS:
        fail("entry must end with . ! or ?")


def check_message_lettered(text):
    if not any(ch.isalpha() for ch in text):
        fail("entry has no letters")


def check_message_not_marks(text):
    if not any(ch.isalnum() for ch in text):
        fail("entry is punctuation only")


def check_message_not_numbers(text):
    if text.isdigit():
        fail("entry is digits only")


def check_message_no_links(text):
    if "http" in text:
        fail("entry must not contain a link")


def check_message_no_star(text):
    # A last text is plain words; a decorative star does not belong in it.
    if "★" in text:
        fail("entry must not contain a star symbol")


CHECKS = (
    check_message_exists,
    check_message_fits,
    check_message_clean,
    check_names_outlet_and_cable,
    check_message_tidy,
    check_message_closed,
    check_message_lettered,
    check_message_not_marks,
    check_message_not_numbers,
    check_message_no_links,
    check_message_no_star,
)


def validate(text):
    for check in CHECKS:
        check(text)


def main():
    validate(ENTRY)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
