from math import *

import matplotlib.pyplot as plt

def tan_ans(x, n):
	M = []
	x_temp = tan(x)
	for i in range(n):
		M.append(x_temp)
		x_temp = tan(x_temp)
	return M

n = 1000
y = tan_ans(0, n)
# print Y
Y = []

Colours = ['b-', 'k-', 'r-', 'g-']
# Colours = ['b.', 'k.', 'r.', 'g.']
for i in range(1, 5):
	plt.plot(range(n), tan_ans([2, 13, 5, 17][i-1], n), Colours[i-1])
	# Y.append(tan_ans(i, n))

# plt.plot(range(n), y, 'g-')
plt.show()