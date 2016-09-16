import matplotlib.pyplot as plt

# def x(n):
#     if n == 0:
#         return 7.
#     else:
#         return x(n-1) - 1. / x(n-1)

y = [1.414]
for i in xrange(10000):
    y.append(y[-1] - 1. / y[-1])
# y = [x(n) for n in xrange(20)]

plt.plot(y, 'g-')
plt.show()
