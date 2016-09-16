import numpy as np
from pylab import imshow, show
import matplotlib.pyplot as plt
from numpy import *

n = 1000
N = 100
t = linspace(0, N, n)

image = [[1 for b in t] for a in t]

for i, a in enumerate(t):
    for j, b in enumerate(t):
        delta = abs(a**b - b**a)
        if delta < 0.7:
            image[i][j] = delta

imshow(image, interpolation='none', cmap='gray')
plt.axis([0, 2*N, 0, 2*N])
show()