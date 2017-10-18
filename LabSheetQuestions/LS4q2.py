#Function that takes input between 1-12 - then print * tables for that number from 1-12

def times(numToMulti):
	x = 1
	if int(numToMulti) <= 12 and int(numToMulti) > 0:
		while x <= 12:
			tot = int(numToMulti) * x
			print(str(x)+" x "+numToMulti+" = "+str(tot))

			x +=1 
	else:
		print("Number not valid.")

	return(0)

times(input("Input the Number you want to sho the times tables for: "))