X = [i / 100. for i in xrange(1,100)]
Y = [1./x for x in X]
# for x in xrange(1,100):
#     print x, 1. / x
# y = [1. / x for x in xrange(1,100)]
print X
import matplotlib.pyplot as plt
plt.plot(Y)
# plt.axis('equal')
plt.show()