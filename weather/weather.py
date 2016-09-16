#import pylab
from pylab import *
from scipy import interpolate
import forecastio
api_key = "98d9ec353b766546308689c1553e96a2"

lng = 39.210
lat = 51.672
R = 1 # biggr than before (0.068) 0.1

a = 7 # defenition, density of points
x = np.linspace(lng - R, lng + R, a)
y = np.linspace(lat - R, lat + R, a)
X,Y = np.meshgrid(x,y)



T = [[ 17.04,  16.2,   15.93,  15.62,  15.28,  15.16,  15.05],
     [ 15.97,  15.61,  15.54,  15.27,  14.91,  14.75,  14.63],
     [ 15.22,  15.06,  14.99,  14.83,  14.61,  14.3,   14.13],
     [ 14.6,   14.44,  16.41,  16.34,  16.24,  13.83,  13.64],
     [ 14.02,  13.76,  13.9,   13.88,  13.72,  13.33,  13.17],
     [ 13.67,  13.49,  13.32,  13.29,  13.31,  13.08,  12.89],
     [ 13.36,  13.14,  12.82,  12.72,  12.75,  12.62,  12.49]]
# T = np.zeros((a,a)) # [lng][lat][t]
# for i in range(a-1, -1, -1):
#     for j in range(a):
#         T[i][j] = forecastio.load_forecast(api_key, y[a-1-i], x[j]).currently().temperature

# T = cos(X) + sin(Y)

# T = array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.], # do not forget that inverted y-axis
#            [ 0.,  0.,  0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.,  10.,  0.]])

T = np.flipud(T) # y-inversion



print(T)
# axis([lng-1.2*R, lng+1.2*R, lat-1.2*R, lat+1.2*R])


interpolation = True
mu = 8 # definition of contour
if interpolation:
    k2 = 70j
    xnew,ynew = np.mgrid[lng-R:lng+R:k2,lat-R:lat+R:k2]
    tck = interpolate.bisplrep(X,Y,T,s=0)
    znew = interpolate.bisplev(xnew[:,0],ynew[0,:],tck)
    contourf(xnew,ynew,znew, mu, alpha=.99, cmap='hot') #cm.coolwarm
    colorbar()
    C = contour(xnew, ynew, znew, mu, colors='black', linewidth=.5)
    clabel(C, inline=1, fontsize=10)
else:
    contourf(X, Y, T, mu, alpha=.85, cmap='hot')
    colorbar()
    C = contour(X, Y, T, mu, colors='black', linewidth=.5)
    clabel(C, inline=1, fontsize=10)


show()