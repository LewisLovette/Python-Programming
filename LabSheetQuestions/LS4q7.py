#Example
#randList = list(range(0,10))	#creates an array from range 0-10 (so [0,1,2,3,4,5,6,7,8,9])

#Sieve of Eratothenes for 0-500 (primes)
def sieveOfErathothenes(n):
	#not my code
	not_prime = []
	prime = []
	#As the second 'for' loop puts every multiple of a prime into not_prime it means that if a number 
	#isn't in not_prime (such as 2 for first loop) then it is a prime - this then repeats (so later 
	#multiples of the prime we know not to be prime) and since every non-prime number is a multiple of 
	#a prime we can append the first instance of a number that is NOT in not_prime as it means that it has
	#to be a prime number. -pretty juicy method tbh.
	for i in range(2, n+1):
		if i not in not_prime:	
									
			prime.append(i)
			for j in range(i*i, n+1, i):  #checks for range of i*i to n+1 in increments of i then adds it to not_prime
				not_prime.append(j)

	print(str(prime))
	#end

	#Misc failed test code.
	#possiblePrimes = list(range(2,500))
	#primeCheck = 2
	#for i in possiblePrimes:
	#	while primeCheck < i:
	#		if i % primeCheck == 0:
	#			del possiblePrimes[i]
	#		primeCheck += 1
	#		
	#print(str(possiblePrimes))


sieveOfErathothenes(500)