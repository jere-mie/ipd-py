# Strategy Encodings

Strategy encodings are done via bit strings, whereby 0 represents defect and 1 represents cooperate.

## Memory Depth 1

Encodings are of length 5 (the first 4 are for the 4 different cases, the last 1 is for the initial move).
Cases:
- 00 (player 1 defects, player 2 defects)
- 01 (player 1 defects, player 2 cooperates)
- 10 (player 1 cooperates, player 2 defects)
- 11 (player 1 cooperates, player 2 cooperates)

### Strategies

- ALLD: `00000`
- ALLC: `11111`
- TFT: `01011`

