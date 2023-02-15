from player_utils import play_match
strategies = {
    "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000":["ALLD", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111":["ALLC", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0101010101010101010101010101010101010101010101010101010101010101010101010101010101011":["TFT", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0101111101011111010111110101111101011111010111110101111101011111010111110101111111111":["TF2T", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0101010101010101010101010101010101010101010101010101010101010101010101010101010101010":["STFT", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0011000000011011001001010000100010111111110110000001010100001111010010000111111010000":["GA_3", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0000110000010111001010011111010111010010000111001100010001010010000101110111100010011":["HC_PN_2", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1010100000000100011100011001011101010011001111110101110010010001100110111011101101000":["HC_SS_2", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1010000110011101001000110001001110011010000111100111001011011011001000101100001100000":["HC_DS_3", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1111001110111010101000110001000010101010100110011000010111001111011011000000101100011":["TS_PN_2", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1000001000100000000000010011010100000000000110000110011001101100110110111100111010110":["TS_SS_1", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1001101101010010110010011110000100001011100110000011100100011010001010101010101100110":["TS_DS_3", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0110110010001001100111011001000110110000101001010010101011110000001110001001101110100":["RAND", 0, [0, 0, 0], 0, [0, 0, 0]],
}

# constants to make indexing better in general
NAME = 0
TOTALSCORES = 1
WINSLOSSESTIES = 2
RANDOMTOTALSCORES = 3
RANDOMWINSLOSSESTIES = 4

# constants to make indexing better for wins/losses/ties
WIN = 0
LOSS = 1
TIE = 2

stratstrs = list(strategies.keys())

print("Player A,Player B,Player A Score,Player B Score")

for a in range(len(stratstrs)):
    for b in range(a+1, len(stratstrs)):
        a_score, b_score = play_match(stratstrs[a], stratstrs[b], 100)
        strategies[stratstrs[a]][TOTALSCORES]+=a_score
        strategies[stratstrs[b]][TOTALSCORES]+=b_score
        if a_score > b_score:
            strategies[stratstrs[a]][WINSLOSSESTIES][WIN]+=1
            strategies[stratstrs[b]][WINSLOSSESTIES][LOSS]+=1
        elif a_score < b_score:
            strategies[stratstrs[a]][WINSLOSSESTIES][LOSS]+=1
            strategies[stratstrs[b]][WINSLOSSESTIES][WIN]+=1
        else:
            strategies[stratstrs[a]][WINSLOSSESTIES][TIE]+=1
            strategies[stratstrs[b]][WINSLOSSESTIES][TIE]+=1
        print(f'{strategies[stratstrs[a]][NAME]},{strategies[stratstrs[b]][NAME]},{a_score},{b_score}')

print("\nStrategy,Total Score")

for strat in stratstrs:
    print(f'{strategies[strat][NAME]},{strategies[strat][TOTALSCORES]}')

print("\nStrategy,Wins,Losses,Ties")

for strat in stratstrs:
    print(f'{strategies[strat][NAME]},{strategies[strat][WINSLOSSESTIES][WIN]},{strategies[strat][WINSLOSSESTIES][LOSS]},{strategies[strat][WINSLOSSESTIES][TIE]}')

# comparing all strats against 10000 random strategies
with open('random_strategies.txt', 'r') as f:
    randstrats = [i.strip() for i in f.readlines()]

for strat in stratstrs:
    for rs in randstrats:
        score, r_score = play_match(strat, rs, 100)
        strategies[strat][RANDOMTOTALSCORES]+=score
        if score > r_score:
            strategies[strat][RANDOMWINSLOSSESTIES][WIN]+=1
        elif score < r_score:
            strategies[strat][RANDOMWINSLOSSESTIES][LOSS]+=1
        else:
            strategies[strat][RANDOMWINSLOSSESTIES][TIE]+=1

print('\nAgainst 10000 Random Opponents')
print('Strategy,Score,Wins,Losses,Ties')
for strat in stratstrs:
    print(f'{strategies[strat][NAME]},{strategies[strat][RANDOMTOTALSCORES]},{strategies[strat][RANDOMWINSLOSSESTIES][WIN]},{strategies[strat][RANDOMWINSLOSSESTIES][LOSS]},{strategies[strat][RANDOMWINSLOSSESTIES][TIE]}')
