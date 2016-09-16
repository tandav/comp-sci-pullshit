# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


m = [ [10.5, 10.5, 4.5, 4, 25, 2, 22, 24, 3],
      [10.5, 10.5, 3, 4, 20, 3, 10, 22, 3],
      [10.5, 10.5, 3, 5, 12, 0, 10, 24, 3],
      [10.5, 10.5, 3, 5, 12, 0, 10, 15, 3],
      [10.5, 10.5, 3, 5, 12, 0, 10, 10, 3],
      [10.5, 10.5, 3, 5, 12, 0, 10, 10, 3],
      [10.5, 10.5, 4, 5, 12, 0, 10, 15, 3],
      [10.5, 10.5, 4, 18, 10, 3, 25, 25, 3],
      [10.3, 10.3, 5, 24, 12, 3, 25, 30, 4.8],
      [10.3, 10.3, 6, 30, 17, 3, 25, 50, 3],
      [10.3, 10.3, 7, 24, 27, 3, 30, 75, 3],
      [10.3, 10.3, 5, 18, 37, 3, 32, 87, 3],
      [10.3, 10.3, 4.2, 23, 36, 3, 35, 86, 3],
      [10.3, 10.3, 4.8, 22, 40, 3, 34, 86, 4.8],
      [10.1, 10.2, 4.8, 23, 36, 3, 30, 85, 4.8],
      [10.3, 10.3, 6, 19, 37, 3, 30, 85, 5.4],
      [10.3, 10.3, 4.2, 18, 40, 3, 32, 88, 4.2],
      [10.3, 10.3, 6.6, 23, 36, 3, 32, 88, 4.2],
      [10.3, 10.3, 6.5, 23, 34, 3, 33, 85, 4.2],
      [10.4, 10.4, 6, 24, 33, 3, 34, 81, 4.2],
      [10.4, 10.4, 6, 24, 32, 3, 36, 80, 4.2],
      [10.4, 10.4, 6.6, 26, 32, 3, 42, 83, 4.2],
      [10.4, 10.4, 6, 28, 30, 4.8, 60, 76, 4.2],
      [10.3, 10.3, 6, 30, 21, 4.2, 42, 38, 4.2] ]
# csfont = {'fontname':'Arial'}


p = np.array([[m[i][0] * (0.9*m[i][2] + 0.7*m[i][3] + 0.9*m[i][4] + 0.9*m[i][8]) + m[i][1] * (0.9*m[i][5] + 0.7*m[i][6] + 0.9*m[i][7])] for i in xrange(24)])
s = np.array([[m[i][0] * (m[i][2] + m[i][3] + m[i][4] + m[i][8]) + m[i][1] * (m[i][5] + m[i][6] + m[i][7])] for i in xrange(24)])
q = (s**2 - p**2)**0.5
t = np.arange(1, len(p)+1)
mean = sum(p) / 24.
meansq = (sum(p**2) / 24.)**0.5
mx = max(p)
# plt.plot(t, p, 'go-', t, q, 'ro-')
# plt.rc('text', usetex=True)
# plt.rc('font', family='sans-serif')
width = .75
ax = plt.axes()      
# ax.axhline(mean, color='k',label= "123",  linewidth=1, linestyle='--')
# ax.axhline(meansq, color='k',label= "123",  linewidth=1, linestyle='--')

ax.yaxis.grid() #vertical lines
plt.bar(t - 1, p, color='cornflowerblue')
# plt.bar(t - 1, q, color='lightcoral')
ax = plt.gca()


# ax.axhline(mean, color='k', linewidth=1, linestyle='--')
# Pср = 1427,106
plt.xticks(t - 1 + width / 2, t, **csfont)
plt.yticks(np.arange(0, 2500, 250), **csfont)
# plt.xlabel(u't, ч')2
ax.xaxis.set_label_coords(1, -0.025)
# plt.ylabel(u'P, кВт', rotation = 'horizontal')
ax.yaxis.set_label_coords(-0.05, 1)


# ax.yaxis.set_label_coords(1.05, -0.025)
# plt.grid()
plt.show()
# plt.savefig("gure.svg")
# plt.savefig("18_a.png")