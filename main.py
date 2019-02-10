from locations_of_year import location_search, line_gen
from map_building import map_create, coordinates_search
def project():
    '''
    None -> None
    Activates the program.
    '''
    try:
        year = input('Enter a year:  ')
        cut = input('Enter the amount of movies to work on:  ')
        if year == '' or cut == '':
            print('Incorrect input.')
            return 0
        else:
            a = int(year)
            intcut = int(cut)
    except:
        print('Incorrect input.')
        return 0
    lst = location_search(year, intcut)
    map_create(lst)


project()
