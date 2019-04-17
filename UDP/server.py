import threading
import socketserver
from metodat import *

print("""
:::::::::::::::::::::::::::::::::::::::'########:'####:'########:'##:::'##::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ##.....::. ##:: ##.....:: ##::'##:::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ##:::::::: ##:: ##::::::: ##:'##::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ######:::: ##:: ######::: #####:::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ##...::::: ##:: ##...:::: ##. ##::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ##:::::::: ##:: ##::::::: ##:. ##:::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ##:::::::'####: ########: ##::. ##::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::..::::::::....::........::..::::..:::::::::::::::::::::::::::::::::::::::::
:::'##::::'##:'########::'########::::::::::::'######::'########:'########::'##::::'##:'########:'########::'####:
::: ##:::: ##: ##.... ##: ##.... ##::::::::::'##... ##: ##.....:: ##.... ##: ##:::: ##: ##.....:: ##.... ##:. ##::
::: ##:::: ##: ##:::: ##: ##:::: ##:::::::::: ##:::..:: ##::::::: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##:: ##::
::: ##:::: ##: ##:::: ##: ########::'#######:. ######:: ######::: ########:: ##:::: ##: ######::: ########::: ##::
::: ##:::: ##: ##:::: ##: ##.....:::........::..... ##: ##...:::: ##.. ##:::. ##:: ##:: ##...:::: ##.. ##:::: ##::
::: ##:::: ##: ##:::: ##: ##:::::::::::::::::'##::: ##: ##::::::: ##::. ##:::. ## ##::: ##::::::: ##::. ##::: ##::
:::. #######:: ########:: ##:::::::::::::::::. ######:: ########: ##:::. ##:::. ###:::: ########: ##:::. ##:'####:
::::.......:::........:::..:::::::::::::::::::......:::........::..:::::..:::::...:::::........::..:::::..::....::
""")


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):

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
            if len(data) == 1:
                MESSAGE = "Ju duhet te shtypni Bashketingellore {hapsire} teskti."
            else:    
                MESSAGE = BASHKETINGELLORE(data[1])
            
        elif data[0] == "PRINTIMI":
            if len(data) != 2:
                MESSAGE = "Ju duhet te shtypni Printimi {hapsire} teskti."
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

        elif data[0] == "FIBONACCI":
            if len(data) != 2:
                MESSAGE = "Ju duhet te shtypni Fibonacci {hapsire} numer."
            else:        
                if not data[1].isdigit():   
                    MESSAGE = "Ju duhet te shtypni Fibonacci {hapsire} numer."
                else:
                    MESSAGE = str(Fibonacci(int(data[1]))) 
            
        elif data[0] == "KONVERTIMI":
            if len(data) != 2:
                MESSAGE = "Ju duhet te shtypni Konvertimi {hapsire} opcioni {hapsire} sasia."                
            else:    
                opcioni = data[1].split(" ",1)
                if len(opcioni) != 2:
                    MESSAGE = "Ju duhet te shtypni Konvertimi {hapsire} opcioni {hapsire} sasia."
                else:
                    if not opcioni[1].isdigit():
                        MESSAGE = "Ju duhet te shtypni Konvertimi {hapsire} opcioni {hapsire} sasia."                
                    else: 
                        MESSAGE = KONVERTIMI(opcioni[0].upper(), float(opcioni[1]))
        elif data[0] == 'EXIT' or  data[0] == 'ProcessTerminatedByUser'.upper():
            MESSAGE = 'Klienti nderpreu lidhjen\n'
               
        else: 
            try:
                MESSAGE = "Ju nuk keni zgjedhur asnje nga opcionet e mesiperme."
                          
            except socket.error:
                print("Lidhja u ndepre")
                
        
       
        socket.sendto(MESSAGE.upper().encode(), self.client_address)       
class ThreadedUDPServer(
socketserver.ThreadingMixIn, 
socketserver.UDPServer):
    pass

if __name__ == "__main__":
    # in this example, we will bind port to 8888
    # for client socketection
    HOST, PORT = "localhost", 12000
    try:
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
    except KeyboardInterrupt:
        print("\nJu e ndalet serverin")    
    except OSError:
        print("Porti eshte i nxene")        