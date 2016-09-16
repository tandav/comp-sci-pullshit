from pylab import *
from scipy import interpolate
import forecastio
api_key = "98d9ec353b766546308689c1553e96a2"
lng = 6
lat = 3
R = 101

class Point:
    x = None
    y = None
    t = None
    def init(self, x, y, dens):
        self.x = np.linspace(x - R, x + R, dens)
        self.y = np.linspace(y - R, y + R, dens)

a = Point()
a.init(2,3,5)
print(a.x)
