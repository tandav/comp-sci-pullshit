import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
from numpy import *
import sys

def p(t):
    return (sqrt(4*sqrt(2)*t + 1) - 1) / 2.

def M(t):
    return p(t) * (t*sqrt(2) - p(t) / 2. - p(t)**2 / 3.)

def s(t):
    return M(t) - t**2 / 2.
n = 1006000
x = linspace(0, sqrt(2), n)
y = s(x)
best = 0.
for i in y:
    if abs(i - 1./12) < abs(best - 1./12):
        best = i
print x[y == best], best
# plt.plot(x, y, 'g-')
# plt.show()