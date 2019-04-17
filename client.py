# import socket
# import sys

# # Create a UDP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server_address = ('localhost', 10000)
# message = 'Connected.'

# try:
#     print('sending "%s"' % message)
#     sent = sock.sendto(message.encode(), server_address)
#     while True:
#         print('waiting to receive')
#         data, server = sock.recvfrom(4096)
#         print('received "%s"' % data.decode())
        
#         message = input("Put some mesage: ")
#         print('sending "%s"' % message)
#         sent = sock.sendto(message.encode(), server_address)

#         # Receive response
        

# except KeyboardInterrupt:
#     print('\nScripta u ndal')
# finally:
#     print('Socketi u mbyll')
#     sock.close()    

# import socket
# server_address = ('localhost', 10000)
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
# MESSAGE = input("Put some msg: ").encode()
# sock.sendto(MESSAGE, server_address)

# while True:
#     msg, b = sock.recvfrom(1024)
#     print(msg.decode())


import socket
import sys

HOST, PORT = "localhost", 8888
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    data = input("Type: ")
    print()
    print(data)
    print()
    sock.sendall(data.encode() + "\n".encode())

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

print("Sent:     %s"%data)
print("Received: %s"%received.decode())
