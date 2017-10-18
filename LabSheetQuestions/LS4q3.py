#list until user types end
def userList():
	userInput = input("Enter what you want in your shopping list: ")
	randList = []

	while userInput.lower() != "end":
		randList.append(userInput)	
		userInput = input("Enter what you want in your shopping list: ")

	print("Your shoping list is: "+str(randList))

	return(0)

userList()