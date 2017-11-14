#Q6 Download a book as a text file from http://www.textfiles.com/etext/. This website hosts books out
#of copyright (so it is legal to download for free). This task works best with a long book. Alternatively,
#there are already three books to choose from in the Codio Week 7 Unit (Books directory)
#The aim of this question is to have Python generate artificial sentences of grammatically correct English.
#The basic steps are below. Hint: start with just the first few lines of the book as a test.
#(a) Open the file containing a book, read the contents into a string and then close it. Remember that
#you should use a try-finally statement to ensure the file closes properly.
#(b) Split the string into a list of words.
#(c) From this create a dictionary: each key should be a word that appears in the book; each value
#should be a list of the words which follow the key-word in the book.
#(d) Have Python create a random English sentence by: selecting a random word to start with; then
#adding on one of the words which follow it in the text; and so on for a set amount of words.

import random as rand
import sys

f = open("PeterPan.txt", "r")
peterPan = f.read().split()
f.close()

dictionary = {}
count = 0

for word in peterPan:
	if count < len(peterPan) - 1:
		if word in dictionary:
			dictionary[word] += peterPan[count + 1]+" "
		else:
			dictionary[word] = peterPan[count + 1]+" "
	count += 1

randNum = rand.randint(5, 15)	#for length of poem

randWordNum = rand.randint(0, len(peterPan) - 1)
randWord = peterPan[randWordNum]
counter = 0

while counter != randNum:
	mostCommonMaybe = 0
	mostCommon = 0

	if counter <= 0:
		randWordSplit = dictionary[randWord].split()
	else:
		randWordSplit = dictionary[mostCommonWord].split()

	#messing around
	if len(randWordSplit) > 5:
		mostCommonWord = randWordSplit[5]
	if len(randWordSplit) > 4:
		mostCommonWord = randWordSplit[4]
	if len(randWordSplit) > 3:
		mostCommonWord = randWordSplit[3]
	if len(randWordSplit) > 2:
		mostCommonWord = randWordSplit[2]
	if len(randWordSplit) > 1:
		mostCommonWord = randWordSplit[1]
	else:
		mostCommonWord = randWordSplit[0]
	#for i in randWordSplit:	#see most popular word
	#	mostCommonMaybe = randWordSplit.count(i)
	#	if mostCommon == 0 and i != "children":
	#		mostCommon = 1
	#		mostCommonWord = i
	#	if mostCommonMaybe > mostCommon and i != "children":
	#		mostCommon = mostCommonMaybe
	#		mostCommonWord = i

	print(mostCommonWord, end=" ")

	counter += 1


