from math import factorial
#Find the sum of the digits in the number 100!
xFact = str(factorial(100))
sumOfDigits = 0
xFactArray = list(xFact)	#puts each number in 100! into an array of each character
print(str(xFactArray))	#test

for i in xFactArray:
	sumOfDigits += int(i)

print("\nFactorial: "+str(xFact))	#test
print("\nThe sum of the digits for 100! is: "+str(sumOfDigits))