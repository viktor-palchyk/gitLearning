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

feat_group = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
	feat_group.add_child(folium.CircleMarker(
												location=[lt, ln],
												radius=5,
												popup=str(el)+" m",
												fill_color=color_producer(el),
												color = 'grey',
												fill_opacity=0.7
											)
						)
m_ob.add_child(feat_group)

m_ob.save("Map2.html") 