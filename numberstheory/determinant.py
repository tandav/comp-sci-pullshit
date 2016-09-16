from random import shuffle
import numpy as np
from pylab import imshow, show


def det(a):
    return  a[0]*a[4]*a[8]+a[1]*a[5]*a[6]+a[2]*a[3]*a[7]-a[2]*a[4]*a[6]-a[0]*a[5]*a[7]-a[1]*a[3]*a[8]

# [2, 7, 6, 4, 1, 8, 9, 5, 3] 
# [8, 3, 6, 4, 9, 2, 1, 5, 7]
# [7, 1, 5, 6, 8, 3, 2, 4, 9]

best = [7, 1, 5, 6, 8, 3, 2, 4, 9]

# mat = [7, 2, 6, 9, 3, 1, 4, 8, 5]
# best = 412
# for x in xrange(100000):
#     shuffle(mat)
#     if det(mat) >= best:
#         best = mat
#         print mat, det(mat)


image = [[best[0],best[1],best[2]],
         [best[3],best[4],best[5]],
         [best[6],best[7],best[8]] ]

# print mat, det(mat)
imshow(image, interpolation='none', cmap='gray_r')
show()