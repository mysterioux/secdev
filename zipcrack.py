#! /usr/bin/python
# created by: echris
# filename: zipcrack.py
# description: bypassing passwords in zipfiles
# note: make sure your zip file is in the same directory as this script

import zipfile
import os

def extractFile(zfile,password):		
			try:
				zfile.extractall(pwd=password)
				return password
			#silently overlook the error
			except:
				return

def userChoice(option):
	#menu - To crack zipfile password
	if option == 1:
	  #Perform action for cracking password
		print "Performing cracking..."	
		dictname = "dictionary.txt"
		zname = raw_input("Name of zip file: ")

		#strip off .zip if exist
		if ".zip" in zname:
			zname = zname.split(".")[0] + ".zip"
		else:
			zname = zname + ".zip"
		
		#Checks to see if file ever existed
		if not os.path.isfile(dictname):
			print "Sorry! The dictionary File: \"" + dictname + "\" is missing \n"
			exit(0)

		elif not os.path.isfile(zname):
			print zname + " does not exist \n"
			exit(0)

		else:
			zfile = zipfile.ZipFile(zname)
			passfile = open(dictname,'r')

			for line in passfile.readlines():
				password = line.strip("\n")
				guess = extractFile(zfile,password)
				if guess:
					print "\nFile Unzipped Successful"
					print "Password found : " + password + "\n"
					exit(0)
			
	#menu - to enter password of file
	elif option == 2:

		filename = raw_input("Enter name of file (without the extension): ")
		password = raw_input("Enter supposed password: ")
		filename = filename + ".zip"
		
		if not os.path.isfile(filename):
			print "Sorry, Cannot find " + filename
			exit(0)
		else:
			zfile = zipfile.ZipFile(filename)
			try:
				zfile.extractall(pwd=password)
				print "Extraction Completed"
			except Exception, e:
				print "\n"
				print "Error extacting: " + filename
				print "Error details: "+ str(e)

	#menu - to validate the existence of unzipped file
	elif option == 3:
		filename = raw_input("Enter name of folder: ")

		if not os.path.isdir(filename):
			print "No such folder exist"
			exit(0)
		else:
			print "Yes! a folder with the name: " + filename + " exist"

  #To exist program
	elif option == 4:
		print "Thanks for visiting - Later dude"
		exit(0)

	#safe guard for smartdudes
	else: 
		print "Hey! Hope you ain't trying to be smart?"
		exit(0)
	return

def main():
	print "-"*50
	print "Welcome to ZipCracking System"
	print "-"*50
	print "Make a choice:"
	print "[1] - Crack Zip Password"
	print "[2] - Unzip Passworded File"
	print "[3] - Validate folder"
	print "[4] - Exit"
	print "*"*70
	print "Note: Make sure your zip file is in the same directory as this script"
	print "*"*70
	print "\n"

	option = int(raw_input("Select a choice: "))
	userChoice(option)
	

if __name__ == "__main__":
	main()


