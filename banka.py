import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, factorial

def h(t, h0, k):
    return (sqrt(h0) - k*t/2)**2

def derivative(h0, k, n):
    if n == 0:
        return h0
    else:
        power = 0.5
        c = -k
        for i in xrange(1, n):
            c *= power
            power -= 1
        return c * h0**power


def hTaylor(t, h0, k, n):
    h = h0
    for i in xrange(1, n):
        h += derivative(h0, k, i) / factorial(i) * t**i
    return h

h0 = 6.
k = 0.6 * sqrt(2 * 9.8) / 576
t = np.linspace(0, 1100, 1000)
h = h(t, h0, k)
h2 = hTaylor(t, h0, k, 102)



plt.plot(t, h, 'k-')
plt.plot(t, h2, 'r-')
# plt.axis('equal')
plt.show()
