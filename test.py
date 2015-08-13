import sys
import os

if len(sys.argv) == 2:
	filename = sys.argv[1]
	#find out if the file path exist
	if not os.path.isfile(filename):
		print "[-] Sorry! The file " + filename + " cannot be found"
		print "[-] Kindly check that it exist"
		exit(0)
	#check to see if user has permission to read file
	if not os.access(filename,os.R_OK ):
		print "You don't have permission to read " + filename
		exit(0)
	print "[+] Reading vulnerabilities from: " + filename