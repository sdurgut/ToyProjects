'''
>>> userList = createUserList()
>>> len(userList)
943
>>> userList[10]["occupation"]
'other'
>>> sorted([str(x) for x in userList[55].values()])
['25', '46260', 'M', 'librarian']
>>> len([x for x in userList if x["gender"]=="F"])
273
>>> movieList = createMovieList()
>>> len(movieList)
1682
>>> movieList[27]["title"]
'Apollo 13 (1995)'
>>> movieList[78]["title"].split("(")[0]
'Fugitive, The '
>>> sorted([x for x in movieList[1657].values() if type(x) == str])
['', '06-Dec-1996', 'Substance of Fire, The (1996)', 'http://us.imdb.com/M/title-exact?Substance%20of%20Fire,%20The%20(1996)']
>>> numUsers = len(userList)
>>> numMovies = len(movieList)
>>> rawRatings = readRatings()
>>> rawRatings[:2]
[(196, 242, 3), (186, 302, 3)]
>>> len(rawRatings)
100000
>>> len([x for x in rawRatings if x[0] == 1])
272
>>> len([x for x in rawRatings if x[0] == 2])
62
>>> sorted([x for x in rawRatings if x[0] == 2][:11])
[(2, 13, 4), (2, 50, 5), (2, 251, 5), (2, 280, 3), (2, 281, 3), (2, 290, 3), (2, 292, 4), (2, 297, 4), (2, 303, 4), (2, 312, 3), (2, 314, 1)]
>>> [x for x in rawRatings if x[1] == 1557]
[(405, 1557, 1)]
>>> [rLu, rLm] = createRatingsDataStructure(numUsers, numMovies, rawRatings)
>>> len(rLu)
943
>>> len(rLm)
1682
>>> len(rLu[0])
272
>>> min([len(x) for x in rLu])
20
>>> min([len(x) for x in rLm])
1
>>> sorted(rLu[18].items())
[(4, 4), (8, 5), (153, 4), (201, 3), (202, 4), (210, 3), (211, 4), (258, 4), (268, 2), (288, 3), (294, 3), (310, 4), (313, 2), (319, 4), (325, 4), (382, 3), (435, 5), (655, 3), (692, 3), (887, 4)]
>>> len(rLm[88])
275
>>> movieList[88]["title"]
'Blade Runner (1982)'
>>> rLu[10][716] == rLm[715][11]
True
>>> commonMovies = [m for m in range(1, numMovies+1) if m in rLu[0] and m in rLu[417]]
>>> commonMovies
[258, 269]
>>> rLu[0][258]
5
>>> rLu[417][258]
5
>>> rLu[0][269]
5
>>> rLu[417][269]
5
'''
#-------------------------------------------------------
from project2Phase1a import *
#-------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
