from math import tan, sin
from random import randint, choice
import pickle

MIN_VALUE = 0
MAX_VALUE = 4
LENGTH = 7
POPULATION_SIZE = 500
FIRSTTIME = True

def fitness(arr):
    fit = 0
    for i in xrange(LENGTH):
        fit += arr[i] * (arr[i - 1] + arr[(i + 1) % LENGTH])
    return fit

def newunit():
    return [choice(xrange(MIN_VALUE, MAX_VALUE + 1)) for i in xrange(LENGTH)]

def crossover(unit1, unit2):
    crosspoint = randint(1, LENGTH - 1)
    return unit1[:crosspoint] + unit2[crosspoint:]

def mutate(unit, level=1):
    for i in xrange(level):
        unit[randint(0, LENGTH - 1)] = randint(MIN_VALUE, MAX_VALUE)
    return unit

def bestunit(population):
    fitarray = [fitness(unit) for unit in population]
    maxfitindex = fitarray.index(max(fitarray))
    return population[maxfitindex], fitarray[maxfitindex]

def evolution(population, steps):
    maxfit = max([fitness(unit) for unit in population])
    for i in xrange(steps):
        fitarray = [fitness(unit) for unit in population]
        # maxfitindex = fitarray.index(max(fitarray))
        minfitindex = fitarray.index(min(fitarray))
        newunit = crossover(population[randint(0, POPULATION_SIZE - 1)], population[randint(0, POPULATION_SIZE - 1)])
        newunit = mutate(newunit)
        newunitfit = fitness(newunit)
        if newunitfit > fitarray[minfitindex]:
            population[minfitindex] = newunit
            if newunitfit > maxfit:
                maxfit = newunitfit
                print newunit, newunitfit
    with open('population.txt', 'wb') as f:
        pickle.dump(population, f)
    return population

if FIRSTTIME:
    population = [newunit() for i in xrange(POPULATION_SIZE)]
else:
    with open('population.txt', 'rb') as f:
        population = pickle.load(f)

evolution(population, 10000)
print bestunit(population)
