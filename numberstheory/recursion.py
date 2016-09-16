import matplotlib.pyplot as plt
from math import sqrt

def xi(n):
    if  n == 0:
        return 0
    else:
        xprev = xi(n - 1) 
        return (sqrt(xprev**2 + 4) + xprev) / 2


x = xrange(1,200)
y = [(xi(i) - xi(i - 1))**2 for i in x]
plt.plot(x, y, "o-")
# plt.axis('equal')
plt.show()