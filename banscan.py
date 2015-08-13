#! /usr/bin/python
# created by: echris
# filename: banscan.py
# description: Scans FTP servers to check if the version has a potential vulnerability

import socket
import sys
import os

def retBanner(ip,port):
	try:
		#create a timeout to connect to remote host
		socket.setdefaulttimeout(2)

		#creates a socket object
		s = socket.socket()

		#connect to the remote host with port number
		s.connect((socket.gethostbyname(ip),port))

		#set a packet buffer size to receive
		banner = s.recv(4028)
		return banner

	except Exception, e:
		message = "An Error Occured: " + str(e)
		return message

# def errMsg():
# 	message = "This is the error found "
# 	return message

def checkVulns(banner,filename):
	f = open(filename,'r') #file must be place in the same root directory
	for line in f.readlines():
		if line.strip("\n") in banner:
			print "[+] Server is vulnerable " + banner.strip("\n")
		else:
			print "Message: " + banner
			print "[-] Server is not vulnerable currently"
	return

#our main entering for the app
def main():
	#portList = [21,22,25,53,80,110,443]
	portList = [80]

	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print filename + " does not exit"
			exit(0)
		elif not os.access(filename, os.R_OK):
			print "Sorry you don't have access to " + filename
			exit(0)
		else:		
			#change range(1,255) after production
			for ip in range(1):
				ipAddress = "192.168.10."+str(ip)
				for port in portList:
					banner = retBanner(ipAddress,port)
					if banner:
						print "[+]" + str(ipAddress) + ":" + str(port)
						checkVulns(banner,filename)
						print "\n"

#main entering call function of the app
if __name__ == '__main__':
	main()