#! /usr/bin/python
# created by: echris
# reads in the text file naem is specified on the command lie3n
# and reports the number of lines and words

import sys

#Always place the function first before the actual call script
def checkline():
	#get our global variables been declared
	global line,wordcount,letters

	#for each line received, convert to list by splitting result
	word = line.split()

	#get the total number of words
	wordcount += len(word)
	
	#use the split words and join them as single words
	letter = "".join(word)

	#then convert them to list and count total
	countletter = len(list(letter))

	#add the result to last recorded value
	letters += countletter


#Main execution script
wordcount = letters = 0
f = open(sys.argv[1]) #sys.argv[0] is the scanlist.py 
flines = f.readlines()
linecount = len(flines) #count the total line

#for each line of values, call checkline
for line in flines:
	checkline()
print "Total line Numbers: " + str(linecount)
print "Total number of Words: " + str(wordcount)
print "Total number of Letters: " + str(letters)

