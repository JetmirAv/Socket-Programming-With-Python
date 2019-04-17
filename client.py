import socket
import sys

HOST, PORT = "localhost", 8888
data = " ".join(sys.argv[1:])
received = ''
# Create a socket (SOCK_STREAM means a TCP socket)
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while received != 'exit'.upper() and data != 'exit':
        sock.connect((HOST, PORT))
        data = input("Type: ")
        print()
        print(data)
        print()
        sock.sendall(data.encode() + "\n".encode())

        received = sock.recv(1024)
except KeyboardInterrupt:
    print("\nScripta u ndal")        
finally:
    sock.close()

print("Sent:     %s"%data)
print("Received: %s"%received.decode())
