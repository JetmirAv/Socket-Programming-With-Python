import socket
import sys
from _thread import *
from clientThread import *

host = 'localhost'
port = 12000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try: 
    s.bind((host, port)) 
    while True:
        conn, addr = s.recvfrom(1024)
        start_new_thread(clientthread, (conn, addr, s))
        print("Connected with " + str(addr[0]) + ":" + str(addr[1]))
        
    s.close() 
except socket.error:
    print("Porti eshte duke u perdorur")
