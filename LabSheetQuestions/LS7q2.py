#An anagram of a word is another word formed from the same letters. For example, parse and spare are
#anagrams. Create a dictionary where the keys are tuples of letters and the values anagrams they create.
#Hints: you can extract the letters from a string by converting to a list and there is a list method to put
#them into alphabetical order! In Scrabble a player receives a bonus if they create an 8 letter word. Use
#your dictionary to find out which group of 8 letters can create the most words.
import pickle as pkl 
f = open("PickledWordList.pkl", "rb")
wordList = pkl.load(f)
f.close

dictionary = {}

for word in wordList:
	letters = list(word)
	letters.sort()
	letters = tuple(letters)	#Since python doesn't let you use mutable types as keys

	if letters in dictionary:
		dictionary[letters] += word+", "
	else:
		dictionary[letters] = word+", "


rand = input("Search for anagrams: ")
rand = list(rand)
rand.sort()
rand = tuple(rand)

if rand in dictionary:
	print(str(dictionary[rand]))
else:
	print("This word is not in the dictionary.")


