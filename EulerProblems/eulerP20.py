#Find the sum of the digits in the number 100!
x = 99 #since we start on 100
sum100 = 100
sumOfDigits = 0

while x != 1:
	sum100 *= x
	print(str(sum100)+" - "+str(x))
	x -= 1

x = 100

while x != 0:
	sumOfDigits += sum100 % 10
	sum100 /= 10
	x -= 1

print("The sum of digits for 100! is: "+str(sumOfDigits))