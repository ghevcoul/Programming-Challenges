# Challenge #249 Intermediate - "Hello, World!" Genetic Algorithm
# https://www.reddit.com/r/dailyprogrammer/comments/40rs67/20160113_challenge_249_intermediate_hello_world/

import string
import random
import heapq

def initialize(length, size=10000):
    """Build the initial population of random strings of <length> with <size> members."""
    pop = []
    for i in range(size):
        pop.append(''.join([random.choice(string.printable) for j in range(length)]))
    return pop

def hamming_distance(s, target):
    """Return the Hamming distance between two input strings.
    Shamelessly taken from Wikipedia article on Hamming Distance."""
    if len(s) != len(target):
        raise ValueError("Strings must be same length.")
    return sum(bool(ord(c1) - ord(c2)) for c1, c2 in zip(s, target))

def selection(pop, target):
    """Select the fittest genotypes from population."""
    h = []
    for i in pop:
        heapq.heappush(h, (hamming_distance(i, target), i))
    parents = [i[1] for i in heapq.nsmallest(100, h)]
    # Seed parents with a few random strings
    for i in range(int(0.05 * len(parents))):
        parents.append(''.join([random.choice(string.printable) for j in range(len(parents[0]))]))
    return parents

def make_babies(parents, size=10000):
    """Create a new population by randomly selecting two parents and
    randomly selecting the character from a parent for each position."""
    children = []
    for i in range(size):
        p1, p2 = random.sample(parents, 2)
        children.append(''.join([p1[i] if random.randint(0,1) else p2[i] for i in range(len(p1))]))
    return children

def optimize_to_target(target):
    # Run genetic algorithm
    population = initialize(len(target))

    for i in range(100):
        fittest = selection(population, target)
        print("Gen: {} | {}".format(i, fittest[0]))
        if hamming_distance(fittest[0], target) == 0:
            break
        population = make_babies(fittest)

if __name__ == "__main__":
    t = "Hello, world!"
    #t = "To be or not to be, that is the question."
    optimize_to_target(t)