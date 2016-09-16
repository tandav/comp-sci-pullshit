import matplotlib.pyplot as plt
from numpy import *
from math import *
x = linspace(-10, 10, 1000)

A = linspace(-1.0001,1.0001,4)

for a in A:
    y = ((1 - a)*x)**(1./(1 - a))
    plt.plot(x, y)
# plt.axis('equal')
# plt.yscale('log')
plt.show()