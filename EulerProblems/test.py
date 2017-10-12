x = 1
fibX = 0
fibY = 1
fibZ = fibX + fibY
while x > 0:
	fibZ = fibX + fibY
	print(fibZ)
	fibX = fibZ + fibY
	print(fibX)
	fibY = fibX + fibZ
	print(fibY)
	