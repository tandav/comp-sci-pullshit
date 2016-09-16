import matplotlib.pyplot as plt
import numpy as np
from math import *
import cmath
from random import randint

x = [0, 1]
y = [0, 1]




# for i in xrange(1000):
# 	n = randint(0, 99)
# 	dx = x[-1] - x[-2]
# 	dy = y[-1] - y[-2]
# 	if n < 50:
# 		x.append(x[-1] - dy) # anti-clocwise
# 		y.append(y[-1] + dx)
# 	else:
# 		x.append(x[-1] + dy) # clockwise
# 		y.append(y[-1] - dx)


l = np.linspace(1, 3, 200000)
for i in l:
	r = sin(i)
	n = randint(0, 99)
	dx = np.sign(x[-1] - x[-2]) * r
	dy = np.sign(y[-1] - y[-2]) * r
	if n < 50:
		x.append(x[-1] - dy)
		y.append(y[-1] + dx)
	else:
		x.append(x[-1] + dy)
		y.append(y[-1] - dx)








plt.plot(x, y, 'k-')
plt.axis('equal')
plt.grid()
plt.show()
