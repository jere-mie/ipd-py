import random
import math

MEMORY_DEPTH = 3
CHROM_LENGTH = sum([4 ** i for i in range(MEMORY_DEPTH + 1)]) # Total chromosome length (based on the value of MEMORY_DEPTH).
INIT_LENGTH = 4 ** MEMORY_DEPTH + MEMORY_DEPTH # Initial chromosome length for setting the population (based on the value of MEMORY_DEPTH).

# Used to get values for the memory_key list.
def binary(num, length):
    val = "{0:b}".format(num) # Format the given number num as binary.
    while len(val) < length: val = '0' + val # Add any number of '0's to fill up the length specified.
    return val


memory_key = [binary(i, 2 * MEMORY_DEPTH) for i in range(2 ** (2 * MEMORY_DEPTH))] # List comprehension to get all possible cases.
points_key = {'11':(3, 3), '10':(0, 5), '01':(5, 0), '00':(1, 1)} # For determining points.

def generate_population(population_size, chrom_len):

    population = [] # List of all "people".
    chromosome = '' # Current chromosome.
    genes = ['0', '1'] # Possible value.

    for x in range(population_size):
        for y in range(chrom_len): chromosome += random.choice(genes)
        population.append(chromosome)
        chromosome = ''

    return population

def tournament(population, size):
    points = [0] * size
    
    for i in range(size):
        for j in range(i, size):
            memory_a = ''
            memory_b = ''
            
            # Parse each play. It must use a loop like this in order to be compatible with different memory depths.
            for k in range(MEMORY_DEPTH):
                memory_a += population[i][4 ** MEMORY_DEPTH + k] + population[j][4 ** MEMORY_DEPTH + k]
                memory_b += population[j][4 ** MEMORY_DEPTH + k] + population[i][4 ** MEMORY_DEPTH + k]
            
            # Unsure why this iterates 100 times like this. Thoughts?
            for k in range(100):
                move_a = population[i][memory_key.index(memory_a)] # Get the specific move of a.
                move_b = population[j][memory_key.index(memory_b)] # Get the specific move of b.
                outcome = points_key[move_a + move_b] # Get the number of points.
                points[i] += outcome[0]
                points[j] += outcome[1]
                memory_a = memory_a[2:] + move_a + move_b
                memory_b = memory_b[2:] + move_b + move_a
    return points

print(tournament(generate_population(10, INIT_LENGTH), 10))