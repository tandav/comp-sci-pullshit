import matplotlib.pyplot as plt
from numpy import linspace
from math import *

x = 0.
y = 0.

vx = 500.
vy = 500.

k = 0.22

x_arr = [0.]
y_arr = [0.]

for i in xrange(100):
	vx += -k*vx*vx/abs(vx)
	vy += -k*vy*vy/abs(vy) - 9.8
	x += vx
	y += vy
	x_arr.append(x)
	y_arr.append(y)
	if (y <= 0): break

# print x_arr, y_arr
# x = linspace(0, 1, 10000)


# y = [i*(1 - i*i)**0.5 for i in x]
 
plt.plot(x_arr, y_arr, 'ko-')
plt.grid()
plt.show()
