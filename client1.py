
import socket 

host = 'localhost' 
port = 8888
BUFFER_SIZE = 2000 
MESSAGE = ''
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

tcpClientA.connect((host, port))




 
while MESSAGE != 'exit':
    
    tcpClientA.send(str.encode(MESSAGE))
    data = tcpClientA.recv(BUFFER_SIZE).decode()
    print(" Client2 received data:", data)
    MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:")
    

tcpClientA.close() 