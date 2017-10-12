#Implementing flowcharts from LabSheet 2 q3

#For whatever reason 'input()' doesn't work for strings so 'raw_input()' was used as this doesn't give errors.
#Could be that the interpreter is an older version which doesn't make sense...

languageInput = raw_input("What language do you speak? ")

if languageInput == "English":
	print("Hello")
elif languageInput == "French":
	print("Bonjour")
elif languageInput == "Mandarin":
	print("Ni Hao")
else:
	print("Sorry, I don't speak that language.")

print("Welcome to Coventry")