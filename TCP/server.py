import socket
import sys 
from _thread import *
from clientThread import *

host = 'localhost'
port = 12000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    s.bind((host, port))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        print("Connected with " + str(addr[0]) + ":" + str(addr[1]))
        try: 
            start_new_thread(clientthread, (conn, addr, s))
        except ConnectionAbortedError: 
            print("Klienti nderpreu lidhjen me server")     
    s.close()
except ConnectionAbortedError: 
            print("Klienti nderpreu lidhjen me server")       
except socket.error:
    print("Porti eshte duke u perdorur")
 





