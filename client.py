import socket
import sys

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Error while creating socket")    
    sys.exit()

print("Socket created sucesfully")

host = "localhost"
port = 8888

try:
    remote_ip = socket.gethostbyname(host)
except socket.error:
    print("Could not find an ip address")
    sys.exit()

print("Ip adress" + remote_ip)

s.connect((remote_ip, port))

print("Socket connected to host: " + host + " by ip: " + remote_ip)