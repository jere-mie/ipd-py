# Strategy Encodings

Strategy encodings are done via bit strings, whereby 0 represents defect and 1 represents cooperate.

## Memory Depth 1

Encodings are of length 5 (the first 4 are for the 4 different cases, the last 1 is for the initial move).  
Cases:
- 00 (player 1 defects, player 2 defects)
- 01 (player 1 defects, player 2 cooperates)
- 10 (player 1 cooperates, player 2 defects)
- 11 (player 1 cooperates, player 2 cooperates)

### Strategy Encodings

- ALLD: `00000`
- ALLC: `11111`
- TFT:: `01011` (TFT always cooperates in first move)
- TF2T: `.....` (not possible with memory depth 1)
- STFT: `01010` (STFT always defects on first move)

## Memory Depth 2

Encodings are of length 21 (the first 16 are for the 16 different cases, the next 4 are for the second move, the last 1 is for the initial move).  
Cases:
- 0000
- 0001
- 0010
- 0011
- 0100
- 0101
- 0110
- 0111
- 1000
- 1001
- 1010
- 1011
- 1100
- 1101
- 1110
- 1111

### Strategy Encodings

- ALLD: `000000000000000000000`
- ALLC: `111111111111111111111`
- TFT:: `010101010101010101011` (TFT always cooperates in first move)
- TF2T: `010111110101111111111` (TF2T always cooperates for the first two moves)
- STFT: `010101010101010101010` (STFT always defects on first move)

## Memory Depth 3

Encodings are of length 85 (the first 64 are for the 64 different cases, the next 16 are for the third move, the next 4 are for the second move, the last 1 is for the initial move).

Note: It should be clear the pattern of the different 'cases', so for brevity they can be excluded.

### Strategy Encodings

- ALLD: `0000000000000000000000000000000000000000000000000000000000000000000000000000000000000`
- ALLC: `1111111111111111111111111111111111111111111111111111111111111111111111111111111111111`
- TFT:: `0101010101010101010101010101010101010101010101010101010101010101010101010101010101011` (TFT always cooperates in first move)
- TF2T: `0101111101011111010111110101111101011111010111110101111101011111010111110101111111111` (TF2T always cooperates for the first two moves)
- STFT: `0101010101010101010101010101010101010101010101010101010101010101010101010101010101010` (STFT always defects on first move)
