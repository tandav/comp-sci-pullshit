from math import sqrt

def aproxim(x):
    best = [1., 1.]
    for a in xrange(1,10):
        for b in xrange(1,10):
            if abs(float(a)/b - x) < abs(float(best[0]) / best[1] - x):
                best[0] = a
                best[1] = b
    return best

bst = aproxim(1.14)
print bst, float(bst[0]) / bst[1]

# import matplotlib.pyplot as plt
# plt.plot(drs, 'go')
# plt.show()

