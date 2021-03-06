####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PHASE 1 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################

import math
import random

# Reads information about users from the file u.user. This information is stored as a list dictionaries and returned.
# Each dictionary has keys "age", "gender", "occupation", and "zip". The dictionary for user i is stored in slot i-1.
def createUserList():
	fusers = open("u.user", "r")

	userList = []
	for line in fusers:
		userInfo = line.strip().split("|")
		userList.append({"age": int(userInfo[1]), "gender": userInfo[2], "occupation": userInfo[3], "zip": userInfo[4]})

	fusers.close()
	return userList

# Reads information about users from the file u.item. This information is stored as a list dictionaries and returned.
# Each dictionary has keys "title", "release date", "video release date", "IMDB url", and "genre". The dictionary for movie i
# is stored in slot i-1.
def createMovieList():
	fitems = open("u.item", "r")
	itemList = []
	for line in fitems:
		itemInfo = line.strip().split("|")
		itemList.append({"title": itemInfo[1], "release date": itemInfo[2], "video release date": itemInfo[3], "IMDB url": itemInfo[4],
					 "genre": map(int, itemInfo[5:])})

	fitems.close()
	return itemList

# This function reads the file u.genre for the names of genres.
def createGenreList():
	f = open("u.genre", "r")

	L = []
	for line in f:
		L.append(line.split("|")[0])

	f.close()
	return L


# Read ratings from a file u.data. Each rating line consisting of a user, movie, and rating are turned into a length-3 int tuple.
# A list of 100,000 such ratings is returned. The timestamps that appear in each rating are ignored. 
def readRatings():
	ratings = []
	f = open("u.data", "r")

	for line in f:
		data = tuple([int(x) for x in line.split()][:3])
		ratings.append(data)

	f.close()
	return ratings
   
# This function is given a bunch of ratings in the form of a list of (user, movie, rating)-tuple.
# It then creates two data structures, one from the point of view of users and one from the point of view of movies. 
# In addition, the function takes the number of users and movies as parameters and uses these to appopriately initialize
# the rating lists.
def createRatingsDataStructure(numUsers, numItems, ratingTuples):
	# Initialization of rating lists
	ratingsList1 = []
	ratingsList2 = []
	for i in range(numUsers):
		ratingsList1.append({})

	for i in range(numItems):
		ratingsList2.append({})

	# Read each line in the rating file and store it in each 
	# of the two data structures
	for rating in ratingTuples:
		ratingsList1[rating[0]-1][rating[1]] = rating[2]
		ratingsList2[rating[1]-1][rating[0]] = rating[2]
	
	return [ratingsList1, ratingsList2]


# returns the mean rating provided by user with id u. The second argument is 
# the ratings list containing ratings per user.
def meanUserRating(u, userRatings):
	return sum(userRatings[u-1].values())/float(len(userRatings[u-1]))

# returns the mean rating received by a movie with id u. The second argument is 
# the ratings list containing ratings per movie. 
def meanMovieRating(u, movieRatings):
	return sum(movieRatings[u-1].values())/float(len(movieRatings[u-1]))

#----------------- FUNCTIONS FOR EVALUATION -----------------------------------------------------
# This function takes a list of raw ratings in the form of (user, movie, rating)-tuples.
# In addition it takes the percentage of the raw ratings that should be placed in the test
# set of ratings. The test set is obtained by randomly selecting the given percent of the raw ratings.
# The remaining unselected ratings are returned as the training set. The test set is a list with
# each element having the form (user, movie, rating). The training set has a similar
# form. it is expected that the user will call this function as 
#             [trainingSet, testSet] = partitionRatings(rawRatings, testPercent)
def partitionRatings(rawRatings, testPercent):
	# Create a random sample of 20,000 integers from the range [0, 100,000) 
	hidden = random.sample(range(len(rawRatings)), int(len(rawRatings)*testPercent/100.0))
	# Store this sample in a dictionary
	hiddenDict = {}
	for i in hidden:
		hiddenDict[i] = 0

	testSet = []
	trainingSet = []
	for i in range(len(rawRatings)):
		if i in hiddenDict:
			testSet.append(rawRatings[i])
		else:
			trainingSet.append(rawRatings[i])
	print "Created a training and test set..."

	return [trainingSet, testSet]

def rmse(actualRatings, predictedRatings):
	sumSquares = 0
	for i in range(len(actualRatings)):
		sumSquares = (actualRatings[i] - predictedRatings[i])**2 + sumSquares

	return math.sqrt(sumSquares/float(len(actualRatings)))
#------------ END EVALUATION FUNCTIONS -------------------------------

#------------ SIMPLE PREDICTION ALGORITHMS ----------------------------

def randomPrediction(user, movie):
	return random.randint(1, 5)

def meanUserRatingPrediction(user, movie, userRatings):
	if userRatings[user-1]:
		return meanUserRating(user, userRatings)
	else:
		return random.randint(1, 5)

def meanMovieRatingPrediction(user, movie, movieRatings):
	if movieRatings[movie-1]:
		return meanMovieRating(movie, movieRatings)
	else:
		return random.randint(1, 5)

def meanRatingPrediction(user, movie, userRatings, movieRatings):
	if userRatings[user-1] and movieRatings[movie-1]:
		return (0.5*meanUserRating(user, userRatings) + 0.5*meanMovieRating(movie, movieRatings))
	elif userRatings[user-1]:
		return meanUserRating(user, userRatings)
	elif movieRatings[movie-1]:
		return meanMovieRating(movie, movieRatings)
	else:
		return random.randint(1, 5)

#------------ END: SIMPLE PREDICTION ALGORITHMS ----------------------------

####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PHASE 2 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################





#####################################################################
# Similarity 
# Use userRatings from training set, namely use trUserRatings set
###################################################################
def similarity(u, v, userRatings):
	#get mean movie ratings of u and v
	uMeanUserRating = meanUserRating(u, userRatings)
	vMeanUserRating = meanUserRating(v, userRatings)

	nominatorSum = 0
	uDenominatorSum = 0
	vDenominatorSum = 0

	uMovieList = [x for x in userRatings[u-1]]
	# print uMovieList
	vMovieList = [x for x in userRatings[v-1]]

	for umovie in uMovieList:
		if umovie in vMovieList:
			r_u = userRatings[u-1][umovie]
			r_v = userRatings[v-1][umovie]
			nominatorSum = nominatorSum + (uMeanUserRating - r_u)*(vMeanUserRating - r_v)
			uDenominatorSum = uDenominatorSum + (uMeanUserRating - r_u)**2
			vDenominatorSum = vDenominatorSum + (vMeanUserRating - r_v)**2
	
	if uDenominatorSum == 0 or vDenominatorSum == 0:
		# print "denominator is 0"
		return 0.0
	else:
		return float(nominatorSum)/math.sqrt( uDenominatorSum*vDenominatorSum )


# print similarity(1,166,trUserRatings)


#####################################################################
# Nearest Neighbors
#####################################################################
def swap(l):
	l[0],l[1] = l[1],l[0]
	return tuple(l)
	

def kNearestNeighbors(u, userRatings,k):
	nearestNeighborList = []
	v_idx = 0
	while v_idx < len(trUserRatings):
		if not v_idx == u:
			nearestNeighborList.append( [ similarity(u, v_idx, userRatings)  , v_idx ] )
		v_idx += 1
	nearestNeighborList =  sorted(nearestNeighborList, reverse = True)
	# print nearestNeighborList[:21]
	nearestNeighborList = [swap(x) for x in nearestNeighborList]

	return nearestNeighborList[:k+1]

# def kNearestNeighbors(u, userRatings, k):
# 	nearestNeighborList = NearestNeighbors(u, userRatings)
# 	return nearestNeighborList[::k+1]

# print kNearestNeighbors(100,trUserRatings,10)

#get the friends of user u
def friends(u, userRatings,k):
	friendsList = [x[0] for x in kNearestNeighbors(u, userRatings, k)]
	return friendsList


def CFRatingPrediction(u, m, userRatings, friends):
	nominatorSum = 0.0
	denominatorSum = 0.0
	for j in friends:
		if m in userRatings[j-1]:
			r_jm = meanUserRating(j, userRatings)
			# print "Set Number=",j," ", userRatings[j-1]
			r_j =  userRatings[j-1][m]
			nominatorSum = nominatorSum + (r_jm - r_j)*similarity(u, j, userRatings)
			denominatorSum = denominatorSum + abs(similarity(u, j, userRatings))
	# if m in userRatings[j-1]:
	# 	r_u = userRatings[u-1][m]
	# else:
	# 	r_u = 0
	r_u = meanUserRating(u, userRatings)

	if denominatorSum == 0:
		return r_u

	return r_u + nominatorSum/denominatorSum



def CFMMRatingPrediction(u, m, userRatings, movieRatings, friends):
	p_um = CFRatingPrediction(u,m,userRatings,friends)
	mean_m = meanMovieRating(m, movieRatings)
	return (p_um+mean_m)/2.0








####################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN PROGRAM
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####################################################################

# Read and store in data structures
userList = createUserList()
numUsers = len(userList)
movieList = createMovieList()
numMovies = len(movieList)
rawRatings = readRatings()


# Create training and testing set
trainingSet = rawRatings[:80000]
testingSet = rawRatings[80000:]



# ------------------------------------Trainig Set -------------------------------------------#


[trUserRatings, trMovieRatings] = createRatingsDataStructure(numUsers, numMovies, trainingSet)

# Call each of the 4 rating prediction algorithms
trRandomRatings = [randomPrediction(x[0], x[1]) for x in trainingSet]
trMeanMovieRatings = [meanMovieRatingPrediction(x[0], x[1], trMovieRatings) for x in trainingSet]
trMeanUserRatings = [meanUserRatingPrediction(x[0], x[1], trUserRatings) for x in trainingSet]
trMeanRatings = [meanRatingPrediction(x[0], x[1], trUserRatings, trMovieRatings) for x in trainingSet]

# ------------------------------------Testing Set -------------------------------------------#

# Call each of the 4 rating prediction algorithms
testingRandomRatings = [randomPrediction(x[0], x[1]) for x in testingSet]
testingMeanMovieRatings = [meanMovieRatingPrediction(x[0], x[1], trMovieRatings) for x in testingSet]
testingMeanUserRatings = [meanUserRatingPrediction(x[0], x[1], trUserRatings) for x in testingSet]
testingMeanRatings = [meanRatingPrediction(x[0], x[1], trUserRatings, trMovieRatings) for x in testingSet]



friends = friends(100, trUserRatings,100)
print "I run friends function"

print CFRatingPrediction(863, 1431, trUserRatings, friends)
print "I passed CFRatingPrediction function"
print CFMMRatingPrediction(100,520, trUserRatings,trMovieRatings,friends)
print "how about this?"



