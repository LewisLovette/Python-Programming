#Ceaser Cipher - move the alphabet by the key
cipherKey = int(input("Enter the number that you want the letters to move: "))
alphabetList = ["a","b","c","d","e","f","g","h","i","j","k","l",
							"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
if cipherKey > 0 and cipherKey <= 26:
	while cipherKey != 100:	#implement exit function
		cipherReverse = cipherKey
		while cipherReverse > 0:
			#append list with the letters, then move the previous letters up + ciperKey spaces
			#then make ones +26 into the spaces going back from the highest and placing it into the
			#cipherKey space (since it'd be that many places forward), take -- from cipher key until it's 0
			#then remove the spaces from 26 onward as they don't need to be used.
			alphabetList[cipherReverse] 

			cipherReverse--


