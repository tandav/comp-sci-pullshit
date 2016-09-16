"""
TODO:

1. Run for a night
2. Determine why s_best is descending sometimes

GA - ne goditsyas
"""
L=10
TP = 'm'
POPN = 50
FirstTime = True

import random
import pickle
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import animation


dt = 1./30 # 30 fps
arbj = [0 for i in xrange(L)]

def s(FD):
    """Returns distanse that vehicle
       ride by its force distribution array
    """
    s = 0
    v = 0

    for f in FD:
        if v == 0:
            if abs(f) < 0.5: # Ftr pokoya
                continue
            Ftr = 0
        else:
            Ftr = -(0.3*v**2 + 1)

        v += f + Ftr
        if v < 0:
            v = 0
        s += v

    while v > 0: # doletaet
        Ftr = -(0.3*v**2 + 1)
        v += Ftr
        if v < 0:
            v = 0
        s += v
    return s

def mutate(unit, percentage = 0.2, mut_radius=0.05):
    FD = [i for i in unit] # !!!
    flag1 = True
    flag2 = True
    flag3 = True
    zp0 = sum(FD) # zapas topliva 
    while flag1 and flag2 and flag3:
        elem_indexes_to_mutate = random.sample(xrange(len(FD)), int(percentage * len(FD)))
        
        for i in elem_indexes_to_mutate:
            dm = random.uniform(-mut_radius, mut_radius)
            if FD[i] + dm > 0:
                FD[i] += dm
                flag1 = False

        l = (zp0 - sum(FD)) / (len(FD) - len(elem_indexes_to_mutate))
        
        for i in xrange(len(FD)):
            if not i in elem_indexes_to_mutate:
                if FD[i] + l > 0:
                    FD[i] += l
                    flag2 = False
        if sum(FD) == zp0:
            flag3 = False
        else:
            flag1 = True
            flag2 = True

    return FD # mb void ?? #mb 0.04 accuracy

def crossover(F1, F2):
    crosspoint = random.randint(0, len(F1)-1)
    child = [F1[i] for i in xrange(crosspoint)]

    for i in xrange(crosspoint, len(F1)):
        child.append(F2[i])

    gain = sum(F1) - sum(child)
    l = gain/len(child)

    for i in xrange(len(child)):
        child[i] += l
    return child

def jiva_init(l, zapas):
    jiva = [float(zapas) / l for i in xrange(l)]
    for x in xrange(5):
        jiva = mutate(jiva)
    return jiva
    
def best_jiv(population):
    s_arr = [s(j) for j in population]
    jiva_best = population[s_arr.index(max(s_arr))]
    return jiva_best

if FirstTime:
    population = [jiva_init(L,10) for i in xrange(POPN)] # for the first time (not from file, generating new random population)
else:
    with open('population_db.txt', 'rb') as f:
        population = pickle.load(f)


def evolution_step(ev_type='mc'):
    # global population
    if ev_type == 'mc' or 'cm':
        s_arr = [s(jv) for jv in population]
        min_s_index = s_arr.index(min(s_arr))
        new_jiv = crossover(population[random.randint(0, len(population)-1)], population[random.randint(0, len(population)-1)])
        new_jiv = mutate(new_jiv)
        if s(new_jiv) > s_arr[min_s_index]:
            population[min_s_index] = new_jiv
    elif ev_type == 'm':
        s_arr = [s(jv) for jv in population]
        min_s_index = s_arr.index(min(s_arr))
        new_jiv = mutate(population[random.randint(0, len(population)-1)])
        if s(new_jiv) > s_arr[min_s_index]:
            population[min_s_index] = new_jiv
    elif ev_type == 'c':
        s_arr = [s(jv) for jv in population]
        min_s_index = s_arr.index(min(s_arr))
        new_jiv = crossover(population[random.randint(0, len(population)-1)], population[random.randint(0, len(population)-1)])
        if s(new_jiv) > s_arr[min_s_index]:
            population[min_s_index] = new_jiv
    with open('population_db.txt', 'wb') as f:
        pickle.dump(population, f)
    ax.relim()                      # reset intern limits of the current axes 
    ax.autoscale_view()   # reset axes limits 

def best_jiv_2D(population):
    s_arr = [s(j) for j in population]
    y = population[s_arr.index(max(s_arr))]
    return (xrange(len(y)), y)


fig = plt.figure()
# ax = plt.axes(xlim=(0, 19), ylim=(0, 2))
ax = plt.axes(xlim=(0, L-1))
line, = ax.plot([], [],'go-', lw=2)
s_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
sum_text = ax.text(0.25, 0.95, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    s_text.set_text('')
    return line, s_text

def animate(i):
    global arbj
    evolution_step(TP)
    line.set_data(best_jiv_2D(population))
    s_text.set_text('s = %f' % s(best_jiv(population)))
    sum_text.set_text('sum(FD(i)) = %.f' % sum(best_jiv(population)))
    if arbj != best_jiv(population):
        arbj = best_jiv(population)
        for i in arbj:
            print round(i, 4), '\t',
        print '...'
    return line, s_text, sum_text


# choose the interval based on dt and the time to animate one step
from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1000 * dt - (t1 - t0)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=300, interval=interval, blit=True)
plt.show()

