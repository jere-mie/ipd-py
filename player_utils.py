import random
#random.seed(6)
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

# For determining points.
points_key = {
    '00': [1, 1],
    '01': [5, 0], 
    '10': [0, 5], 
    '11': [3, 3]
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



def encoding_length(memoryDepth: int=1) -> int:
    """Determines the encoding length of a given memory depth."""

    encodingLength = 0
    for i in range(memoryDepth+1):
        encodingLength += 4**i
    return encodingLength



def generate_strategies(numOfStrats: int, memoryDepth: int=1) -> list[str]:
    """Generates a given amount of unique strategies."""

    strategies = []
    encLength = encoding_length(memoryDepth)

    # Handles if the # of strategies requested are greater than 
    # all possible combinations of the encoded string
    if numOfStrats > 2 ** encLength:
        raise Exception("Too many strategies!")
        
    # Generates strategies with guarantee of no duplication
    for _ in range(numOfStrats):
        #random.seed(6)
        strat = "".join([random.choice(['0', '1']) for __ in range(encLength)])

        while strat in strategies:
            #random.seed(6)
            strat = "".join([random.choice(['0', '1']) for __ in range(encLength)])

        strategies.append(strat)

    return strategies



def play_match(playerA: str, playerB: str, rounds: int=1) -> list[int]:
    """Plays a match between two strategies."""

    pAMem = ""
    pBMem = ""
    pAScore = 0
    pBScore = 0

    # This variable figures out how much of the mem string to keep track of
    totalRoundAmount = memory_depths[len(playerA)] * 2

    for _ in range(rounds):
        pANextMove = next_move(playerA, pAMem[-1*(totalRoundAmount):])
        pBNextMove = next_move(playerB, pBMem[-1*(totalRoundAmount):])

        pAMem += pANextMove + pBNextMove
        pBMem += pBNextMove + pANextMove

        roundScores = points_key[pANextMove + pBNextMove]
        pAScore += roundScores[0]
        pBScore += roundScores[1]

    return [pAScore, pBScore]



def play_tournament(strategies: list[str], rounds: int=1) -> list[int]:
    """Plays a tournament where all players play against
    one another with a provided number of rounds. The strategy score
    is the score with the coinciding index within the returning list."""

    # Defines # of strategies and sets all strategy scores to 0
    numOfStrats = len(strategies)
    strategyScores = [0 for _ in range(numOfStrats)]

    for p1Num in range(numOfStrats):
        for p2Num in range(p1Num+1, numOfStrats):
            # This is where the match is played
            matchScores = play_match(strategies[p1Num], strategies[p2Num], rounds)
            strategyScores[p1Num] += matchScores[0]
            strategyScores[p2Num] += matchScores[1]

    return strategyScores



if __name__ == '__main__':
    strats = [
        '1001000010110100110101110110011110011110100011011011010100100100111001010100010001010',
        '0111001110011101110010001000011000010000011101011001001111010011111101010001101101001'
    ]
    print(strats)
    print(play_tournament(strategies=strats, rounds=100))

    # print(next_move(known_strategies['TFT_2'], '0000'))
    # print(next_move(known_strategies['TFT_2'], '00'))
    # print(next_move(known_strategies['TFT_2'], '0001'))
    # print(next_move(known_strategies['TFT_2'], '01'))
    # print(next_move(known_strategies['TFT_2'], ''))
