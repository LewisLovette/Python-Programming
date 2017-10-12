#24hr clock to 12hr converter
#5.b)	Rounding minute to the nearest 15
#-----To do-----
#When minute is = 0, make it print '00' so that it looks like a normal clock. 
print("Rounding to the closest 15 min.")
#Loop so that if incorrect input is put in, the program will bascially start from the beggining.
wrongInputLoop = 0
while wrongInputLoop == 0:
	#Getting user input
	hourInput = input("What is hour (24hr notation): ")
	minuteInput = input("What is the minute? ")

	#Checking that the user inputted an int.
	if hourInput.isdigit() and minuteInput.isdigit():
		#Converting Inputs into useable ints (otherwise they would cause error when comparing.)
		hour = int(hourInput)
		minute = int(minuteInput)

		#Rounding to closes 15
		#Done in order so that if it's not caught but is caught by the next if then it has to be the number it's
		#rounded to as it wasn't caught by the last one -effectively gives a number a 15 min range to be rounded to it's
		#closest 15 mins
		if minute > 60:
			minute = minute
			#so if it is not a valid number it will be caught during next if statement section
		elif (60 - minute) < 8:	#minute is greater than 52.5 so we round to 60 (or add 1 to hour and make minute 0)
			hour += 1	#rounding up to 60 so +1 to hour and minute = 00
			minute = 00
		elif (60 - minute) < 23:	#this means that minute is greater than 37.5 (but didn't get caught by first if)
			minute = 45					#so it means that if it is greater than 37.5 it will have to be rounded to 45.
		elif (60 - minute) < 38:
			minute = 30
		elif (60 - minute) < 53:
			minute = 15
		else:
			minute = 00
		
		#Checking if time is valid then converting to 12hr clock
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