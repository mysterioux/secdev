#! /usr/bin/python
# created by: echris
# filename: banscan.y
# description: Scans FTP servers to check if the version has a potential vulnerability

import socket


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

def checkVulns(banner):
	f = open('vuln_banner.txt','r') #file must be place in the same root directory
	for line in f.readlines():
		if line.strip('\n') in banner:
			print "[+] Server is vulnerable " + banner.strip("\n")
		else:
			print "Message: " + banner
			print "[-] Server is safe for now"
	return

#our main entering for the app
def main():
	portList = [21,22,25,53,80,110,443]
	#change range(1,255) after production
	for ip in range(1,10):
		ipAddress = "192.168.10."+str(ip)
		for port in portList:
			banner = retBanner(ipAddress,port)
			if banner:
				print "[+]" + str(ipAddress) + ":" + str(port)
				checkVulns(banner)
				print "\n"

#main entering call function of the app
if __name__ == '__main__':
	main()