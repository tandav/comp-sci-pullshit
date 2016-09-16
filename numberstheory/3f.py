from math import *
import matplotlib.pyplot as plt

from numpy import *
def f1(x):
    return 2*x

def f2(x):
    return x

def F(x, y):
    return 2*sin(x)*cos(y*y)

x = linspace(-10, 10, 1000)
y = F(f1(f2(x)), f2(f1(x)))


plt.plot(x, y,'g-')
# plt.axis('equal')
plt.show()
