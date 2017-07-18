import string

def storeCity(line, cities) :
    ''' Extracts the city name and state and stores it. '''
    city  = line[:line.index(',')].strip()
    state = line[line.index(',')+1:line.index('[')].strip()
    cities.append(city + ' ' + state)
    
def storePopulation(line, population) :
    ''' Extracts the population from a line and stores it. '''
    population.append(int(line[line.index(']')+1:]))
    
def storeCoordinates(line, coordinates) :
    ''' Extracts the coordinates from a line and stores them. '''
    coordinates.append(map(int, line[line.index('[')+1 : line.index(']')].split(',')))

def storeDistances(cities, newDistances, distances) :
    ''' Stores the distances to/from each city to the current city. '''
    
    # Skip over the first city since its distances haven't been seen yet
    if not cities: 
        return
    
    # Convert all new distances to integers
    newDistances = [int(x) for x in newDistances]
    
    # Compute dimension of new distances array - 1
    n = len(newDistances)-1
    
    # Set the distance of city from itself to zero
    distances.append([0])

    # For each city already seen
    for i in range(n+1) :
        # Append the distance to this city
        distances[n-i] = distances[n-i]    + [newDistances[i]]
        # Insert the distance from this city
        distances[n+1] = [newDistances[i]] + distances[n+1]
               
def isCityLine(line) :
    ''' Returns whether a line contains city information.'''
    return line[0].isalpha()

def isDistanceLine(line) :
    ''' Returns whether a line contains distance information.'''
    return line[0].isdigit()

def createDataStructure():
    ''' Reads from miles.dat and returns a data structure containing all the information in miles.dat.
        The data structure is a list of 4 items. The first item is a length-128 list of city names.
        The second item is a length-128 list of coordinates. The third item is a length-128 list of 
        populations. The 4th item is a 128 by 128 matrix of distances.'''

    cities      = []     # List of valid city names (city name and state)
    coordinates = []     # Coordinates (lat and long) of each city
    population  = []     # Population of each city
    distances   = []     # Distances to/from each pair of cities

    accDist = []     # Accumulates distances seen over several lines

    f = open("miles.dat", "r")
    for line in f:
        # If this line has distances, accumulate the new distances
        if isDistanceLine(line) :
            accDist = accDist + line.split()
        # If this line has data for a new city
        elif isCityLine(line) :
            # Store the distances accumulated for the previous city
            storeDistances(cities,accDist,distances)
            accDist = []
            # Store the name, coordinates, and popuation for this city
            storeCity(line,cities)
            storeCoordinates(line,coordinates)
            storePopulation(line,population)
    f.close()

    # Store the distances for the last city
    storeDistances(cities,accDist,distances)
 
    return [cities, coordinates, population, distances]

def getCoordinates(name, data) :
    ''' Returns the coordinates for a city as a list of lat and long.
        Returns an empty list if the city name is invalid. '''
    
    cities = data[0]
    coordinates = data[1]

    result = []
    if name in cities :
        result = coordinates[cities.index(name)]
    return result

def getPopulation(name, data) :
    ''' Returns the popultion for a city.
        Returns None if the city name is invalid.'''

    cities = data[0]
    population = data[2]
           
    result = None
    if name in cities :
        result = population[cities.index(name)]
    return result
       
def getDistance(name1, name2, data) :
    ''' Returns the distance between two cities. 
        Returns None if either city's name is invalid.'''
 
    cities = data[0]
    distances = data[3]
           
    result = None
    if name1 in cities and name2 in cities :
        result = distances[cities.index(name1)][cities.index(name2)]
    return result

def nearbyCities(name, r, data) :
    ''' Returns a list of cities within distance r of named city
        sorted in alphabetical order.
        Returns an empty list if city name is invalid. '''
 
    cities = data[0]
    distances = data[3]
           
    result = []
    if name in cities :                # If the city name is valid
        i = cities.index(name)           # Get the index of the named city
        for j in range(len(cities)) :      # For every other city
            if distances[i][j] <= r :      # If within r of named city
                result = result + [cities[j]]  # Add to result
    result.sort() 
    return result




########################################### pahse2 #######################################33








def unserved(served, data, city, r) :
    ''' Returns the number of unserved cities within distance r of city. '''
    
    result = 0
    cities = data[0]
  
    # for each city within distance r of city
    for c in nearbyCities(city, r, data) :
        # if not served, add it to the list of unserved citys
        if not served[cities.index(c)] :
            result = result + 1
    return result

def nextFacility(served, data, r) :
    ''' Returns the name of the city that can service the most unserved 
        cities within radius r. Returns None if all cities are served. '''
    
    facility = None      # Name of city that will be the next service facility
    numberServed = 0     # Number of cities that facility will serve
    
    cities = data[0]
    distances = data[3]

    # For each city
    for c in range(len(cities)) :
        # compute how many unserved cities will be served by city c
        willBeServed = unserved(served, data, cities[c], r)
        # if it can serve more cities than the previous best city
        if willBeServed >  numberServed:
            # make it the service center
            facility = cities[c]
            numberServed = willBeServed
    return facility
            
def locateFacilities(data, r) :
    ''' Returns an alphabetically sorted list of the cities in which facilities
        must be located to service all cities with a service radius of r. '''

    cities = data[0]
    distances = data[3]
    
    # List of cities that are served by current facilities
    served = [False] * len(cities)
    
    # List of cities that are service facilities
    facilities = []
    
    # Get the city that is the next best service facility
    facility = nextFacility(served, data, r )
    
    # While there are more cities to be served
    while facility :
        
        # Mark the service facility as served
        served[cities.index(facility)] = True
        
        # Mark each city as served that will be served by this facility
        for city in nearbyCities(facility, r, data) :
            served[cities.index(city)] = True
            
          # Append the city to the list of service facilities
        facilities.append(facility)
        
        # Get the city that is the next best service facility
        facility = nextFacility(served, data, r)
        
    # Sort the list of facilties alphabetically
    facilities.sort()
    
    return facilities







##################################Phase  3######################################################





def display(facilities, data):

	lattitue = 0
	longitude = 0
	height = 0

	f = open("visualization800.kml","w")
	f.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n")
	f.write("<Document>"), f.write("<Style id=\"smallLine\">\n")
	f.write("<LineStyle\n><color>7f00007f</color\n><width>1</width\n></LineStyle\n><PolyStyle><color>7f00007f</color\n></PolyStyle\n></Style\n>")

	for c in facilities:
		idx = data[0].index(c)
		lattitue = -1 * data[1][idx][1]/100.0
		longitude = data[1][idx][0]/100.0
		cityName =  ", ".join(data[0][idx].split())

		f.write("<Placemark>\n")
		f.write("<name>")
		f.write(cityName)
		f.write("</name>\n")
		f.write("<description>")
		f.write(cityName)
		f.write("</description>\n")

		f.write("<Point>\n")
		f.write("<coordinates>")
		f.write(str(lattitue)) , f.write(","), f.write(str(longitude)) , f.write(","), f.write(str(height))
		f.write("</coordinates>\n")
		f.write("</Point>\n")
		f.write("</Placemark>\n")


		nearbyCityList = nearbyCities(c,800,data)

		for city in nearbyCityList:
			idx1 = data[0].index(city)
			lattitue1 = -1 * data[1][idx1][1]/100.0
			longitude1 = data[1][idx1][0]/100.0
			cityName1 = ", ".join(data[0][idx1].split())
			f.write("<Placemark>\n")
			f.write("<name>"), f.write(c), f.write(" - "), f.write(city), f.write("</name>\n")
			f.write("<description>Path from"), f.write(c), f.write(" to "), f.write(city), f.write("</description>\n")
			f.write("<styleUrl>#smallLine</styleUrl>\n")
			f.write("<LineString>\n<extrude>1</extrude>\n<tessellate>1</tessellate>\n")
			f.write("<altitudeMode>absolute</altitudeMode>\n")
			f.write("<coordinates>")
			f.write(str(lattitue)) , f.write(","), f.write(str(longitude)) , f.write(","), f.write(str(height))
			f.write(" ")
			f.write(str(lattitue1)) , f.write(","), f.write(str(longitude1)) , f.write(","), f.write(str(height))
			f.write("</coordinates>\n")
			f.write("</LineString>\n")
			f.write("</Placemark>\n")


	f.write("</Document>\n")
	f.write("</kml>")
	f.close()



data = createDataStructure()
facilities = locateFacilities(data, 800)
display(facilities, data)