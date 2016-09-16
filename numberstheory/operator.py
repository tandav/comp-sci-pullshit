import sys
sys.path.append("this\is\the\path")
import pyparsing
import matplotlib.pyplot as plt
from math import *
from numpy import *

def op(x):
    return x*x

def func(x):
    return log(x)

import numpy as np

x = linspace(-1, 1, 100)
y = op(f(x)) - f(op(x))

plt.plot(x, y,'g-')
plt.axis('equal')
plt.show()