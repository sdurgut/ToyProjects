'''
>>> userList = createUserList()
>>> numUsers = len(userList)
>>> movieList = createMovieList()
>>> numMovies = len(movieList)
>>> rawRatings = readRatings()
>>> trainingSet = rawRatings[:80000]
>>> testingSet = rawRatings[80000:]
>>> [trUserRatings, trMovieRatings] = createRatingsDataStructure(numUsers, numMovies, trainingSet)
>>> [round(similarity(1, v, trUserRatings), 2) for v in range(1, numUsers+1)][:20]
[1.0, 0.44, 0.14, 0.56, 0.41, 0.38, 0.25, 0.69, 0.39, 0.09, 0.25, 0.03, 0.43, 0.01, 0.15, 0.24, 0.72, 0.08, -0.58, 0.01]
>>> [v for v in range(1, numUsers+1) if round(similarity(1, v, trUserRatings), 2) >= 0.9]
[1, 34, 47, 86, 166, 341, 351, 418, 547, 646, 685, 687, 740, 772, 797, 801, 810, 811, 812, 813, 824, 842, 856, 866, 895, 898]
>>> [v for v in range(1, numUsers+1) if round(similarity(1, v, trUserRatings), 2) >= 0.99]
[1, 47, 341, 351, 418, 547, 646, 685, 687, 740, 772, 801, 810, 811, 812, 813, 824, 842, 856, 866, 895, 898]
>>> sum([int(round(similarity(u, v, trUserRatings),2) == round(similarity(v, u, trUserRatings),2)) for u in range(1, 21) for v in range(1, 21)])
400
>>> sum([int(-1 <= round(similarity(10, v, trUserRatings),2) <= 1) for v in range(1, numUsers+1)])
943
>>> [len([v for v in range(1, numUsers+1) if round(similarity(u, v, trUserRatings), 2) >= 0.95]) for u in range(1, 21)]
[23, 31, 78, 97, 62, 10, 5, 62, 144, 12, 13, 52, 1, 16, 17, 27, 83, 51, 86, 62]
>>> [len([v for v in range(1, numUsers+1) if round(similarity(u, v, trUserRatings), 2) < 0]) for u in range(1, 21)]
[163, 230, 344, 346, 193, 273, 225, 219, 299, 259, 265, 422, 160, 431, 269, 258, 337, 251, 477, 428]
>>> sorted([(x[0], round(x[1], 2)) for x in kNearestNeighbors(1, trUserRatings, 21)])
[(47, 1.0), (341, 1.0), (351, 1.0), (418, 1.0), (547, 1.0), (646, 1.0), (685, 1.0), (687, 1.0), (740, 1.0), (772, 1.0), (801, 1.0), (810, 0.99), (811, 1.0), (812, 1.0), (813, 1.0), (824, 1.0), (842, 1.0), (856, 1.0), (866, 1.0), (895, 1.0), (898, 1.0)]
>>> x = kNearestNeighbors(1, trUserRatings, 1)[0][0]
>>> sum([int(similarity(1, x, trUserRatings) >= similarity(1, v, trUserRatings)) for v in range(2, numUsers+1)])
942
>>> y = kNearestNeighbors(100, trUserRatings, 1)[0][0]
>>> sum([int(similarity(100, y, trUserRatings) >= similarity(100, v, trUserRatings)) for v in range(2, numUsers+1)])
942
>>> sorted([(x[0], round(x[1], 3)) for x in kNearestNeighbors(101, trUserRatings, 92)])
[(9, 1.0), (36, 1.0), (51, 1.0), (61, 1.0), (91, 1.0), (105, 1.0), (110, 1.0), (126, 1.0), (134, 1.0), (140, 1.0), (143, 1.0), (147, 1.0), (155, 1.0), (169, 1.0), (179, 1.0), (202, 1.0), (205, 1.0), (206, 1.0), (219, 1.0), (220, 1.0), (225, 1.0), (228, 1.0), (229, 1.0), (240, 1.0), (241, 1.0), (278, 1.0), (282, 1.0), (284, 1.0), (300, 1.0), (317, 1.0), (335, 1.0), (341, 1.0), (355, 1.0), (362, 1.0), (364, 1.0), (369, 1.0), (372, 1.0), (375, 1.0), (377, 1.0), (405, 1.0), (408, 1.0), (414, 1.0), (426, 1.0), (433, 1.0), (444, 1.0), (451, 1.0), (475, 1.0), (476, 1.0), (485, 1.0), (502, 1.0), (509, 1.0), (510, 1.0), (511, 1.0), (515, 1.0), (520, 1.0), (529, 1.0), (573, 1.0), (574, 1.0), (583, 1.0), (589, 1.0), (600, 1.0), (603, 0.995), (604, 1.0), (616, 1.0), (626, 1.0), (646, 1.0), (673, 1.0), (687, 1.0), (695, 1.0), (720, 1.0), (725, 1.0), (740, 1.0), (752, 1.0), (766, 1.0), (767, 1.0), (777, 0.995), (787, 1.0), (797, 1.0), (801, 1.0), (811, 1.0), (812, 1.0), (816, 1.0), (820, 1.0), (846, 1.0), (850, 1.0), (853, 1.0), (863, 1.0), (884, 1.0), (898, 1.0), (911, 1.0), (914, 1.0), (926, 1.0)]
>>> L = kNearestNeighbors(900, trUserRatings, numUsers)
>>> len(L)
942
>>> round(L[0][1] - L[numUsers-2][1], 3)
2.0
>>> [round(kNearestNeighbors(u, trUserRatings, numUsers)[numUsers-2][1], 2) for u in range(1, 21)]
[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -0.63, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]
>>> testingSet[:5]
[(863, 1431, 4), (761, 1287, 1), (863, 322, 1), (828, 694, 2), (889, 523, 4)]
>>> friends = kNearestNeighbors(863, trUserRatings, 76)
>>> round(CFRatingPrediction(863, 1431, trUserRatings, friends), 3)
3.213
>>> friends = kNearestNeighbors(863, trUserRatings, numUsers)
>>> round(CFRatingPrediction(863, 1431, trUserRatings, friends), 3)
3.248
>>> friends = kNearestNeighbors(863, trUserRatings, 76)
>>> round(CFMMRatingPrediction(863, 1431, trUserRatings, trMovieRatings, friends), 3)
3.107
>>> friends = kNearestNeighbors(863, trUserRatings, numUsers)
>>> round(CFMMRatingPrediction(863, 1431, trUserRatings, trMovieRatings, friends), 3)
3.124
>>> friends = kNearestNeighbors(761, trUserRatings, numUsers)
>>> round(CFRatingPrediction(761, 1287, trUserRatings, friends), 3)
1.638
>>> round(CFMMRatingPrediction(761, 1287, trUserRatings, trMovieRatings, friends), 3)
1.819
>>> friends = []
>>> round(CFRatingPrediction(761, 1287, trUserRatings, friends), 3)
2.977
>>> round(CFMMRatingPrediction(761, 1287, trUserRatings, trMovieRatings, friends), 3)
2.489
>>> friends = kNearestNeighbors(889, trUserRatings, numUsers)
>>> [i for i in range(len(friends)-1) if friends[i][1] - friends[i+1][1] > 0.01] 
[25, 28, 30, 31, 35, 37, 42, 51, 59, 97, 776, 831, 840, 844, 850, 851, 858, 862, 863, 864, 865, 874, 878, 879, 880, 882, 883, 887, 890, 891, 892, 893, 901, 905, 906, 908, 909]
>>> round(CFRatingPrediction(889, 523, trUserRatings, friends[:26]), 3)
4.561
>>> round(CFMMRatingPrediction(889, 523, trUserRatings, trMovieRatings, friends[:26]), 3)
4.272
>>> round(CFRatingPrediction(889, 523, trUserRatings, friends[:777]), 3)
4.008
>>> round(CFMMRatingPrediction(889, 523, trUserRatings, trMovieRatings, friends[:777]), 3)
3.995
'''
#-------------------------------------------------------
from project2Phase2a import *
#-------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
