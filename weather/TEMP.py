from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
map = Basemap(projection='ortho', lat_0=39, lon_0=51,
              resolution='l', area_thresh=1000.0)

# map = Basemap(projection='ortho', lat_0=50, lon_0=-100,
#               resolution='l', area_thresh=500.0)

 
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='coral')
 
plt.show()