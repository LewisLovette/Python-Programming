#24hr clock to 12hr converter
#5.a) Checking user input and
wrongInputLoop = 0
while wrongInputLoop == 0:
	#Make it so that it checks the type of input before it asks for th next input?
	hourInput = raw_input("What is hour (24hr notation): ")
	minuteInput = raw_input("What is the minute? ")
	#if hour.isfloat() or minute.isfloat():
	#	print("Error, enter a 1 or 2 digit numer without floating points.")
	if hourInput.isdigit() and minuteInput.isdigit():
		#Converting Inputs into useable ints (otherwise they would cause error when comparing.)
		hour = int(hourInput)
		minute = int(minuteInput)

		if hour > 24 or hour < 0:
			print("That is not a valid time!")
		elif minute > 60 or minute < 0:
			print("That is not a valid time!")
		elif hour > 12:
			hour -= 12
			print("That's "+str(hour)+":"+str(minute)+"pm")
		else:
			print("That's "+str(hour)+":"+str(minute)+"am")
		wrongInputLoop = 1
	else:
		print("Error, please enter a 1 or 2 digit number, no floating point.\n-------------------------------")

print("Program End.")