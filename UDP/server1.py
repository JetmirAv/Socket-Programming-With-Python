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
        for i in range(1):
            conn, addr = s.recvfrom(1024)
            start_new_thread(clientthread, (conn, addr, s))
            print("Connected with " + str(addr[0]) + ":" + str(addr[1]))
        s.sendto("exit".encode(), addr)      
    s.close()     
except KeyboardInterrupt:
    MESSAGE = 'exit'
    s.sendto(str.encode(MESSAGE), addr)
    print("\nJu e ndalet serverin")
except ConnectionAbortedError: 
    print("Klienti nderpreu lidhjen me server")       
except socket.error:
    print("Porti eshte duke u perdorur")
except OSError:
    print("\nJu e ndalet serverin")