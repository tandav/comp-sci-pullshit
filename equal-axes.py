from math import *

import matplotlib.pyplot as plt

x = xrange(3)
y = [i*i for i in x]
plt.plot(x, y)
plt.axis('equal')
plt.show()