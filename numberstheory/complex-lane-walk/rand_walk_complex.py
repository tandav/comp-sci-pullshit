import matplotlib.pyplot as plt
import numpy as np
from math import *
import cmath
from random import randint, random, uniform

def digitalSum(n):
    if n < 10 :
        return n
    return n % 10 + digitalSum( n // 10 )


N = 2000

z = np.zeros(N, dtype = complex)
z[0] = complex(0, 0)
z[1] = complex(1, 1)
# z[2] = complex(z[1] + z[1] - z[0])
# r = complex(1,1)

slider = np.linspace(1, pi, N)

for i in xrange(2, N):
	theta = sin(1/slider[i])
	# z[i] = (z[i-1] + (z[i-1] - z[i-2]))*cmath.exp(theta*1j)*(z)
	z[i] = z[i-1] + (z[i-1] - z[i-2])*cmath.exp(theta*1j)





plt.plot(z.real, z.imag, 'k-')
plt.axis('equal')
# plt.xlim(-2, 2)
# plt.ylim(-2, 2)
plt.axhline(0, color='blue')
plt.axvline(0, color='blue')

plt.grid()
plt.show()
