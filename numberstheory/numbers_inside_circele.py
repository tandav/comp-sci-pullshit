from math import sqrt

def dr(n):
    res = n % 9
    if res == 0:
        return 9
    else:
        return res


m = 0
M = []
for r in xrange(1,500):
    for i in xrange(r):
        for j in xrange(r):
            if sqrt(i**2 + j**2) <= r:
                m += 1
    M.append(m)
    m = 0
# print M

drs = [dr(x) for x in M]
print drs

import matplotlib.pyplot as plt
plt.plot(drs, 'go')
plt.show()

