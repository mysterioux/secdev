#! /usr/bin/python
# created by: echris
# reads in the text file naem is specified on the command lie3n
# and reports the number of lines and words

import sys

#Always place the function first before the actual call script
def checkline():
	global line
	global wordcount

	word = line.split()
	wordcount += len(word)

#Main execution script
wordcount = 0
f = open(sys.argv[1]) #sys.argv[0] is the scanlist.py 
flines = f.readlines()
linecount = len(flines)
for line in flines:
	checkline()
print linecount,wordcount


#how to run
#install python27
#make sure its in your PATH system
#open a command prompt
#type: python scanlist.py sample.txt
#where sample.txt could be anything