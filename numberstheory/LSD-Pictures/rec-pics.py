import numpy as np
from pylab import imshow, show
import matplotlib.image as mpimg
import matplotlib
from math import *

from random import uniform, randint, random
# img=mpimg.imread('ff.png')[:,:,0]
img=mpimg.imread('stinkbug.png')[:,:,0]

prev_i = randint(1, img.shape[0])
prev_j = randint(1, img.shape[1])


for i in xrange(1000):
	cur_i = int(sin(prev_i)*10)
	cur_j = int(cos(prev_j)*10)
	img[cur_i][cur_j] = 1
	prev_i = cur_i
	prev_j = cur_j
# for i in xrange(1, img.shape[0] - 1):
# 	for j in xrange(1,img.shape[1] - 1):
# 		# img[i][j] = (cos( (img[i-1][j-1] + img[i-1][j+1])*0.5 + img[i-1][j]*0.5 )) % 1
# 		# img[i][j] = ( cos((img[i-1][j-1]+img[i-1][j]+img[i-1][j+1])*0.45 + img[i][j]*0.94) ) % 1
# 		# varik = random()
# 		if img[i-1][j] < 0.2:
# 			img[i][j] = (img[i-1][j-1]+
# 						   img[i-1][j]+
# 						   img[i-1][j+1]) % 1
						  



imshow(img, interpolation='none', cmap='hot')
# imshow(img, cmap='YlGnBu')
show()