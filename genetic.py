import random
import math
from player_utils import *

MEMORY_DEPTH = 3
POPULATION_SIZE = 86
GENERATIONS = 1000
ROUNDS = 100
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.001
CHROM_LENGTH = sum([4 ** i for i in range(MEMORY_DEPTH + 1)]) # Total chromosome length (based on the value of MEMORY_DEPTH).
INIT_LENGTH = 4 ** MEMORY_DEPTH + MEMORY_DEPTH # Initial chromosome length for setting the population (based on the value of MEMORY_DEPTH).

def binary(num, length):
    """Used to get values for the memory_key list."""
    
    val = "{0:b}".format(num) # Format the given number num as binary.
    while len(val) < length: val = '0' + val # Add any number of '0's to fill up the length specified.
    return val

memory_key = [binary(i, 2 * MEMORY_DEPTH) for i in range(2 ** (2 * MEMORY_DEPTH))] # List comprehension to get all possible cases.



def generate_population(population_size, chrom_len):

    population = [] # List of all "people".
    chromosome = '' # Current chromosome.
    genes = ['0', '1'] # Possible value.

    for x in range(population_size):
        for y in range(chrom_len): chromosome += random.choice(genes)
        population.append(chromosome)
        chromosome = ''
    
    return population



def tournament(population):
    size = len(population)
    points = [0] * size
    
    for i in range(size):
        for j in range(i + 1, size):
            memory_a = ''
            memory_b = ''
            
            # Parse each play. It must use a loop like this in order to be compatible with different memory depths.
            for k in range(MEMORY_DEPTH):
                memory_a += population[i][4 ** MEMORY_DEPTH + k] + population[j][4 ** MEMORY_DEPTH + k]
                memory_b += population[j][4 ** MEMORY_DEPTH + k] + population[i][4 ** MEMORY_DEPTH + k]
            
            # Unsure why this iterates 100 times like this. Thoughts?
            for k in range(ROUNDS):
                move_a = population[i][memory_key.index(memory_a)] # Get the specific move of a.
                move_b = population[j][memory_key.index(memory_b)] # Get the specific move of b.
                outcome = points_key[move_a + move_b] # Get the number of points.
                points[i] += outcome[0]
                points[j] += outcome[1]
                memory_a = memory_a[2:] + move_a + move_b
                memory_b = memory_b[2:] + move_b + move_a
    return points



# Get the fitness.
# The fitness formula squares each result to make the differences more extreme.
# Then the average fitness is appended at the end of the list for comparison's sake.
def get_fitness(points, size):
    
    fitness = points
    average_fitness = sum(fitness) / size
    fitness.append(average_fitness)

    return fitness



# Generate a new population using the Roulette-Wheel sampling method.
def new_population(population, fitness, crossover_rate, mutation_rate):
    
    length = len(population)
    fitness_range = [0] * (length + 1)
    new_pop = []
    parent1 = ''
    parent2 = ''
    child1 = ''
    child2 = ''
    mutated1 = ''
    mutated2 = ''

    for i in range(length): fitness_range[i + 1] = fitness_range[i] + fitness[i]

    for i in range(int(math.ceil(float(length)/2))):

        spin_1 = random.uniform(0, fitness_range[length]) # Get random number between 0 and the corresponding average fitness range.
        for j in range(length):
            if fitness_range[j] <= spin_1 <= fitness_range[j + 1]:
                parent1, parent2 = population[j], population[j]
                break

        while parent1 == parent2:
            spin_2 = random.uniform(0, fitness_range[length]) # Get another random number between 0 and the corresponding average fitness range.
            for j in range(length):
                if fitness_range[j] <= spin_2 <= fitness_range[j + 1]:
                    parent2 = population[j]
                    break

        # Determine if a crossover should take place.
        if random.uniform(0, 1) < crossover_rate:
            crossover_position = random.randrange(INIT_LENGTH + MEMORY_DEPTH) # Get a number for crossing over the "dna" for the future children.
            child1 = parent1[:crossover_position] + parent2[crossover_position:]
            child2 = parent2[:crossover_position] + parent1[crossover_position:]
        else:
            child1 = parent1
            child2 = parent2

        # Determine if mutation takes place for each offspring.
        for a, b in zip(child1, child2):

            if random.uniform(0, 1) < mutation_rate:
                # Swap the bit value due to mutation.
                if a == '1': mutated1 += '0'
                else: mutated1 += '1'
            else: mutated1 += a # Don't swap because mutation doesn't occur here.

            if random.uniform(0, 1) < mutation_rate:
                # Swap the bit value due to mutation.
                if b == '1': mutated2 += '0'
                else: mutated2 += '1'
            else: mutated2 += b # Don't swap because mutation doesn't occur here.
            
        new_pop.append(mutated1)
        new_pop.append(mutated2)

        parent1, parent2 = '', ''
        mutated1, mutated2 = '', ''
        
    # Pop any random member of the population for an odd population length.
    if length % 2 != 0: new_pop.pop(random.randrange(len(new_pop)))
    return new_pop



def prisoners_dilemma(pop_size, num_generations, num_runs, crossover_rate, mutation_rate):
    
    points = [0] * pop_size
    fitness = [0] * pop_size
    population = []
    generations = []
        
    # This is the run for the first generation.
    population = generate_population(pop_size, CHROM_LENGTH) # Get the initial population.
    points = play_tournament(population, ROUNDS) # Run the tournament.
    fitness = get_fitness(points, pop_size) # Get the fitness. This is used to determine who can carry on to the next generation.
    temp = zip(population, fitness) # Creates a list that iterates through the population and fitness together, effectively giving each "person" their fitness.
    generations.append(list(temp)) # Append to generations.
    #generations[0].append(fitness[-1]) # Append the average fitness to the first generation.
    
    # Now we use a loop for the next generations (necessary for creating the new population).
    for g in range(1, num_generations):
        population = new_population(population, fitness, crossover_rate, mutation_rate) # Generate new population.
        points = play_tournament(population, ROUNDS) # Run the tournament.
        fitness = get_fitness(points, pop_size) # Get the fitness.
        temp = zip(population, fitness) # New list of each person and their corresponding fitness level.
        generations.append(list(temp))
        #generations[g].append(fitness[-1]) # Append the average fitness to the corresponding generation.

    #runs.append(generations) # Appends the generations.
    #generations = []

    return generations



if __name__ == '__main__':
    results = prisoners_dilemma(POPULATION_SIZE, GENERATIONS, 1, CROSSOVER_RATE, MUTATION_RATE) # Run the Prisoner's Dilemma!
    lastgen = results[-1] # Get the last generation.
    lastgen.sort(key=lambda x: x[1], reverse=True) # Sort it by fitness/score level in decreasing order.

    # Output the results of the tournament, namely the last generation.
    for i in range(len(lastgen)):
        print(f"Player {i + 1}: {list(lastgen[i])[0]} Fitness: {list(lastgen[i])[1]}")