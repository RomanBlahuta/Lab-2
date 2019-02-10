import geocoder
import folium

def coordinates_search(location):
    '''
    str -> list
    Gives coordinates of location by its name.
    '''
    try:
        geo = geocoder.arcgis(location)
        return geo.latlng
    except:
        return "Couldn't find the coordinates"

def map_create(lst):
    '''
    list -> None
    Creates the html-map based on the information from the "lst" list.
    '''
    map = folium.Map()
    movie_names = folium.FeatureGroup(name="Movie information")
    locations_names = folium.FeatureGroup(name="Locations' names")
    for movie in lst:
        loc = movie[1]
        coords = coordinates_search(loc)
        locations_names.add_child(folium.Marker(location=[coords[0], coords[1]], popup=loc, icon=folium.Icon()))
        movie_names.add_child(folium.Marker(location=[coords[0], coords[1]], popup=movie[0], icon=folium.Icon()))
    fg_pp = folium.FeatureGroup(name="Population")
    fg_pp.add_child(folium.GeoJson(data=open('world.json', 'r',
                                             encoding='utf-8-sig').read(),
                                   style_function=lambda x: {'fillColor': 'green'
                                   if x['properties']['POP2005'] < 10000000
                                   else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                   else 'red'}))
    map.add_child(fg_pp)
    gdp = folium.FeatureGroup(name="GDP")
    map.add_child(movie_names)
    map.add_child(fg_pp)
    map.add_child(locations_names)
    map.add_child(folium.LayerControl())
    map.save('Map_1.html')
