import matplotlib.pyplot as plt
import itertools
from random import randint, choice

# Global Constants
MAX_SPEED = 1
POPULATION_SIZE = 10
TANK = 12 #Firstly: TANK = LENGTH
LENGTH = 24

def sWithFriction(arr):
    s = v = 0
    for f in arr:
        friction = 0.3 * v
        v += f - friction
        if v < 0:
            v = 0
        s += v

    while v > 0.01: # doletaet
        friction = 0.3 * v
        v -= friction
        if v < 0:
            v = 0
        s += v
    return s
    
def sNoFriction(arr):
    v = s = 0
    for a in arr:
        v += a
        s += v
    return s

def newUnit(tank, length):
    unit = [0 for i in xrange(length)]
    while tank > 0:
        randIndex = randint(0, length - 1)
        if unit[randIndex] < MAX_SPEED:
            unit[randIndex] += 1
            tank -= 1
    return unit

def crossover(unit1, unit2):
    for i in xrange(2):
        crosspoint = randint(1, len(unit1)-1)
        child = unit1[:crosspoint] + unit2[crosspoint:]
        if sum(child) == sum(unit1):
            return child
    return unit1

def mutation(unit, level):
    mutant = unit
    for i in xrange(level):
        while True:
            j = randint(0, len(unit)-1)
            if mutant[j] < MAX_SPEED:
                mutant[j] += 1
                break
        while True:
            j = randint(0, len(unit)-1)
            if mutant[j] > 0:
                mutant[j] -= 1
                break
    return mutant

def worstUnitIndex(population):
    minIndex = 0
    sMin = sWithFriction(population[0])
    for i in xrange(len(population)):
        sTemp = sWithFriction(population[i])
        if sTemp < sMin:
            minIndex = i
            sMin = sTemp
    return minIndex

def bestUnitIndex(population):
    maxIndex = 0
    sMax = sWithFriction(population[0])
    for i in xrange(len(population)):
        sTemp = sWithFriction(population[i])
        if sTemp > sMax:
            maxIndex = i
            sMax = sTemp
    return maxIndex


bestS = 0
bestUnit = []
for i in xrange(100000):
    unit_temp = newUnit(TANK, LENGTH)
    if sWithFriction(unit_temp) > bestS:
        bestS = sWithFriction(unit_temp)
        bestUnit = unit_temp
        # print bestUnit
print bestUnit, bestS


plt.plot(xrange(LENGTH), bestUnit, 'go-')
plt.show()