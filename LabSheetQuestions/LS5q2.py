#Raising Exceptions: Copy out the code from Day.py in the Codio Week 5 Unit. Extend it so that it
#will raise a TypeError if the input n is not of type int. Can you think of any other checks needed to
#ensure n is valid?

def numToDay(n):
	"""Input is int between 1-7. Output is corresponding day as 3 letter string"""
	Mtup = ("","Mon","Tue","Wed","Thu","Fri","Sat","Sun")
	if type(n) != int:
		raise TypeError("Input an integer!")
	elif n>7 or n<=0:
		raise ValueError("There are only 7 days!")
	else:
		return(Mtup[n])

#Comment out to test specific ones
print(numToDay(4))
print(numToDay(-3))
print(numToDay(8))
print("")
print(numToDay("8"))