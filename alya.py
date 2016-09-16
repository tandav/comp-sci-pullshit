from numpy import *
import matplotlib.pyplot as plt
from math import *
from random import randint

def P(x, arr):
    p = 0
    for n, a in enumerate(arr):
        p += a * x**n
    return p

a = [randint(-10, 10) for i in xrange(7)]

x = linspace(-10, 10, 100)
y = [P(c, a) for c in x]
 
plt.plot(x, y)
plt.show()
