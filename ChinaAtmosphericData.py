import os
import matplotlib as mpl
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
import numpy as np
from pyhdf.SD import SD, SDC
import matplotlib.colors as colors

#hdf = SD("L8ANC2021301.hdf_fused", SDC.READ)
#hdf = SD("L8ANC2013224.hdf_fused", SDC.READ)
#hdf = SD("L8ANC2013302.hdf_fused", SDC.READ)
#print(hdf.datasets())
#datasets_dic = hdf.datasets()
#for d in datasets_dic:
#    if "aot" in d:
#        print(d)

def plot(d, hdf):
    data = hdf.select(d)
    latitude = np.arange(0, 7200, 1)
    longitude = np.arange(0, 3600, 1)
    z = np.flip(data.get(), axis = 0)
    fig, ax = plt.subplots()
    pcm = ax.pcolorfast(latitude,longitude,z,cmap='jet',norm=colors.LogNorm())
    fig.colorbar(pcm, ax=ax, extend='max')

for file in os.listdir("/Users/daniellong/Documents/programming/Python/LandSat/Ozone:Water/Bulk Order full ozone/water vapor/MODIS Fused C2"):
    print(file)
    plot("Coarse Resolution Ozone", SD("Ozone:Water/Bulk Order full ozone/water vapor/MODIS Fused C2/" + file, SDC.READ))
    plt.savefig("/Users/daniellong/Documents/programming/Python/LandSat/frames/" + file[:-10] + '.png')
    plt.clf()
    plt.cla()

#for x in data:
 #   if x.any():
  #      if x[5] != 0:
   #         print(x)

#for idx,sds in enumerate(datasets_dic.keys()):
 #   print(idx,sds)
  #  data3D = hdf.select(sds)
   # print(data3D.get().shape)

##m = Basemap(projection='cyl', resolution='l', llcrnrlat=-90, urcrnrlat = 90, llcrnrlon=-180, urcrnrlon = 180)
##m.drawcoastlines(linewidth=0.5)
##m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
##m.drawmeridians(np.arange(-180., 181., 45.), labels=[0, 0, 0, 1])
##x, y = m(longitude, latitude)
##m.pcolormesh(x, y, z)

