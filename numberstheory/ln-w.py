from numpy import *
import matplotlib.pyplot as plt
from math import *

def w(number):
    if len(str(number)) == 1:
        return number
    else:
        return w(sum([int(n) for n in [i for i in str(number)]]))


def wab(n):
	if n / 10 == 0:
		return n
	else:
		return w(int((n - int(n))*10**int(n)))

x = range(1,100)
y = [wab(log(i)) for i in x]
# u = [w(i) for i in primes]
# y = [r(i) for i in ln]
    
# # t = linspace(0, 150, 1000)
# # y = f(t, 1.02, 0.033, 0.7285)

plt.plot(x, y, 'g-')
plt.show()
