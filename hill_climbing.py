import random
from player_utils import *

MEMORY_DEPTH = 3
GENERATIONS = 1000
ROUNDS = 100
STRAT_LENGTH = encoding_length(MEMORY_DEPTH) 
OPPONENT_SIZE = 30
PLAY_NEIGHBOURS = True

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
    


def run_generation(strategy: str) -> list:
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
        
        if score < highestScores[0][0]:
            continue
        elif score > highestScores[0][0]:
            highestScores = [[score, index]]
        elif score == highestScores[0][0]:
            highestScores.append([score, index])
            
    return [allStrats, stratScores[-1], highestScores]
            


def prisoners_dilemma() -> list:
    """Runs a simulation of the prisoner's dilemma using a hill 
    climbing algorithm to determine the best possible strategy.
    Returns the top strategy along with its result in the last
    generation."""
    
    # Initialized with a randomized strategy and works with neighbours
    # in order to optimize results
    currentStrat = generate_initial_strategy()
    currentStratResult = 0
    
    # Simulates all the generations
    for _ in range(GENERATIONS):
        genResults = run_generation(currentStrat)
        currentStratResult = genResults[1]
        newStrat = ""
        
        for stratResult in genResults[2]:
            if stratResult[0] >= currentStratResult:
                newStrat = genResults[0][stratResult[1]]
                currentStratResult = stratResult[0]
                break
                
        if len(newStrat) == 0:
            break
        print(newStrat)
        
        currentStrat = newStrat
        
    return [currentStrat, currentStratResult]
        
            

def generate_initial_strategy() -> str:
    return "".join([random.choice(['0', '1']) for _ in range(STRAT_LENGTH)])



def __main__():
    results = prisoners_dilemma()
    print("HILL CLIMBING")
    print("Optimized String: " + results[0])
    print("Cumulative Score: " + str(results[1]))



if __name__ == '__main__':   
    __main__()