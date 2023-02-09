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

def next_move(encoding: str, memory: str) -> str:
    return encoding[int(memory, 2)]

if __name__ == '__main__':
    print(next_move(known_strategies['ALLD_1'], '00'))
    print(next_move(known_strategies['ALLD_1'], '01'))
    print(next_move(known_strategies['ALLC_1'], '00'))
    print(next_move(known_strategies['ALLC_1'], '01'))
    print(next_move(known_strategies['TFT_1'], '00'))
    print(next_move(known_strategies['TFT_1'], '01'))
