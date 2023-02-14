import random
from player_utils import *
from hill_climbing import generate_initial_strategy
import time

MEMORY_DEPTH = 2
GENERATIONS = 1000
ROUNDS = 100
STRAT_LENGTH = encoding_length(MEMORY_DEPTH) 
OPPONENT_SIZE = 30
PLAY_NEIGHBOURS = False
SAME_STRANGERS = False
TABU_LENGTH = 100 # maximum tabu list length

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
    randomStrats = []

    if SAME_STRANGERS and PLAY_NEIGHBOURS:
        raise Exception("Cannot play same strangers and also play neighbours")
    else:
        randomStrats = generate_strategies(OPPONENT_SIZE, MEMORY_DEPTH)
        randomStrats.append(strategy)
    
    if PLAY_NEIGHBOURS:
        # Grabs the strategy scores from the tournament played between neighbours
        stratScores = play_tournament(allStrats, ROUNDS)
    else:
        # Throws all neighbours and current strategy into randomized tournaments
        for strat in allStrats:
            if not SAME_STRANGERS:
                randomStrats = generate_strategies(OPPONENT_SIZE, MEMORY_DEPTH)
            else:
                randomStrats.pop()

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
        elif score < highestScores[0][0]:
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
    currentStrat = generate_initial_strategy(STRAT_LENGTH)
    currentStratResult = 0
    tabu_list = []
    
    # Simulates all the generations
    for gen in range(GENERATIONS):
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

        print(f"Gen {gen+1}: " + newStrat + f" Score: {currentStratResult}")
        currentStrat = newStrat

    return [currentStrat, currentStratResult]

def __main__():
    t0 = time.time()
    results = tabu_prisoners_dilemma()
    t1 = time.time()
    timeTook = t1 - t0
    print("TABU SEARCH")
    print("Optimized String: " + results[0])
    print("Cumulative Score: " + str(results[1]))
    print(f"Time took: {timeTook} seconds ({timeTook/60} minutes)")

if __name__ == '__main__':   
    __main__()