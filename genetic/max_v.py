import matplotlib.pyplot as plt
import itertools
from random import randint, choice

fuel = 6
l = 6

def v_friction(arr):
    v = 0
    for f in arr:
        friction = 0.3 * v # ~ v | ~ v^2
        v += f - friction
        if v < 0:
            v = 0
    return v
            
def newunit(fuel):
    unit = [0 for i in xrange(l)]
    while fuel > 0:
        unit[randint(0, l - 1)] += 1
        fuel -= 1
    return unit

def mutation(unit, level):
    mutant = unit
    for i in xrange(level):
        while True:
            j = randint(0, l - 1)
            if mutant[j] > 0:
                mutant[j] -= 1
                mutant[randint(0, l - 1)] += 1
                break
    return mutant

def worstUnitIndex(population):
    velocities = map(v_friction, population)
    return velocities.index(min(velocities))

def bestUnitIndex(population):
    velocities = map(v_friction, population)
    return velocities.index(max(velocities))

population = [newunit(fuel) for i in xrange(50)] # population size
v_best = v_friction(population[bestUnitIndex(population)])

for i in xrange(300000):
    unit_temp = newunit(fuel)
    v_temp = v_friction(unit_temp)
    if v_temp > v_best:
        v_best = v_temp
print v_friction(population[bestUnitIndex(population)])
plt.plot(population[bestUnitIndex(population)], 'go-')
plt.show()