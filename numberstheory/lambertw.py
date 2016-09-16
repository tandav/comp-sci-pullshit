import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from math import log

X = linspace(0.001, 10, 10000)
Y = [-x * log(-log(x)/x) / log(x) for x in X]

plt.plot(X, Y,'g-')
plt.axis('equal')
plt.show()
# print lambertw(-1.3).real