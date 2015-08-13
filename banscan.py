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

		#creates a list of dictionary port identifier 
		portList = {"ftp":21,"ssh":22,"smtp":25,"dns":53,"http":80,"https":443}

		#connect to the remote host with port number
		s.connect((socket.gethostbyname(ip),portList[port]))

		#set a packet buffer size to receive
		banner = s.recv(4028)
		return banner

	except Exception, e:
		message = "An Error Occured: " + str(e)
		return message

def checkVulns(banner):
	if "FreeFloat FTP Server" in banner:
		print "Frefloat ftp server is vulnerable to an attack"
	elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
		print '[+] 3CDaemon FTP Server is vulnerable.'
	elif 'Ability Server 2.34' in banner:
		print '[+] Ability FTP Server is vulnerable.'
	elif 'Sami FTP Server 2.0.2' in banner:
		print '[+] Sami FTP Server is vulnerable.'
	else:
		print '[-] FTP Server is not vulnerable.'
	return

#our main entering for the app
def main():
	domain1 = "localhost"
	domain2 = "127.0.0.1"
	portid1 = 'ftp'
	portid2 = 80

	banner1 = retBanner(domain1,portid1)

	if banner1:
		print "[+] Banner 1 has: " + str(domain1) + ":" + str(portid1)
		checkVulns(banner1)
		print "\n"

	banner2 = retBanner(domain2,portid2)
	if banner2:
		print "[+] Banner 1 has: " + str(domain2) + ":" + str(portid2)
		checkVulns(banner2)
		print "\n"

#main entering call function of the app
if __name__ == '__main__':
	main()