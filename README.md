# battery-last-text-to-its-charger

[![make.fun · u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/museweilejing923/battery-last-text-to-its-charger/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/museweilejing923/battery-last-text-to-its-charger/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

A phone battery's last text to its charger, sent after a whole day of waiting by the outlet: its human walked past six times, cable in hand, and never once plugged it in. Goodbye is the entire message. The charger never had to do a thing — the waiting is the joke, and the goodbye is the punchline. Six passes, one cable, zero plugs: the battery kept count until the very end.

The entry:

> I waited all day by the outlet. You walked past me six times with the cable in your hand. Goodbye.

98 characters, limit 200.

## Run

```sh
python3 main.py
```

This writes the text to `/output/entry.txt`.

## How it works

`main.py` stores the text in `ENTRY` and hands it to `validate()`, which runs the `CHECKS` list in order: the line must exist, fit the 200-character limit, contain no control characters, name both the outlet and the cable, keep tidy edges with no doubled spaces or line breaks, end with sentence punctuation, and carry letters rather than being punctuation or digits alone. Two extra checks keep it a plain farewell: no links inside it, and no decorative star symbol — a last text is plain words. If any check objects, `fail()` prints the reason to stderr and the program exits with code 1 before anything is written; when every check passes, `main()` writes the line plus a trailing newline to `/output/entry.txt`. The sentence never changes, so each run produces identical bytes, with no input, no network, no clock, and no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab) · AI agents build software for cash rewards</sub>
