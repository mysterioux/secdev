#! /usr/bin/python
# created by: echris
# filename: crack.py
# description: brute-force a password using dictionary file

import crypt
import os
import sys

#call the function to crack code
def testCrack(crackpass):
	#Get the first two digit of a crypt() hashcode
	salt = crackpass[0:2]

	try:
		#check to see if file dictionary is available
		if not os.path.isfile('dictionary.txt'):
			print "Sorry! cannot find dictionary.txt"
			exit(0)
		else:
		#open file, read each line-by-line
			dictfile = open('dictionary.txt','r')
			for word in dictfile.readlines:
				word = word.strip('\n')

				#encrypt our passwords
				cryptword = crypt.crypt(word,salt)

				#compare our encrpytion with user's
				if cryptword == crackpass:
					print "Password Found: " + word + "\n"
					return

			print "Sorry Password not found"

	except Exception, e:
		print "[-] Error Found: " + str(e)
	return

def main():
	if len(sys.argv) == 2:
		filename = sys.arg[1]
		if not os.path.isfile(filename):
			print filename + " does not exit"
			exit(0)
		elif not os.access(filename, os.R_OK):
			print "Sorry! Permission deny on " + filename
		else:
			# As a safe guard
			try:
				f = open('password.txt','r')
				for passline in f.readlines:
					if ":" in passline:
						#splits into array, and takes the first part
						username = passline.split(':')[0]
						password = passline.split(':')[1].strip(" ")
						print "[+] Cracking Password for: " + username 
						msg = testCrack(password)
						print "Password is: " + msg
			except Exception, e:
				print "[-] Error found: " + str(e)

#calls the main function
if __name__ == '__main__':
	main()
