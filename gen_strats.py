from player_utils import generate_strategies

strats = generate_strategies(10000, 3)
with open('random_strategies.txt', 'w') as f:
    for s in strats:
        f.write(s+'\n')
