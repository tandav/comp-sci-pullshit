from math import floor, ceil, log
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 110)
# print x
x = xrange(1,100)
# y = [floor(log(ceil(i))) - ceil(log(floor(i))) for i in x]
y = [floor(log(ceil(i))) for i in x]
# print y
plt.plot(x, y)
# plt.axis('equal')
plt.show()