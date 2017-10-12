money = 10000
years = 0
while years < 5:
	interest = input("What is the interest rate? ")
	yearInput = input("How many years? ")
	years += int(yearInput)
	money *= (1+float(interest)/100)**float(yearInput)

interest = money - 10000
print("Your overall money after 5 years is: "+"{0:.2f}".format(float(money))+
	"\nWhich is "+"{0:.2f}".format(float(interest))+" ontop of original investment")