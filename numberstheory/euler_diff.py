import matplotlib.pyplot as plt
from numpy import linspace
from math import *

def f(x, y):
    return cos(x) / sin(x)

x = [0]
y = [1]
h = 0.1

for i in xrange(7000):
    x.append(x[-1] + h)
    y.append(y[-1] + h * f(x[-1], y[-1]))

plt.plot(x, y, 'k-')
plt.grid()
plt.show()