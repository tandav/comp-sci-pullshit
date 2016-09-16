from numpy import *
import matplotlib.pyplot as plt
from math import *
from random import randint



a = [randint(-10, 10) for i in xrange(7)]

x = linspace(0, 10000, 10000)
y = [sin(c) for c in x]
 
plt.plot(x, y, 'k.')
plt.xscale('log')
plt.show()
