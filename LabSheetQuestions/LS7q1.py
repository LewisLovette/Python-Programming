#Q1 Write a function isThisAWord(S) which takes a string S and returns the appropriate Boolean.
import pickle as pkl 

def isThisAWord(S):
	f = open("PickledWordList.pkl", "rb")
	wordList = pkl.load(f)

	print(len(wordList))

	if S in wordList:
		return True
	else:
		return False

print(isThisAWord(input("Enter a word to see if it exists: ")))