def line_gen():
    file = open('locations.list', 'r', encoding='ISO-8859-1')
    for line in file:
        yield line

def location_search(year, cut):
    '''
    str, int -> list
    Returns the chosen amount of movies and locations of the chosen year.
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
    return result[:cut]
