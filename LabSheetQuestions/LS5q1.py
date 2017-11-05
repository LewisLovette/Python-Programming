#Handling Exceptions: Write a function called add which takes two inputs a and b, then outputs their
#sum a+b. If the sum is not defined for the inputs then the function should catch the TypeError and
#instead print a message to the user and return None.

def add(a,b):
	try:
		a = int(a)
		b = int(b)
		sumTest = a+b
		return(print(sumTest))
	except TypeError:
		print("You have a TypeError, insert integers.")
		return(0)
	except ValueError:
		print("You have a ValueError, insert integers.")
		return(0)

add(input("a: "),input("b: "))