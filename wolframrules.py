import numpy as np
from pylab import imshow, show
from random import randint

def newgen(arr, rules):
    gen = []
    gen.append(rules['0' + str(arr[0]) + str(arr[1])])
    for i in xrange(1, len(arr)-1):
        gen.append(rules[str(arr[i-1]) + str(arr[i])+str(arr[i+1])])
    gen.append(rules[str(arr[-2]) + str(arr[-1]) + '0'])
    return gen

rules = { '000':0,
          '001':1,
          '010':1,
          '011':1,
          '100':0,
          '101':1,
          '110':1,
          '111':0}

n = 100
state = [0]
for i in xrange(n-2):
    state.append(randint(0,1))
state.append(0)

image = []
for x in xrange(400):
    image.append(state)
    state = newgen(state, rules)
# print image
imshow(image, interpolation='none', cmap='gray')
show()
# arr = np.zeros((n, len(firststate)), dtype = np.uint8)
# print newgen(firststate, rules)





# image = np.ones((n, n), dtype = np.uint8)

# for i in xrange(n):
#     for j in xrange(i + 1):
#         # image[i][j] = image[i - 1][j - 1] + image[i - 1][j]
#         image[i][j] = binadd(image[i - 1][j - 1], image[i - 1][j])

