#calculate mean, median and mode averages and standard deviation using standard library. 
#Then add the num 28 and recalculate
def meanFunc(mean, randList):
	
	for i in range(len(randList)):	#checking i for the index of the length of randList (smooth)
		mean += randList[i]
	mean /= len(randList)

	return(mean)
def medianFunc(median, randList):
	#Find the middle number of list, if it's even it will go to the len(half) + 1.
	median = randList[int(len(randList)/2)]

	return(median)

def modeAvgFunc(modeAverage, randList):


	return(modeAverage)

def stanDeviationFun(stanDeviation, randList):

	return(stanDeviation)
	
randList = [1,2,3,3,3,4,4,5,6,7,8,9,10, 28]

mean = meanFunc(0, randList)
median = medianFunc(0, randList)
modeAverage = 0
stanDeviation = 0

print("Mean: "+str(mean)+"\nMedian: "+str(median)+"\nMode Average: "+str(modeAverage)+
	"\nStandard Deviation: "+str(stanDeviation))