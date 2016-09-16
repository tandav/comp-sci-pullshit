from numpy import *
from itertools import cycle
import matplotlib.pyplot as plt


def vedic(n):
    V = [1]
    steps = [1, -1, 1]
    step = cycle(steps) # LOOP
    for i in range(n - 1):
        V.append(V[-1] + next(step))
    return V

def w(number):
    if len(str(number)) == 1:
        return number
    else:
        return w(sum([int(n) for n in [i for i in str(number)]]))

N = 30
# y = [sum(vedic(i)) / float(vedic(i)[i - 1]) for i in range(1, N + 1)]
# print y, vedic

W = [w(sum(vedic(i))) for i in range(1, N + 1)]
print W
plt.plot(range(N), W, 'g-')
plt.show()

# in future: play with w-function