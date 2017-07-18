#############################################
# Name	 : Suleyman Durgut					#
# Section: A2                      			#
# ID     : 00804224                         #
#############################################

#########################################
# 
#########################################
def createUserList():
	f = open("u.user","r")
	lineList = f.read().split()
	userDict = []
	dictPerUser = {}
	userList = [line.split("|") for line in lineList]

	counter = 0
	for x in userList:

		userDict.append({"age": int(userList[counter][1]) , "gender": userList[counter][2], "occupation": userList[counter][3], "zip": userList[counter][4] })
		counter += 1  

	return userDict


#########################################
# 
#########################################

def createMovieList():
	f = open("u.item","r")
	lineList = f.read().split("\n")
	movieDict = []
	dictPerMovie = {}
	movieList = [line.split("|") for line in lineList]

	counter = 0
	for x in movieList:
		movieDict.append({"title": movieList[counter][1], "release date": movieList[counter][2], "video release date":movieList[counter][3], "IMDB url":movieList[counter][4]})
		idx = 5
		tempGenreList = []
		while idx < len(movieList[counter]):	
			tempGenreList.append( int(movieList[counter][idx]) ) 
			idx +=1
		movieDict[counter].update({"genre": tempGenreList})
		counter +=1

	return movieDict

#########################################
# 
#########################################

def readRatings():
	f = open("u.data","r")
	lineList = f.read().split("\n")
	ratingTuple = []
	ratingList = [line.split() for line in lineList]

	for x in ratingList:
		x = map(int,x)
		if len(x) > 3:
			del x[3]
		ratingTuple.append(tuple(x))

	del ratingTuple[len(ratingTuple)-1]

	# print ratingTuple

	return ratingTuple

#########################################
# 
#########################################

def createRatingsDataStructure(numUsers, numItems, ratingTuples):
	rLu = [{}]*numUsers
	rLm = [{}]*numItems

	# print rLu, len(rLu)


	for x in ratingTuples:
		# print int(x[0])

		if len(rLu[int(x[0])-1]) == 0:
			rLu[int(x[0])-1] = {x[1]:x[2]}
		else:
			rLu[int(x[0])-1].update({x[1]:x[2]})



	for x in ratingTuples:
		if len(rLm[int(x[1])-1]) == 0:
			rLm[int(x[1])-1] = {x[0]:x[2]}
		else:
			rLm[int(x[1])-1].update({x[0]:x[2]})


	return [rLu,rLm]


#########################################
#
#########################################

def createGenreList():
	f = open("u.genre","r")
	L = f.read().split()
	L = [x.split("|") for x in L]
	L = [x[0] for x in L]

	return L

# print createGenreList()


#########################################
# 
#########################################

def meanUserRating(u, rLu):
	ratingTotal = 0.0
	for x in rLu[u-1].items():
		# print x
		ratingTotal = ratingTotal + x[1]

	return ratingTotal/len(rLu[u-1])

#########################################
# 
#########################################

def meanMovieRating(m, rLm):
	ratingTotal = 0.0
	for x in rLm[m-1].items():
		ratingTotal = ratingTotal + x[1]


	return ratingTotal/len(rLm[m-1])


#########################################
# Here comes the prediction algorithms
#########################################

import random

def randomPrediction(u, m):

	return random.randint(1,6)

# print randomPrediction(1,5)


def meanUserRatingPrediction(u, m, userRatings):
	ratingTotal = 0.0
	for x in userRatings[u-1].items():
		# print x
		ratingTotal = ratingTotal + x[1]

	return ratingTotal/len(userRatings[u-1])


def meanMovieRatingPrediction(u, m, movieRatings):
	ratingTotal = 0.0
	for x in movieRatings[m-1].items():
		ratingTotal = ratingTotal + x[1]


	return ratingTotal/len(movieRatings[m-1])

def meanRatingPrediction(u, m, userRatings, movieRatings):
	return [meanUserRatingPrediction(u,m,userRatings), meanMovieRatingPrediction(u,m,movieRatings)]



#########################################
# Evaluation Functions
#########################################

def partitionRatings(rawRatings, testPercent):
	trainingSet = []
	testSet = []
	randomNumberSet = []
	testSetLength = int(len(rawRatings)*testPercent/100.0)
	idx = 0

	while idx < testSetLength:
		randomIdx =  random.randint( 0, len(rawRatings) )
		# testSet.append( rawRatings[randomIdx] )
		if randomIdx not in randomNumberSet:
			randomNumberSet.append(randomIdx)
		else:
			idx -= 1

		idx += 1

	for x in randomNumberSet:
		testSet.append( rawRatings[x] )
	for x in rawRatings:
		if x not in testSet:
			trainingSet.append(x)


	return [trainingSet,testSet]




#########################################
# root mean square calculation for predicted and actual ratings
#########################################


def rmse(actualRatings, predictedRatings):
	# print len(actualRatings), len(predictedRatings)
	# print predictedRatings[1]
	
	import math

	idx = 0
	ratingDiffTotal = 0

	while idx < len(predictedRatings):

		ratingDiffTotal += (actualRatings[idx]-predictedRatings[idx])*(actualRatings[idx]-predictedRatings[idx])
		idx +=1

	return math.sqrt(ratingDiffTotal/float(len(predictedRatings)))

