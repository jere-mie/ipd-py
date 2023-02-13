import random
from player_utils import *
from hill_climbing import generate_initial_strategy

MEMORY_DEPTH = 3
GENERATIONS = 100
ROUNDS = 100
STRAT_LENGTH = encoding_length(MEMORY_DEPTH) 
OPPONENT_SIZE = 30
PLAY_NEIGHBOURS = True
TABU_LENGTH = 10 # maximum tabu list length

BIT_FLIP = {'0': '1', '1': '0'}

def generate_neighbours(currentStrat: str) -> list[str]:
    """Generates neighbours based on the given current strategy."""
    
    # Turns the strat into a list so indices can be modified
    currentStratList = list(currentStrat)
    neighbours = []
    
    # Creates all the neighbours
    for c in range(len(currentStratList)):
        newStrat = currentStratList.copy()
        newStrat[c] = BIT_FLIP[newStrat[c]]
        neighbours.append("".join(newStrat))
        
    return neighbours

def tabu_run_generation(strategy: str, tabu_list: list[str]) -> list:
    """Runs a single generation.
    
    \nThe return values are as follows by index:
    \n0 - All of the strategy strings
    \n1 - The score of the current strategy being used
    \n2 - The highest scores from this generation"""
    
    # Compiles all strategies into one list
    allStrats = generate_neighbours(strategy)
    allStrats.append(strategy)
    stratScores = []
    
    if PLAY_NEIGHBOURS:
        # Grabs the strategy scores from the tournament played between neighbours
        stratScores = play_tournament(allStrats, ROUNDS)
    else:
        # Throws all neighbours and current strategy into randomized tournaments
        for strat in allStrats:
            randomStrats = generate_strategies(OPPONENT_SIZE, MEMORY_DEPTH)
            randomStrats.append(strat)
            
            randomTournamentScores = play_tournament(randomStrats, ROUNDS)
            stratScores.append(randomTournamentScores[-1])
            
    # Stores highest scores by fitness score, then index
    highestScores = [[-1, -1]]
    
    # Checks to see if a new local best strategy was discovered
    for index in range(len(stratScores)-1):
        score = stratScores[index]

        if allStrats[index] in tabu_list:
            continue
        if score < highestScores[0][0]:
            continue
        elif score > highestScores[0][0]:
            highestScores = [[score, index]]
        elif score == highestScores[0][0]:
            highestScores.append([score, index])
            
    return [allStrats, stratScores[-1], highestScores]

def tabu_prisoners_dilemma() -> list:
    """Runs a simulation of the prisoner's dilemma using a tabu
    search algorithm to determine the best possible strategy.
    Returns the top strategy along with its result in the last
    generation."""
    
    # Initialized with a randomized strategy and works with neighbours
    # in order to optimize results
    currentStrat = generate_initial_strategy()
    print(currentStrat)
    currentStratResult = 0
    tabu_list = []
    
    # Simulates all the generations
    for _ in range(GENERATIONS):
        genResults = tabu_run_generation(currentStrat, tabu_list)
        currentStratResult = genResults[1]
        newStrat = ""
        
        for stratResult in genResults[2]:
            if stratResult[0] >= currentStratResult:
                newStrat = genResults[0][stratResult[1]]
                currentStratResult = stratResult[0]
                break
                
        if len(newStrat) == 0:
            break

        tabu_list.append(newStrat)
        # max tabu list length - will need to be tuned based on generations/rounds
        if len(tabu_list) > TABU_LENGTH:
            tabu_list = tabu_list[1:]

        currentStrat = newStrat

    return [currentStrat, currentStratResult]

def __main__():
    results = tabu_prisoners_dilemma()
    print("TABU SEARCH")
    print("Optimized String: " + results[0])
    print("Cumulative Score: " + str(results[1]))



if __name__ == '__main__':   
    __main__()