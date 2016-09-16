import numpy as np
import matplotlib.cm as cm
from pylab import imshow, show, savefig
import matplotlib.pyplot as plt
from timeit import default_timer as timer
# from numba import autojit # acseleration
from math import *

# @autojit
def mandel(x, y, max_iters):
  """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
  """
  c = complex(x, y)
  z = 0.0j
  r = complex(2., 1.)
  for i in range(max_iters):
    z = z * z + c # stock
    if (z.real*z.real + z.imag*z.imag) >= 4:
      return i

  return max_iters

# @autojit
def create_fractal(min_x, max_x, min_y, max_y, image, iters):
  height = image.shape[0]
  width = image.shape[1]

  pixel_size_x = (max_x - min_x) / width
  pixel_size_y = (max_y - min_y) / height
    
  for x in range(width):
    real = min_x + x * pixel_size_x
    for y in range(height):
      imag = min_y + y * pixel_size_y
      color = mandel(real, imag, iters)
      image[y, x] = color

x = -1.2 # center of image
y = 0.31
zoom = 40
min_x = x - 2./zoom
max_x = x + 1./zoom
min_y = y + 1./zoom
max_y = y - 1./zoom

toler = 200
image = np.zeros((2 * toler, 3 * toler), dtype = np.uint8)
start = timer()
create_fractal(min_x, max_x, min_y, max_y, image, 100) # when zoom - 20 could be bigger
# create_fractal(-2.0, 1.0, -1.0, 1.0, image, 40) # when zoom - 20 could be bigger
# create_fractal(-2.0, 1.0, -1.0, 1.0, image, 40) # when zoom - 20 could be bigger

dt = timer() - start
print "Mandelbrot created in %f s" % dt

# print image

# imshow(image, cmap='hot')
# imshow(image, interpolation='none',  cmap=cm.Greys_r)
# imshow(image, interpolation='none',  cmap = plt.get_cmap('gray'), vmin = -100, vmax = 100)
imshow(image, interpolation='none', cmap='hot')

# savefig('/Users/alx1dr/Desktop/foo.png')
show()

