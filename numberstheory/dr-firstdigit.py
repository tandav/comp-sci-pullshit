import math
import matplotlib.pyplot as plt
def dr(n):
    res = n % 9
    if res == 0:
        return 9
    else:
        return res

def firstdigit(x):
    return int((x - int(x)) * 10)

# X = xrange(1000)
# Y = [dr(x * x) for x in X] 

X = xrange(2,100)
Y = [dr(x * x) for x in X]
plt.plot(X, Y, 'go-')



# Y1 = [dr(x**x) for x in X]
# plt.plot(X, Y1, 'ro-')
plt.show()