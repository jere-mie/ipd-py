import random
# a dict of pre-made strategy encodings
known_strategies = {
    "ALLD_1":"00000",
    "ALLD_2":"000000000000000000000",
    "ALLD_3":"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "ALLC_1":"11111",
    "ALLC_2":"111111111111111111111",
    "ALLC_3":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
    "TFT_1":"01011",
    "TFT_2":"010101010101010101011",
    "TFT_3":"0101010101010101010101010101010101010101010101010101010101010101010101010101010101011",
    # note: TF2T is not possible with memory depth 1
    "TF2T_2":"010111110101111111111",
    "TF2T_3":"0101111101011111010111110101111101011111010111110101111101011111010111110101111111111",
    "STFT_1":"01010",
    "STFT_2":"010101010101010101010",
    "STFT_3":"0101010101010101010101010101010101010101010101010101010101010101010101010101010101010"
}

# k-v pairs where the key is the encoding length and the value is the respective memory depth
memory_depths = {
    1:0,
    5:1,
    21:2,
    85:3,
    341:4,
    1365:5
}

def next_move(encoding: str, memory: str) -> str:
    # always return the last character when we have no memory
    if len(memory) == 0:
        return encoding[-1]

    # if we have less memory than our memorydepth, but greater than no memory,
    # we remove the main cases from the encoding to return a simpler encoding
    if len(memory)//2 < memory_depths[len(encoding)]:
        return next_move(encoding[-1*(len(encoding)//4):], memory)
    return encoding[int(memory, 2)]

def encoding_length(memoryDepth=1) -> int:
    encodingLength = 0
    for i in range(memoryDepth+1):
        encodingLength += 4**i
    return encodingLength

def generate_strategies(numOfStrats, memoryDepth=1) -> list:
    strategies = []
    encLength = encoding_length(memoryDepth)
    for _ in range(numOfStrats):
        strategies.append("".join([random.choice(['0', '1']) for __ in range(encLength)]))
        
    return strategies

def play_match(playera: str, playerb:str, rounds=1):
    pa_mem = ''
    pb_mem = ''
    pa_score = 0
    pb_score = 0
    return 'hello'

if __name__ == '__main__':
    print(next_move(known_strategies['TFT_2'], '0000'))
    print(next_move(known_strategies['TFT_2'], '00'))
    print(next_move(known_strategies['TFT_2'], '0001'))
    print(next_move(known_strategies['TFT_2'], '01'))
    print(next_move(known_strategies['TFT_2'], ''))
