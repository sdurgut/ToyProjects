# Original Author : Steven Miller (Spring 2012)
# Modified by Sriram Pemmaraju (Spring 2014)
# Modified by Sriram Pemmaraju (Spring 2015)

''' Phase 1 of Programming Project 1 CS:1210 Spring 2015'''

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
    coordinates.append([int(x) for x in line[line.index('[')+1 : line.index(']')].split(',')])

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
