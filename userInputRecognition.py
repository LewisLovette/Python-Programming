#Code written by Lewis Lovette
#-------------------------------
def postCodeCheck(listToCheck):
	"""Takes input as array of strings, searches for postcode and returns as string"""
	#checks if words match either 'aa# #aa' or 'aa##aa' (for postcodes)
	postcode = "_Empty_"
	listIndexCount = 0

	for i in listToCheck:
		if listIndexCount < len(listToCheck):	#Doesn't go out of index range.
			#checks if it and the next positions length are 3 since more likely to be a postcode - less processing if not true.
			if len(i) == 6:	#For postcodes without spaces
				if i[2].isdigit() == True and i[3].isdigit() == True:	#quick check so doesn't take aslong - then checks the rest
					if i[0].isdigit() == False and i[1].isdigit() == False and i[4].isdigit() == False and i[5].isdigit() == False:
						postcode = i
						break
			elif len(i) == 3 and len(listToCheck[listIndexCount]) == 3:	#for postcodes with spaces	
				if i[0].isdigit() == False and i[1].isdigit() == False and i[2].isdigit() == True:
					aheadCheck = listToCheck[listIndexCount+1]
					if aheadCheck[0].isdigit() == True and aheadCheck[1].isdigit() == False and aheadCheck[2].isdigit() == False:
						postcode = i + listToCheck[listIndexCount+1]
						break
			aheadCheck = "_filler_" 	#setting to 'filler' to stop conflicts on next loop.
			
			listIndexCount += 1

	return(postcode)

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

###MAIN FUNCTION###
def userInputRecognition(userInputPull):
	"""Takes user input as an array and returns 'want', 'where' and 'topic' keywords as separate arrays."""

	userInput = userInputPull.lower().split()

	topicKeywords = ("food", "foods", "restaurant", "restaurants", "spicy", "bland", "plain", "fast", "organic", "refined", "whole", "wholefoods", "gourmet")
	topic = []
	where = []
	want = []

	postCode = postCodeCheck(userInput)
	if postCode != "_Empty_":	#means it's not empty
		where.append(postCode)
	
	
	userInputCount = 0	#To get array positions other than the one in the loop
	for i in userInput:
		#Searching for 'Topic Keywords'
		if i in topicKeywords:
				topic.append(i)

		#Words where the 'want' is generally before the 'where'
		if (i == "food" or i == "near" or i == "places" or i == "restaurant" or i == "restaurants" or (i == "to" and userInput[userInputCount+1] == "me")) and userInputCount-1 >= 0:
			if i == "to":	#for cases where the 'where' is before the 'want' but isn't activated eg. "Closes dominos to me"
				where.append(userInput[userInputCount+1])
			want.append(userInput[userInputCount-1])
			if i == "places":
				want.append(i)

		#for words where the 'want' is generally after the 'where'
		if (i == "near" or i == "in" or i == "local" or i == "closest" or i == "nearest") and len(userInput) >= userInputCount + 1:	#specific cases
			if len(userInput)-1 > userInputCount:
				if i == "local" or i == "closest" or i == "nearest":	#for 'wants' not 'where'
					want.append(userInput[userInputCount+1])
					where.append(i)
				elif i == "in":
					want.append(userInput[userInputCount-1])
					where.append(userInput[userInputCount+1])
				else:
					where.append(userInput[userInputCount+1])
			
		userInputCount += 1	

	#removing any duplicates
	removeDuplicates(topic)
	removeDuplicates(where)
	removeDuplicates(want)

	#testing output
	#print("Want: "+str(want)+"\tWhere: "+str(where)+"\tTopic: "+str(topic))
		
	return(want, where, topic)

#For testing code individually, when running this file
#print(userInputRecognition(input("What do you need help with? ")))

#---------------------------
