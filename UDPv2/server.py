import threading
import socketserver
from metodat import *
### Teksti qe shfaqet ne startim te scriptes
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
		###Ruajme portin e klientit ne variablen port
        port = self.client_address[1]
		### Ruajme socketin e nevojshem per komunikim ne variablen socket
        socket = self.request[1]
		### Ruajme adresen e klientit ne variablen client_address
        client_address = (self.client_address[0])
        print("Eshte kyqur klienti: %s:%s" %(client_address, port))
        welcome = """Zgjedhni njerin nga Operacionet 
                (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, 
                PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA,
                FIBONACCI, KONVERTIMI)? """ 
        socket.sendto(welcome.encode(), self.client_address)
        # data = self.request[0].strip().decode().upper()
        data = socket.recvfrom(1024)[0].decode()      
        data = data.split(" ",1)
        data[0] = data[0].upper()
        print(data[0])
        ### Testojme kerkesen
        if len(data) == 1:
            print("Klienti %s:%s kerkoi: %s" %(client_address, port, data[0]))
        else:    
            print("Klienti %s:%s kerkoi: %s %s" %(client_address, port, data[0], data[1]))
		
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
            ### Kontrolli per gabime               
            except socket.error:
                print("Lidhja u ndepre")
                
        
       
        socket.sendto(MESSAGE.encode(), self.client_address)       
class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

### Fillimi i scriptes
if __name__ == "__main__":
    host, port = "localhost", 12000
    try:
        ### Krijojm serverin me ane te Klases ThreadUDPServer ne portin 12000 
        server = ThreadedUDPServer((host, port), ThreadedUDPRequestHandler)    
        ip, port = server.server_address
        print("Startoi serveri ne %s:%s."  %(ip, port))
        print("Ne pritje te kerkesave.")
        ### Presim klientet
        server.serve_forever()
        ### Krijojme nje thread per cdo klient qe lidhet me serverin.
        ### Me pas ai thread krijon nga nje thread per cdo kerkese qe behet
        server_thread = threading.Thread(target=server.serve_forever)
        ### Fillon threadin
        server_thread.daemon = True
        server_thread.start()
        ### Mbyll te gjite thread-at ne lidhje me klientin ne momentin qe klienti shkeputet
        server.shutdown()
    ### Kontrolli per gabime
    except KeyboardInterrupt:
        print("\nJu e ndalet serverin")    
    except OSError:
        print("Porti eshte i nxene")        