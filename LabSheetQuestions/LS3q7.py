#Numbers to words
ones = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tens = ["Ten", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
#hundres = ones + "Hundred"	--- Thousands is the same
num = input("Enter a number between 1 and 9999: ")
numInt = int(num)

if numInt > 1 and numInt <=9999:
	onesStr = str(ones[int(num/1000 -1)]) + " Thousands"

	print(onesStr)