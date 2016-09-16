import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import uniform, randint
from math import *
fig = plt.figure()
t = 0
N = 100
arr = np.zeros((N, N))
def nakal(ar):
    ar_prev = ar
    h = arr.shape[0]
    w = arr.shape[1]
    for i in range(1, h - 2):
        for j in range(1, w - 2):
            # if arr[i][j] != 0.:
                # ar[i][j] = 0.9 * ar_prev[i][j] + 0.1 * (ar_prev[i-1][j-1] + ar_prev[i-1][j] + ar_prev[i-1][j+1] + ar_prev[i][j-1] + ar_prev[i][j+1] + ar_prev[i+1][j-1] + ar_prev[i+1][j] + ar_prev[i+1][j+1]) / 8.
                ar[i][j] = 0.8 * ar_prev[i][j] + 0.2 * (ar_prev[i-1][j-1] + ar_prev[i-1][j] + ar_prev[i-1][j+1] + ar_prev[i][j-1] + ar_prev[i][j+1] + ar_prev[i+1][j-1] + ar_prev[i+1][j] + ar_prev[i+1][j+1]) / 8.
    global t
    t += 1
    if t > 100:
        for i in range(1, h):
            ar[i][0] = uniform(200., 1000.)
            # ar[i][0] = -1.*abs(sum([ar[j][1] for j in range(1, h)]) / (h - 2.))
    for i in range(1, h):
        ar[i][-1] = -1.*abs(sum([ar[j][-2] for j in range(1, h)]) / (h - 2.))
    for i in range(1, w):
        ar[0][i] = -1.*abs(sum([ar[1][j] for j in range(1, w)]) / (w - 2.))
    for i in range(1, w):
        ar[-1][i] = -1.*abs(sum([ar[-2][j] for j in range(1, w)]) / (w - 2.))
    arr[10][80] = 1020 # constant temp
    return ar

def circle(x, y, r, temperature):
    global arr
    for i in range(x - r, x + r):
        for j in range(y - r, y + r):
            if (i - x)**2 + (j - y)**2 <= r*r:
                arr[i][j] = temperature


for i in range(1, arr.shape[0] - 1):
    arr[i][0] = 200.

for i in range(1, arr.shape[0] - 1):
    arr[i][-2] = -200.


for x in xrange(1000):
    circle(randint(10, 90), randint(10, 90), 6, uniform(-200, 200))
circle(50,73,22, 200.)
circle(20,23,12, -210.)
circle(65,23,22, -210.)
circle(25,83,12, 200.)
circle(15,2,22, -210.)
circle(65,23,22, -210.)
circle(75,23,13, 210.)


im = plt.imshow(arr, interpolation='nearest', cmap=plt.get_cmap('coolwarm'))
def updatefig(*args):
    global arr
    arr = nakal(arr)
    im.set_data(arr)
    # return im,

ani = animation.FuncAnimation(fig, updatefig, interval=1, blit=False)
plt.show()
