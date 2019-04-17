# import socket
# import sys
# from _thread import *
# from clientThread import *

# # Create a TCP/IP socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # Bind the socket to the port
# server_address = ('localhost', 10000)
# print('starting up on %s port %s' % server_address)


# try:
#     s.bind(server_address)
#     while True:
#         print('\nwaiting to receive message')
#         data, address = s.recvfrom(1024)
#         start_new_thread(clientthread, (data, address, s))
        
#         # print('received %s bytes from %s' % (len(data), address))
#         # print(data.decode())
        
#         # if data:
#         #     sent = s.sendto(data, address)
#         #     print('sent %s bytes back to %s' % (sent, address))
# except KeyboardInterrupt:
#     print("\nServeri u ndal")
# except AssertionError: 
#     print('\nServeri u ndal')

# import threading
# import socket

# class Broker():
    
#     def __init__(self):
#         server_address = ('localhost', 10000)
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         self.sock.bind(server_address)

#     def talkToClient(self, ip):
#         self.sock.sendto("ok".encode(), ip)

#     def listen_clients(self):
#         while True:
#             msg, client = self.sock.accept()
#             t = threading.Thread(None, self.talkToClient, None, (client,), None)
#             t.start()
# b = Broker()
# b.listen_clients()


import threading
import socketserver
from metodat import *

class ThreadedUDPRequestHandler(
	socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip().decode().upper()
        data = data.split(" ",1)
		### get port number
        port = self.client_address[1]
		### get the communicate socket
        socket = self.request[1]
		### get client host ip address
        client_address = (self.client_address[0])
        print("received call from client address: %s:%s" %(client_address, port))
        if len(data) == 1:
            print("received data: %s" %(data[0]))
        else:    
            print("received data: %s %s" %(data[0], data[1]))
		
        if data[0] == "IPADRESA":
            MESSAGE = IPADRESA(client_address)

        elif data[0] == "NUMRIIPORTIT":
            MESSAGE =  NUMRIIPORTIT(port)

        elif data[0] == "BASHKETINGELLORE": 
            MESSAGE = BASHKETINGELLORE(socket, self)
        elif data[0] == "PRINTIMI":
            if len(data) != 2:
                MESSAGE = "Ju duhet te shtypni Printimi {hapsire} metoda."
            else:        
                MESSAGE = PRINTIMI(data[1])

        elif data[0] == "EMRIIKOMPJUTERIT":
            MESSAGE =  EMRIKOMPJUTERIT(socket)   

        elif data[0] == "KOHA":
            MESSAGE = KOHA()  

        elif data[0] == "LOJA":
            MESSAGE =  LOJA()   
             
        elif data[0] == "KONTROLLOPORTIN":
            host_port = data[1].split(" ",1)
            if len(host_port) != 2:
                MESSAGE = "Ju duhet te shtypni kontrollohostin {hapsire} hosti {hapsire} porti."
            else:        
                MESSAGE = KONTROLLOPORTIN(host_port[0], host_port[1])
 
        elif data[0] == "PASSWORDGEN":
            MESSAGE = PASSWORDGEN()

        # elif data[0] == "FIBONACCI":
        #     numri = "Shkruani numrin: "
        #     (numri.encode(), addr)
        #     try: 
        #         num = int(s.recvfrom(1024).decode())
        #         MESSAGE = str(Fibonacci(num))
        #     except:
        #         MESSAGE = 'Duhet te shtypni nje numer.(INT)'

            
        elif data[0] == "KONVERTIMI":
           MESSAGE = KONVERTIMI(socket)
        elif data[0] == 'EXIT' or  data[0] == 'ProcessTerminatedByUser'.upper():
            MESSAGE = 'Klienti nderpreu lidhjen\n'
               
        # else: 
        #     try:
        #         MESSAGE = "Ju nuk keni zgjedhur asnje nga opcionet e mesiperme.\nA deshironi te nderpreni lidhjen?(JO)"
        #         socket.sendto(str.encode(MESSAGE), addr)
        #         response = s.recvfrom(1024).decode().upper()
        #         if response == 'JO':
        #             MESSAGE = "Vazhdoni"
        #         else: 
        #             print(MESSAGE)
        #             MESSAGE = 'exit'
        #             s.sendto(MESSAGE.encode(), addr)
                          
            # except socket.error:
            #     print("Lidhja u ndepre")
                
        
       
        socket.sendto(MESSAGE.upper().encode(), self.client_address)  
        # except:
        #     print("Nuk eshte e mundur ti dergohet nje pergjigje klientit")  
                  

		### assemble a response message to client
        
class ThreadedUDPServer(
socketserver.ThreadingMixIn, 
socketserver.UDPServer):
    pass

if __name__ == "__main__":
    # in this example, we will bind port to 8888
    # for client socketection
    HOST, PORT = "localhost", 8888

    server = ThreadedUDPServer((HOST, PORT), 
		ThreadedUDPRequestHandler)
    ip, port = server.server_address
    server.serve_forever()
    # Start a thread with the server -- 
	# that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    server.shutdown()