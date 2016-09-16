import matplotlib.pyplot as plt
from math import e
import numpy as np
from numpy import *

def delta(x, b):
    return abs(x**(b/x) - (b/x)**x)

n = 5000 # t size
B = linspace(0.1, 20, n) # 20 -> ~
X = linspace(.1, 10, 100)

delta_avg = []
for x in X:
    delta_avg.append(delta(x, abs(x**(e+1/(x-e)) - (e+1/(x-e))**x)))
plt.plot(delta_avg,'g-')
plt.show()