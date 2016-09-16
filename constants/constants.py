# -*- coding: utf-8 -*-
#================================= DATA IMPORT =================================

pi = open("pi.txt", 'r')

letters = 0

for line in pi:
    1

PI = []
for i in range(len(line)):
    PI.append(int(line[i]))

pi.close()

e = open("e.txt", 'r')
letters = 0

for line in e:
    1

E = []
for i in range(len(line)):
    E.append(int(line[i]))
    
e.close()

phi = open("phi.txt", 'r')
letters = 0

for line in phi:
    1

PHI = []
for i in range(len(line)):
    PHI.append(int(line[i]))

phi.close()

#================================= PROCESSING ==================================
#print(len(PI))
MATCHES = []
X_AXIS = []
for i in range(100):    #1000001
    if PI[i] == E[i] or E[i] == PHI[i] or PI[i] == PHI[i]:
        X_AXIS.append(i)
        MATCHES.append(i)

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.size'] = '12.0'
mpl.rcParams['font.sans-serif'] = 'Arial'
plt.plot(MATCHES,'gh-', label = "$i(n)$")
plt.xlabel('$n = 1, 2, 3...$')    # обозначение оси абсцисс
plt.ylabel(u'$i$, Индекс совпадения цифры в трех константах $\pi,e,\phi$')
plt.title(u'Возрастание индекса совпадений от $n \int \mu(n)dn$')  # название графика
plt.legend(loc = 4)
plt.show()