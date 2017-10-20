#Write a function wordFrequency whose input is a sentence (string). The function should print out
#a table of words in that sentence. The words should be printed alphabetically with the number of
#occurrences next to it. You will need a loop (you choose which).

def wordFrequency():
	listSplit = input("Enter a sentence: ").split()	#splits the string between spaces
	listSplit.sort()	#origanises the list alphabetically

	#print(str(listSplit))		#test
	
	count = 0
	listPosI = 0
	listPosX = 0
	for i in listSplit:	
		for x in listSplit:	#another for loop so it checks 'i' against the full range of listSplit
			listPosX += 1
			if x == "_No_Duplicate_":	#so that it skips the code for the index if it's a duplicate
				continue
			elif i == x:	#if it's a duplicate(but not the first instance of the word)then it will change its string
				if count != 0:
					listSplit[listPosX-1] = "_No_Duplicate_"
				count += 1	
			

		if listSplit[listPosI] != "_No_Duplicate_":	#if it's not a duplicate then it will print (so it prints once)
			print(str(i+" : "+str(count)))

		count = 0
		listPosX = 0
		listPosI += 1

	#print(str(listSplit))		#test

	return(0)

wordFrequency()