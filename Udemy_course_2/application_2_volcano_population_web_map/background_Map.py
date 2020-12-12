import folium
import pandas
from color_by_elevation_function import color_elevation_check

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
names = list(data['NAME'])
elev = list(data['ELEV'])

map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fgv = folium.FeatureGroup(name='Volcanoes')



for la,lo,el in zip(lat,lon,elev):
        fgv.add_child(folium.CircleMarker(location=[la, lo], radius=6, popup=str(el)+' m', fill_color = color_elevation_check(el), color = 'grey', fill_opacity = 0.7))


fgpop = folium.FeatureGroup(name='Population')


fgpop.add_child(folium.GeoJson(data=open('world.json', 'r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange'  if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red'} ))




map.add_child(fgv)
map.add_child(fgpop)


map.add_child(folium.LayerControl())


map.save('Map1.html')
