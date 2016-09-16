from numpy import *
import matplotlib.pyplot as plt
from math import *

x = linspace(0, 10, 200)
y = [sqrt(i) for i in x]
 
 
plt.plot(x, y, 'k-')
plt.grid(True)
plt.show()


