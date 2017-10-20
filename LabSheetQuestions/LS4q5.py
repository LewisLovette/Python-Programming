#12/12 table printed like it would look if you drew it - use nested loops.
def timesTable():
	timesTop = 0
	timesLeft = 0
	multi = 0
	#1-12 at top
	while timesTop <= 24:
		if timesTop <= 12:	#1-12 on top row
			if timesTop == 0:
				print("x | ", end = "")
			print(str(timesTop)+"\t", end="")
			
		if timesTop >= 12:	#------ below top row
			if timesTop == 12:
				print("\n", end = "")
			print("--------", end="")
		timesTop += 1

	timesTop = 0
	#rest of the table
	while timesTop <= 12:
		print("\n"+str(timesTop)+" | ", end="")
		while timesLeft <= 12:
			multi = timesTop*timesLeft
			print(str(multi)+"\t", end="")
			timesLeft += 1
		
		timesTop += 1
		timesLeft = 0
	
	return(0)

timesTable()