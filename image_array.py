import numpy as np
from pylab import imshow, show

image = np.zeros((4, 3), dtype = np.uint16)
image[2][2] = 16000
image[0][1] = 2444
image[3][2] = 1373

print image
imshow(image, interpolation='none')
show()