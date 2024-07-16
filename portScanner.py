#!/bin/python3

# This is a simple port Scanner written in python
# The file takes the IP address as the argument and prints out the ports that are open
# Author: M.F.M. Ashfaaq

import sys
import socket
from datetime import datetime
import pyfiglet

ban = pyfiglet.figlet_format("PORT SCANNER")

# First step is to define our target

if len(sys.argv) == 2:

    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to ipv4
    print(target)

else:
    print(ban)
    print("Invalid number of arguments")
    sys.stdout.write('Syntax\n')
    sys.exit()

# Add a pretty banner
print(ban)
print("*" * 50)
print("Scanning target: " +target)
print("Time Started: " +str(datetime.now()))
print("*" * 50)


# Perform Scan
for port in range(1,65536):
             s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             socket.setdefaulttimeout(1)
             result = s.connect_ex((target,port))

             if result == 0:
                 print(f"Port {port} is open")
             s.close() 
                

