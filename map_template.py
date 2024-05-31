from collections import namedtuple
import plotting as plott

#Coordinates for drawing and fetching the data
name = 'EFHK'
circle_rad = 1 #km
lon = 24.9570
lat = 60.3277
xkm = 5 #Total dimension
ykm = 5 #Total dimension
far_xkm = 300
far_ykm = 300
close_zoom_lvl = 13 #Bigger=more detailed
far_zoom_lvl = 7 #For another bigger map 

params = namedtuple('par',['name','circle_rad','lon','lat','xkm','ykm','far_xkm','far_ykm','close_zoom_lvl','far_zoom_lvl'])
par = params(name,circle_rad,lon,lat,xkm,ykm,far_xkm,far_ykm,close_zoom_lvl,far_zoom_lvl)

#plott.closemap(par)
#plott.farmap(par)
plott.twinmap(par)