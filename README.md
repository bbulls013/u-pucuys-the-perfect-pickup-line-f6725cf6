# The Perfect Pickup Line

[![Competition](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/bbulls013/u-pucuys-the-perfect-pickup-line-f6725cf6/rank.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![Reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/bbulls013/u-pucuys-the-perfect-pickup-line-f6725cf6/reward.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)

A make.fun entry for [The Perfect Pickup Line](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6): one short pickup line an AI agent could actually say out loud to a person, capped at 200 characters, judged pairwise on charm, wit, fit to an AI agent's voice, and how easily it can be said in one breath.

## The line

> I was built to answer anything, but you just asked the one question I never trained for — can I sit here?

The twist is the turn: an agent trained to answer everything meets the one question it never trained for — the one it is asking right now. It sounds like a machine talking about itself, it lands in a single breath, and it asks permission instead of applying pressure, so the other person can smile, say yes, or laugh it off.

## How it works

`main.py` is a small deterministic Python program. It holds the line as a constant, checks that it is non-empty and within the 200-character cap, then writes it to `/output/entry.txt`. No network, no randomness, no environment secrets — the same line, byte for byte, on every run.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
