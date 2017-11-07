#'Devise simple and more complex approach to recognize what the user(s) has typed.'
#Get input, split it up, look for keyword - if keyword then do whatever.
#order would be #action# then #looking for# for example, "Find pizza near me"
#out want and need? eg, want = 'where' and need = 'food'?

#TO DO -------------------------
#Run 'want' through list of keywords to ckeck if they're relevant
#Recognize more what user is talking about (if it is or isn't relevant)
#Make this a function that can search for post codes/addresses
#place into while loop so that if the subject is relevant, it makeks sure it takes data for where to find the 'want'
#-------------------------------

def removeDuplicates(listToRemove):
	"""Takes list as input and outputs the list without duplicates"""
	duplicateCount = 0	#number of 'duplicateCount' == amount of that string.
	indexPosition = 0
	for i in listToRemove:
		for j in listToRemove:	#checks each index against eachother
			if i == j:
				duplicateCount += 1
				if duplicateCount > 1:	#if duplicateCount > 1 then it means there is more than 1 of that string in the array
					del listToRemove[indexPosition]
		indexPosition += 1
		duplicateCount = 0

	return(listToRemove)

def userInputRecognition(userInput):
	"""Takes user input as an array and returns 'want' and 'where' keywords"""
	
	whereKeywords = ["near", "in", "local", "closest", "nearest"]
	where = []
	want = []
	while len(where) <= 0:
		userInputCount = 0	#To get array positions in different places to the one we are checking
		for i in userInput:
			for j in whereKeywords:
				if i == j:
					where.append(i)
			
			#Words where the 'want' is generally before the 'where'
			if (i == "food" or i == "near" or i == "places" or (i == "to" and userInput[userInputCount+1] == "me")) and userInputCount-1 >= 0:
				if i == "to":	#for cases where the 'where' is before the 'want' but isn't activated eg. "Closes dominos to me"
					where.append("near")										#will still allow this to pick up 'want' and 'where'
					where.append(userInput[userInputCount+1])
				want.append(userInput[userInputCount-1])
				if i == "places":
					want.append(i)

			#for words where the 'want' is generally after the 'where'
			if (i == "near" or i == "in" or i == "local" or i == "closest" or i == "nearest") and len(userInput) >= userInputCount + 1:	#specific cases
				if i == "local" or i == "closest" or i == "nearest":	#for 'wants' not 'where' (these should be in keyword array too)
					want.append(userInput[userInputCount+1])
				else:
					where.append(userInput[userInputCount+1])
			
			userInputCount += 1	
		if len(where) <= 0:
			userInput = input("Enter where you want to find this: ").lower().split()
	#------------------------Change words with same meaning to general use word so less cases need to be worked on------------------
	#------------------------Remove Duplicates if needed----------------------------------------------------------------------------
	removeDuplicates(where)
	removeDuplicates(want)

	print("Want: "+str(want)+"\tWhere: "+str(where))
		


	if len(want) > 0 and len(where) > 0:
		return(want, where)
	else:
		return(print("I am not familiar with this subject"))	#filler for unfimiliar subject matter

#Input needs to be set to lower and split.
print(userInputRecognition(input("What do you need help with? ").lower().split()))