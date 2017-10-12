#LabSheet3 Exercise 1 - Q1 DONE - Q2
#All inputs and outputs must be integers - functions need same name.
#Include Docstrings as well as comments.

def personalAllowance(yearlySalary):
	pAllowance = 11500
	pAllowanceMinus = 0	#money we take away from the personal allowance

	#Checks if salary is over £100,000 and then takes £1 for every £2 over that
	if yearlySalary > 100000:
		yearlySalary -= 100000	#since we only need to work with anything above £100,000
		#Checks for odd numbers and makes them even so we don't have an uneven number when dividing yearlySalary by 2
		if (yearlySalary % 2) == 1:
			yearlySalary -= 1
		pAllowanceMinus = yearlySalary/2	#since for every £2 we take away £1 from the allowance
		pAllowance -= pAllowanceMinus
	if pAllowance < 0:	#So we don't have a negative personal allowance
		pAllowance = 0

	return(pAllowance)

def incomeTax(yearlySalary):
	yearlySalary -= personalAllowance(yearlySalary)	#Since we are taxed after personal allowance is given
	taxBill = 0
	#Checks salary(after personal allowance) and takes percentage away in correlation to the yearly salary.

	if yearlySalary >= 150000:
		taxBill = yearlySalary/100 * 20
		yearlySalary -= yearlySalary/100 * 20
		taxBill += yearlySalary/100 * 40
		yearlySalary -= yearlySalary/100 * 40
		taxBill += yearlySalary/100 * 5
		yearlySalary -= yearlySalary/100 * 5
	elif yearlySalary > 32000:
		taxBill = yearlySalary/100 * 20
		yearlySalary -= yearlySalary/100 * 20
		yearlySalary -= 32000
		taxBill += yearlySalary/100 * 40
		yearlySalary -= yearlySalary/100 * 40
	else:
		taxBill = yearlySalary/100 * 20
		yearlySalary -= yearlySalary/100 * 20

	#if yearlySalary <= 32000:
	#	taxBill = (yearlySalary/100 * 20)	#taking 20% tax
	#elif yearlySalary < 150000:
	#	taxBill = (yearlySalary/100 * 40)	#taking 40% tax on anything below 150,000 and above 32000
	#else:
	#	taxBill = (yearlySalary/100 * 45)	#anything £150000 or above gets a 45% tax

	if taxBill < 0:
		taxBill = 0

	#taxBill = int(taxBill)
	print(str(taxBill))	#testing output

	return(taxBill)