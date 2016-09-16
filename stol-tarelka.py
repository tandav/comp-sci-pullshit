import matplotlib.pyplot as plt
from numpy import linspace
from math import *

n = 8
angles = [2*pi/n*i for i in xrange(n)]

x = map(lambda x: cos(x), angles)
y = map(lambda x: sin(x), angles)
# x = [pi*i for ]
# print x_arr, y_arr
# x = linspace(0, 1, 10000)


 
plt.plot(x, y, 'ko-')
plt.grid()
plt.axis('equal')
plt.show()
