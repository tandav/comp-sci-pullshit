import numpy as np
from pylab import imshow, show

def binadd(a, b):
    if a == b:
        return 0
    else:
        return 1

def binom(n, k):
    if n < k:
        print "error"
        return
    if n == k or k == 0:
        return 1
    else:
        return binadd(binom(n - 1, k - 1), binom(n - 1, k))

n = 100
image = np.ones((n, n), dtype = np.uint8)

for i in xrange(n):
    for j in xrange(i + 1):
        # image[i][j] = image[i - 1][j - 1] + image[i - 1][j]
        image[i][j] = binadd(image[i - 1][j - 1], image[i - 1][j])
        # image[i][j] = image[i - 1][j - 1]+ image[i - 1][j]


imshow(image, interpolation='none', cmap='hot')

show()