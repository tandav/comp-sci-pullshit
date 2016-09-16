import numpy as np
from pylab import imshow, show
import matplotlib.image as mpimg
import matplotlib
from math import *

from random import uniform, randint, random
# img=mpimg.imread('ff.png')[:,:,0]
img=mpimg.imread('stinkbug.png')[:,:,0]


# print len(img[0])
# print np.amin(img)

# for i in xrange(1, img.shape[0] - 1):
# 	for j in xrange(1,img.shape[1] - 1):
# 		# img[i][j] = (cos( (img[i-1][j-1] + img[i-1][j+1])*0.5 + img[i-1][j]*0.5 )) % 1
# 		# img[i][j] = ( cos((img[i-1][j-1]+img[i-1][j]+img[i-1][j+1])*0.45 + img[i][j]*0.94) ) % 1
# 		varik = random()
# 		if varik > 0.4:
# 			img[i][j] = (img[i-1][j-1]+
# 						   img[i-1][j]+
# 						   img[i-1][j+1]+
# 						   img[i][j-1]+
# 						   img[i][j]+
# 						   img[i][j+1]+
# 						   img[i+1][j-1]+
# 						   img[i+1][j]+
# 						   img[i+1][j+1])*i*j % 1
			# img[i][j] = sin(img[i][j])*cos(img[i][j])



imshow(img, interpolation='none', cmap='hot')
# imshow(img, cmap='YlGnBu')
show()