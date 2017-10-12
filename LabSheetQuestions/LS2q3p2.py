spend = float(input("How much did you spend? "))
student = raw_input("Are you a student? y/n ")

if student == "y":
	spend -= (spend/5)
else:
	uniStaff = raw_input("Are you apart of the University Staff? y/n ")
	if uniStaff == "y":
		spend -= (spend/10)

com121 = raw_input("Are you involved in 121COM? y/n ")
if com121 == "y":
	spend -= (spend/20)

print("Your bill is: "+str(spend)+" GBP")
