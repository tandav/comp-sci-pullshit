import matplotlib.pyplot as plt
# import numpy as np
from numpy import *
from math import log

x = linspace(-0.001, 0.001, 1000)
powers = linspace(-1, 1.1, 10)

Y = [x**a for a in powers]
print powers
for y in Y:
    plt.plot(y)

# plt.yscale('log')
# plt.axis('equal')
plt.show()