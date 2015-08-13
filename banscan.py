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
	portList = [21,22,25,53,80,110,443]
	#change range(1,255) after production
	for ip in range(1,10):
		ipAddress = "192.168.10."+str(ip)
		for port in portList:
			banner = retBanner(ipAddress,port)
			if banner:
				print "[+]" + str(domain1) + ":" + str(portid1)
				checkVulns(banner)
				print "\n"


#main entering call function of the app
if __name__ == '__main__':
	main()