# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

m = [ [10.5, 10.5, 7, 22, 18, 3, 32, 35, 5],
      [10.5, 10.5, 7, 20, 16, 2, 33, 23, 5],
      [10.5, 10.5, 7, 17, 13, 2, 23, 22, 4],
      [10.5, 10.5, 7, 19, 14, 2, 23, 22, 4],
      [10.5, 10.5, 7, 18, 15, 2, 23, 22, 4],
      [10.5, 10.5, 6, 18, 16, 2, 22, 22, 3],
      [10.5, 10.5, 7, 22, 14, 2, 23, 25, 4],
      [10.5, 10.5, 8, 23, 17, 4, 24, 28, 5],
      [10.5, 10.5, 9, 25, 15, 3, 24, 31, 5],
      [10.5, 10.5, 9, 25, 15, 4, 24, 88, 5],
      [10.5, 10.5, 10, 24, 25, 3, 36, 85, 7],
      [10.4, 10.4, 10, 24, 26, 3, 36, 88, 7],
      [10.5, 10.5, 10, 26, 30, 3, 40, 93, 5],
      [10.5, 10.5, 12, 24, 27, 4, 36, 90, 5],
      [10.4, 10.5, 9, 25, 27, 3, 38, 93, 5],
      [10.3, 10.3, 9, 26, 30, 3, 40, 92, 6],
      [10.3, 10.4, 10, 29, 24, 4, 42, 93, 8],
      [10.3, 10.4, 10, 28, 25, 4, 48, 94, 7],
      [10.4, 10.4, 11, 36, 31, 5, 51, 94, 7],
      [10.4, 10.4, 12, 35, 26, 5, 59, 92, 8],
      [10.4, 10.4, 13, 37, 30, 5, 60, 92, 7],
      [10.4, 10.5, 12, 37, 27, 5, 58, 90, 10],
      [10.4, 10.5, 11, 30, 21, 5, 49, 61, 9],
      [10.5, 10.5, 11, 25, 19, 4, 40, 33, 7] ]

csfont = {'fontname':'Arial'}

# plt.title('111title',**csfont)

p = np.array([[m[i][0] * (0.9*m[i][2] + 0.7*m[i][3] + 0.9*m[i][4] + 0.9*m[i][8]) + m[i][1] * (0.9*m[i][5] + 0.7*m[i][6] + 0.9*m[i][7])] for i in xrange(24)])
s = np.array([[m[i][0] * (m[i][2] + m[i][3] + m[i][4] + m[i][8]) + m[i][1] * (m[i][5] + m[i][6] + m[i][7])] for i in xrange(24)])
q = (s**2 - p**2)**0.5
t = np.arange(1, len(p)+1)
mean = sum(p) / 24.
meansq = (sum(p**2) / 24.)**0.5
mx = max(p)
# plt.plot(t, p, 'go-', t, q, 'ro-')
width = .75

ax = plt.axes()      
# ax.axhline(mean, color='k',label= "123",  linewidth=1, linestyle='--')
# ax.axhline(meansq, color='k',label= "123",  linewidth=1, linestyle='--')

ax.yaxis.grid() #vertical lines
# plt.bar(t - 1, p, color='cornflowerblue')
plt.bar(t - 1, q, color='lightcoral')
ax = plt.gca()


# ax.axhline(mean, color='k', linewidth=1, linestyle='--')
# plt.rc('font', family='sans-serif')
plt.xticks(t - 1 + width / 2, t, **csfont)
plt.yticks(np.arange(0, 2500, 250), **csfont)
ax.xaxis.set_label_coords(1, -0.025)
ax.yaxis.set_label_coords(-0.05, 1)


# ax.yaxis.set_label_coords(1.05, -0.025)
# plt.grid()
# plt.show()
plt.savefig("17_r.png")
