from math import factorial
#Find the sum of the digits in the number 100!
xFact = factorial(100)
sumOfDigits = 0

while(xFact > 0):
	sumOfDigits += xFact % 10
	xFact /= 10
	round(xFact, 0)
	print(str(xFact)+"\n")

print("The sum of the digits for 100! is: "+str(sumOfDigits)+"\nFactorial: "+str(xFact))