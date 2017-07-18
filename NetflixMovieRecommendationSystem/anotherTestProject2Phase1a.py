'''
>>> genreList = createGenreList()
>>> genreList[2]
'Adventure'
>>> len(genreList)
19
>>> genreList[17]
'War'
>>> userList = createUserList()
>>> numUsers = len(userList)
>>> movieList = createMovieList()
>>> numMovies = len(movieList)
>>> rawRatings = readRatings()
>>> [rLu, rLm] = createRatingsDataStructure(numUsers, numMovies, rawRatings)
>>> round(meanUserRating(1, rLu), 2)
3.61
>>> [round(meanUserRating(x, rLu), 2) for x in range(1, 11)] 
[3.61, 3.71, 2.8, 4.33, 2.87, 3.64, 3.97, 3.8, 4.27, 4.21]
>>> min([(meanUserRating(x, rLu), x) for x in range(1, numUsers+1)])[1]
181
>>> round(meanUserRating(181, rLu), 2)
1.49
>>> max([(meanUserRating(x, rLu), x) for x in range(1, numUsers+1)])[1]
849
>>> round(meanUserRating(849, rLu), 2)
4.87
>>> round(meanMovieRating(1, rLm), 2)
3.88
>>> max([(meanMovieRating(x, rLm), x) for x in range(1, numMovies+1)])[1]
1653
>>> len(rLm[1652])
1
>>> max([(meanMovieRating(x, rLm), x) for x in range(1, numMovies+1) if len(rLm[x-1]) >= 10])[1]
408
>>> movieList[407]["title"]
'Close Shave, A (1995)'
>>> sorted([movieList[y[1]-1]["title"] for y in sorted([(meanMovieRating(x, rLm), x) for x in range(1, numMovies+1) if len(rLm[x-1]) >= 10])[::-1][:10]])
['12 Angry Men (1957)', 'Casablanca (1942)', 'Close Shave, A (1995)', 'Rear Window (1954)', "Schindler's List (1993)", 'Shawshank Redemption, The (1994)', 'Star Wars (1977)', 'Usual Suspects, The (1995)', 'Wallace & Gromit: The Best of Aardman Animation (1996)', 'Wrong Trousers, The (1993)']
'''
#-------------------------------------------------------
from project2Phase1a import *
#-------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
