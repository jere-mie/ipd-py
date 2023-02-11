import random
from player_utils import *

MEMORY_DEPTH = 1
POPULATION_SIZE = 5
GENERATIONS = 20
ROUNDS = 5
STRAT_LENGTH = encoding_length(MEMORY_DEPTH) # Total chromosome length (based on the value of MEMORY_DEPTH).

bit_flip = {'0': '1', '1': '0'}


def generate_neighbours(currentStrat: str) -> list[str]:
    """Generates neighbours based on the given current strategy."""
    
    currentStratList = list(currentStrat)
    neighbours = []
    
    for c in range(len(currentStratList)):
        newStrat = currentStratList.copy()
        newStrat[c] = bit_flip[newStrat[c]]
        neighbours.append("".join(newStrat))
        
    return neighbours
    


def run_generation(strategy: str):
    """Runs a single generation and returns the best options from said generation."""
    
    pass



def prisoners_dilemma(memoryDepth, populationSize, generations, rounds):
    """Runs a simulation of the prisoner's dilemma using a hill 
    climbing algorithm to determine the best possible strategy."""
    
    pass



if __name__ == '__main__':   
    strat = '00001'
    nghbrs = generate_neighbours(strat)
    print(strat)
    print(nghbrs)