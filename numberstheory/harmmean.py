import matplotlib.pyplot as plt
from numpy import *
from math import log

def harm(a, b):
    if a + b == 0:
        return 0
    else:
        return 2. * a * b / (a + b)
x = []
y = []
H = []

r0 = -1000
r1 = 1000

for a in xrange(r0, r1):
    for b in xrange(r0, a):
        if a != b:
            h = harm(a, b)
            if h != 0 and h - int(h) == 0:
                x.append(a)
                y.append(b)
                H.append(h)
                # print a, b, h


# plt.plot(x, y)
plt.plot(x, H)

# plt.yscale('log')
# plt.axis('equal')
plt.show()