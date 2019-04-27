import socket 
import sys 
from _thread import *

# from clientThread import *
from metodat import *

host = 'localhost'
port = 12000
### Krijojm socketin te protokolit TCP
fiekUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try: 
### Header per scripten fiek tcp-serveri
    print("""
:::::::::::::::::::::::::::::::::::::::'########:'####:'########:'##:::'##::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ##.....::. ##:: ##.....:: ##::'##:::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ##:::::::: ##:: ##::::::: ##:'##::::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ######:::: ##:: ######::: #####:::::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ##...::::: ##:: ##...:::: ##. ##::::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ##:::::::: ##:: ##::::::: ##:. ##:::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ##:::::::'####: ########: ##::. ##::::::::::::::::::::::::::::::::::::: 
:::::::::::::::::::::::::::::::::::::::..::::::::....::........::..::::..:::::::::::::::::::::::::::::::::::::: 
'########::'######::'########::::::::::::'######::'########:'########::'##::::'##:'########:'########::'####::::
... ##..::'##... ##: ##.... ##::::::::::'##... ##: ##.....:: ##.... ##: ##:::: ##: ##.....:: ##.... ##:. ##:::::
::: ##:::: ##:::..:: ##:::: ##:::::::::: ##:::..:: ##::::::: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##:: ##:::::
::: ##:::: ##::::::: ########::'#######:. ######:: ######::: ########:: ##:::: ##: ######::: ########::: ##:::::
::: ##:::: ##::::::: ##.....:::........::..... ##: ##...:::: ##.. ##:::. ##:: ##:: ##...:::: ##.. ##:::: ##:::::
::: ##:::: ##::: ##: ##:::::::::::::::::'##::: ##: ##::::::: ##::. ##:::. ## ##::: ##::::::: ##::. ##::: ##:::::
::: ##::::. ######:: ##:::::::::::::::::. ######:: ########: ##:::. ##:::. ###:::: ########: ##:::. ##:'####::::
:::..::::::......:::..:::::::::::::::::::......:::........::..:::::..:::::...:::::........::..:::::..::....:::::
Startoi serveri ne %s:%s.
Ne Pritje te kerkesave.   
    """ %(host, port))


    ### Bashkangjesim hostin dhe portin ne te cilin do te punoj serveri
    fiekUDP.bind((host, port))
    

    while True:
        count = 1
        ### Presim per lidhje te ndonje serveri
        conn, addr = fiekUDP.recvfrom(1024)      
        print("Eshte kyqur klienti: " + str(addr[0]) + ":" + str(addr[1]))
        ### Krijimi i nje threadi te veqant per klientin e lidhur
        # start_new_thread(clientthread, (conn, addr, fiekUDP))   
        while count != 2:
            welcome = """Zgjedhni njerin nga Operacionet 
                    (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, 
                    PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA,
                    FIBONACCI, KONVERTIMI, KONTROLLOPORTIN, PASSWORDGEN)? """ 
        
        
            fiekUDP.sendto(welcome.encode(), addr)
            

            data, addr = fiekUDP.recvfrom(1024)
            data = data.decode() 
            print("Klienti %s:%s kerkoi: %s" %(addr[0], addr[1], data))

            data = data.split(" ", 1)
            
            method = data[0].upper().strip()
            
            if method == "IPADRESA":
                MESSAGE = IPADRESA(addr[0])

            elif method == "NUMRIIPORTIT":
                MESSAGE =  NUMRIIPORTIT(addr[1])

            elif method == "BASHKETINGELLORE":
                if len(data) == 1:
                    MESSAGE = "Ju duhet te shtypni Bashketingellore {hapsire} teskti."
                else:    
                    MESSAGE = BASHKETINGELLORE(data[1])
            elif method == "PRINTIMI":
                if len(data) != 2:
                    MESSAGE = "Ju duhet te shtypni Printimi {hapsire} teskti."
                else:        
                    MESSAGE = PRINTIMI(data[1])

            elif method == "EMRIIKOMPJUTERIT":
                MESSAGE =  EMRIKOMPJUTERIT(fiekUDP)   

            elif method == "KOHA":
                MESSAGE = KOHA()  

            elif method == "LOJA":
                MESSAGE =  LOJA()   
                    
            elif method == "KONTROLLOPORTIN":

                if len(data) != 2:
                    MESSAGE = "Ju duhet te shtypni kontrollohostin {hapsire} hosti {hapsire} porti."
                else:        
                    host_port = data[1].split(" ",1)
                    if len(host_port) != 2:
                        MESSAGE = "Ju duhet te shtypni kontrollohostin {hapsire} hosti {hapsire} porti."
                    else:        
                        MESSAGE = KONTROLLOPORTIN(host_port[0], host_port[1])
  
            elif method == "PASSWORDGEN":
                MESSAGE = PASSWORDGEN()

            elif method == "FIBONACCI":
                if len(data) != 2:
                    MESSAGE = "Ju duhet te shtypni Fibonacci {hapsire} numer."
                else:        
                    if not data[1].isdigit():   
                        MESSAGE = "Ju duhet te shtypni Fibonacci {hapsire} numer."
                    else:
                        MESSAGE = str(Fibonacci(int(data[1])))
            elif method == "KONTROLLOPORTIN":
                host_port = data[1].split(" ",1)
                if len(host_port) != 2:
                    MESSAGE = "Ju duhet te shtypni kontrollohostin {hapsire} hosti {hapsire} porti."
                else:        
                    MESSAGE = KONTROLLOPORTIN(host_port[0], host_port[1])
    
            elif method == "PASSWORDGEN":
                MESSAGE = PASSWORDGEN()

                
            elif method == "KONVERTIMI":
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
             
            elif method == 'EXIT' or  method == 'ProcessTerminatedByUser'.upper():
                MESSAGE = 'Klienti nderpreu lidhjen\n'  
            else: 
                try:
                    MESSAGE = "Ju nuk keni zgjedhur asnje nga opcionet e mesiperme."
                # Kontrolli per gabime               
                except socket.error:
                    print("Lidhja u ndepre")
            try:
                fiekUDP.sendto(str.encode(MESSAGE) + ("\n").encode(), addr)
                count += 1      
            except socket.error:
                print("Nuk eshte e mundur ti dergohet nje pergjigje klientit")  
                        
        MESSAGE += "\nLidhja me " + str(addr[0]) + ":" + str(addr[1]) + " u nderpre"
        print(MESSAGE) 
        
        fiekUDP.sendto(str.encode("exit"), addr)
    
### Kontrolli per gabime      
except KeyboardInterrupt:
    MESSAGE = 'exit'
    fiekUDP.sendto(str.encode(MESSAGE), addr)
    print("\nJu e ndalet serverin")
except ConnectionAbortedError: 
    print("Klienti nderpreu lidhjen me server")       
# except socket.error:
#      print("Porti eshte duke u perdorur")
 
 




