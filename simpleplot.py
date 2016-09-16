import matplotlib.pyplot as plt
from numpy import linspace
from math import *

x = linspace(0, 1, 10000)
y = [i*(1 - i*i)**0.5 for i in x]
 
plt.plot(x, y)
plt.grid()
plt.show()
