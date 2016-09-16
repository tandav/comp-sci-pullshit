from random import randint, choice, shuffle

FirstTime = True
# must_have = [2, 2, 2, 2, 2, 4, 3]
must_have = [1, 2, 3, 5,17 , 7, 7, 11, 13, 17, 19, 23,29]
factory_l = 29
population_size = 40

for x in must_have:
    if x > factory_l:
        print 'EROOR'
        break

def waste(unit):
    summa = 0
    wst = 0
    for el in unit:
        if summa + el > factory_l:
            wst += factory_l - summa
            summa = 0
        summa += el
    return wst + factory_l - summa

# def initunit(mh):
#     new = mh
#     shuffle(new)
#     return new


def crossover(unit1, unit2):
    crosspoint = randint(1, len(unit1) - 1)
    return unit1[:crosspoint] + unit2[crosspoint:]

def mutate(unit):
    i = randint(0, len(unit) - 1)
    j = randint(0, len(unit) - 1)
    unit[i], unit[j] = unit[j], unit[i]

def evolution_process(population, generations):
    # for i in xrange(generations):
    worst = max(waste(population))
    return worst
        # new_unit = crossover_1point(random.choice(population), random.choice(population))
        # new_unit = mutation(new_unit)
        # if waste(new_unit) < waste(worst):
        #     worst = new_unit


# mutate(must_have)



for x in xrange(10):
    print waste(must_have), must_have
    shuffle(must_have)






# print evolution_process(df, 2)



# population1 = [unit_init(must_have) for i in xrange(population_size)]

# print population1
# print crossover_1point(must_have, population1[1])

# if FirstTime:
#     population = [unit_init(must_have) for i in xrange(population_size)]
# else:
#     with open('population_db.txt', 'rb') as f:
#         population = pickle.load(f)