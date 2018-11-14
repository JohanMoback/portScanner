import socket
import subprocess
import sys
import logging 
from datetime import datetime

#Clear the screen 
subprocess.call('cls', shell=True)

#Input 
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#print a nice banner with information on which host we are about to scan
print ("-", 60)
print ("Please hold, scanning remote host", remoteServerIP)
print ("-" * 60)
 
time = datetime.now()

try:
	for port in range(1, 1025):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0: 
			print ("Port {}: Open".format(port))
		sock.close() 

except KeyboardInterrupt: 
	print ("Closing process")
	sys.exit()

except socket.gaierror: 
	print ("Hostname could not be resolved. Exiting")
	sys.exit()

except socket.error: 
	print ("Coulnd't connect to a server")
	sys.exit()

time2 = datetime.now()

total = time2 - time1 

print ("Scanning completed in: ", total)


