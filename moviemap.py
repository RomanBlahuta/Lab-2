import geocoder
import folium

def coordinates_search(location):
    try:
        geo = geocoder.arcgis(location)
        return geo.latlng
    except:
        return "Couldn't find the coordinates"

def line_gen():
    file = open('locations.list', 'r', encoding='ISO-8859-1')
    for line in file:
        yield line

def location_search(year):
    '''
    '''
    result = []
    gen = line_gen()
    for skip in range(14):
        a = next(gen)
    for time in range(1241772):
        line = next(gen)
        if year in line:
            line = line.split('\t')
            for i in line:
                if len(i) == 0:
                    w = line.index(i)
                    line = line[:w] + line[w+1:]
            a = line[-1]
            line = line[:-1]
            line.append(a[:-1])
            result.append(line)
    return result[:130]

def map_create(lst):
    '''
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

def project():
    '''
    '''
    try:
        year = input('Enter a year: ')
        if year == '':
            print('Incorrect input.')
        else:
            a = int(year)
    except:
        print('Incorrect input.')
    lst = location_search(year)
    map_create(lst)


project()
