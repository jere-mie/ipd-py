from player_utils import play_match
strategies = {
    "1011001100110101100110010111111100000000100110111100100001001011011001111100111010100":["GA_1", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0101100100010000110101010000000100000110010001110101101010100001101010010111111101111":["GA_2", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0011000000011011001001010000100010111111110110000001010100001111010010000111111010000":["GA_3", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1000000101101001001100001001011100101000001010100010010000010111001011100000100101010":["HC_DS_1", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0011000000001110011000111010010110000010000100011001101101111000100011000100000100110":["HC_DS_2", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1010000110011101001000110001001110011010000111100111001011011011001000101100001100000":["HC_DS_3", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0110111111000001100100000000110110110001011100100101111100011001001001110101100011011":["HC_PN_1", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0000110000010111001010011111010111010010000111001100010001010010000101110111100010011":["HC_PN_2", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1100010101010011000001011000110000101011001111011000101101101100111011110111010001011":["HC_PN_3", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1010000000001011000000110100110001100011011000110011000010010110001110111001000111011":["HC_SS_1", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1010100000000100011100011001011101010011001111110101110010010001100110111011101101000":["HC_SS_2", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1011000000000010010010100010001010000010110110000010000110000011010001010010001011110":["HC_SS_3", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0111000011011100100000000101100000111010001101111000111111000101111110110000111010011":["TS_DS_1", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0001001101011011001100101111111000011110010100001001011101010111001011110000110101010":["TS_DS_2", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1001101101010010110010011110000100001011100110000011100100011010001010101010101100110":["TS_DS_3", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1100101000100011100000000011100101010100001001111010000000000111001001101011000100101":["TS_PN_1", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1111001110111010101000110001000010101010100110011000010111001111011011000000101100011":["TS_PN_2", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0111100001000001001000100000011110100010100110011010101100110101010001000111001101000":["TS_PN_3", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1000001000100000000000010011010100000000000110000110011001101100110110111100111010110":["TS_SS_1", 0, [0, 0, 0], 0, [0, 0, 0]],
    "0010001100110000001100101010110011010010111010101000001100110111001010111000000000001":["TS_SS_2", 0, [0, 0, 0], 0, [0, 0, 0]],
    "1110100000000001101100010110000010010001111000110011000100101101110011011011000111001":["TS_SS_3", 0, [0, 0, 0], 0, [0, 0, 0]],
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
