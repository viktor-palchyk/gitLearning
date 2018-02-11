"""
Folium is a library which helps to work with javascript and html to python
"""

import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
	if elevation < 1000:
		return 'green'
	elif 1000 <= elevation <= 3000:
		return 'orange'
	else:
		return 'red'


m_ob = folium.Map(location=[38.58, -99], zoom_start = 6, tiles="Mapbox Bright")

feat_group_volcanoes = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
	feat_group_volcanoes.add_child(folium.CircleMarker(
												location=[lt, ln],
												radius=5,
												popup=str(el)+" m",
												fill_color=color_producer(el),
												color = 'grey',
												fill_opacity=0.7
											)
						)


feat_group_population = folium.FeatureGroup(name="Population")

feat_group_population.add_child(folium.GeoJson(
										data=open("world.json", 'r', encoding='utf-8-sig'), 
										style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] > 100000000 
																					else 'green'}
									)
					)


#The map object is added with children layers
m_ob.add_child(feat_group_volcanoes)
m_ob.add_child(feat_group_population)

#The layer control is needed to switch on and off the needed layer on the map in the right top corner
m_ob.add_child(folium.LayerControl())

m_ob.save("Map2.html") 