#24hr clock to 12hr converter
hour = input("What is hour (24hr notation): ")
minute = input("What is the minute? ")

if hour > 24 or hour < 0:
	print("That is not a valid time!")
elif minute > 60 or minute < 0:
	print("That is not a valid time!")
elif hour > 12:
	hour -= 12
	print("That's "+str(hour)+":"+str(minute)+"pm")
else:
	print("That's "+str(hour)+":"+str(minute)+"am")
