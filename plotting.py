import matplotlib.pyplot as plt
import numpy as np
from cartopy import crs as ccrs, geodesic as gd
import cartopy.io.img_tiles as cimgt
import shapely

plt.style.use("./styles/mystyle.mplstyle")

def lon_kmtodeg(xkm,lat):
    return xkm/(111.320*np.cos(np.deg2rad(lat)))

def closemap(par):
    request = cimgt.OSM() #Requesting open street map
    #request = cimgt.GoogleTiles() #Requesting google street map

    #Drawing the plot
    fig = plt.figure()
    ax = plt.subplot(projection=request.crs) #Specifying the projection
    ax.add_image(request, par.close_zoom_lvl, interpolation='spline36') #Adding the map
    ax.set_extent([par.lon-lon_kmtodeg(par.xkm,par.lat)/2, par.lon+lon_kmtodeg(par.xkm,par.lat)/2,
                    par.lat-par.ykm/(2*110.574), par.lat+par.ykm/(2*110.574)]) #Limiting the map area (Crashs without this)
    gl = ax.gridlines(draw_labels=True,zorder=5) #Drawing grid lines
    gl.xlabel_style = {'size':14}
    gl.ylabel_style = {'size':14}
    gl.top_labels = None
    gl.right_labels = None

    #Marking the spot and drawing the scale circle
    ax.scatter(par.lon,par.lat,c='red',transform=ccrs.PlateCarree())
    ax.annotate(par.name,(par.lon+lon_kmtodeg(par.xkm,par.lat)*0.02,par.lat+0.02/110.574),zorder=6,c='red',fontsize=13,transform=ccrs.PlateCarree())
    circle_points = gd.Geodesic().circle(par.lon, par.lat, radius=par.circle_rad*1000)
    geom = shapely.geometry.Polygon(circle_points) #Generating the circle object
    ax.add_geometries((geom,), crs=ccrs.PlateCarree(), facecolor='none', zorder=6, edgecolor='red', linewidth=2)
    ax.annotate(f'{par.circle_rad}km',(par.lon-lon_kmtodeg(par.circle_rad*0.9,par.lat),par.lat),zorder=6,c='red',fontsize=13,transform=ccrs.PlateCarree())

    ax.set_title('Esimerkki havasemakartta EFHK')
    #plt.savefig('map1.png',dpi=200)
    plt.show()

def farmap(par):
    request = cimgt.OSM() #Requesting open street map
    #request = cimgt.GoogleTiles() #Requesting google street map

    text_offset = 1.5 #Text will not overlap with the location marker

    #Drawing the plot
    fig = plt.figure()
    ax = plt.subplot(projection=request.crs) #Specifying the projection
    ax.add_image(request, par.far_zoom_lvl, interpolation='spline36') #Adding the map
    ax.set_extent([par.lon-lon_kmtodeg(par.far_xkm,par.lat)/2, par.lon+lon_kmtodeg(par.far_xkm,par.lat)/2,
                    par.lat-par.far_ykm/(2*110.574), par.lat+par.far_ykm/(2*110.574)]) #Limiting the map area (Crashs without this)
    gl = ax.gridlines(draw_labels=True,zorder=5) #Drawing grid lines
    gl.xlabel_style = {'size':14}
    gl.ylabel_style = {'size':14}
    gl.top_labels = None
    gl.right_labels = None

    #Marking the spot
    ax.scatter(par.lon,par.lat,s=80,c='red',zorder=6,transform=ccrs.PlateCarree())
    ax.annotate(par.name,(par.lon+lon_kmtodeg(par.xkm,par.lat)*text_offset,par.lat+text_offset*2/110.574),c='red',fontsize=16,zorder=6,transform=ccrs.PlateCarree())

    ax.set_title('Esimerkki havasemakartta EFHK')
    #plt.savefig('map2.png',dpi=200)
    plt.show()

def twinmap(par):
    request = cimgt.OSM() #Requesting open street map
    #request = cimgt.GoogleTiles() #Requesting google street map

    text_offset = 1.5 #Text will not overlap with the location marker

    #Drawing the plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), subplot_kw={"projection": request.crs})
    ax1.add_image(request, par.far_zoom_lvl, interpolation='spline36') #Adding the map
    ax1.set_extent([par.lon-lon_kmtodeg(par.far_xkm,par.lat)/2, par.lon+lon_kmtodeg(par.far_xkm,par.lat)/2,
                    par.lat-par.far_ykm/(2*110.574), par.lat+par.far_ykm/(2*110.574)]) #Limiting the map area (Crashs without this)
    gl1 = ax1.gridlines(draw_labels=True,zorder=5) #Drawing grid lines
    gl1.xlabel_style = {'size':14}
    gl1.ylabel_style = {'size':14}
    gl1.top_labels = None
    gl1.right_labels = None

    #Marking the spot and drawing the scale circle
    ax1.scatter(par.lon,par.lat,s=80,c='red',zorder=6,transform=ccrs.PlateCarree())
    ax1.annotate(par.name,(par.lon+lon_kmtodeg(par.xkm,par.lat)*text_offset,par.lat+text_offset*2/110.574),c='red',fontsize=16,zorder=6,transform=ccrs.PlateCarree())

    ax2.add_image(request, par.close_zoom_lvl, interpolation='spline36') #Adding the map
    ax2.set_extent([par.lon-lon_kmtodeg(par.xkm,par.lat)/2, par.lon+lon_kmtodeg(par.xkm,par.lat)/2,
                    par.lat-par.ykm/(2*110.574), par.lat+par.ykm/(2*110.574)]) #Limiting the map area (Crashs without this)
    gl2 = ax2.gridlines(draw_labels=True,zorder=5) #Drawing grid lines
    gl2.xlabel_style = {'size':14}
    gl2.ylabel_style = {'size':14}
    gl2.top_labels = None
    gl2.right_labels = None

    #Marking the spot and drawing the circle
    ax2.scatter(par.lon,par.lat,c='red',transform=ccrs.PlateCarree())
    ax2.annotate(par.name,(par.lon+lon_kmtodeg(par.xkm,par.lat)*0.02,par.lat+0.02/110.574),zorder=6,c='red',fontsize=13,transform=ccrs.PlateCarree())
    circle_points = gd.Geodesic().circle(par.lon, par.lat, radius=par.circle_rad*1000)
    geom = shapely.geometry.Polygon(circle_points) #Generating the circle object
    ax2.add_geometries((geom,), crs=ccrs.PlateCarree(), facecolor='none', zorder=6, edgecolor='red', linewidth=2)
    ax2.annotate(f'{par.circle_rad}km',(par.lon-lon_kmtodeg(par.circle_rad*0.9,par.lat),par.lat),zorder=6,c='red',fontsize=13,transform=ccrs.PlateCarree())

    fig.suptitle('Esimerkki havasemakartta EFHK',fontsize = 20)
    #plt.savefig('map1.png',dpi=200)
    plt.show()   
