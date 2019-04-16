from metodat import *


def clientthread(conn, addr, s):
    welcome = """Zgjedhni njerin nga Operacionet 
                (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, 
                PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA,
                FIBONACCI, KONVERTIMI)? """             
    s.sendto(welcome.encode(), addr)
    while True:
               
        method, addr = s.recvfrom(1024)
        
        print("Server received data:", method.decode())
        method = method.upper()
        
        if method == "IPADRESA":
            MESSAGE =  IPADRESA(addr)

        elif method == "NUMRIIPORTIT":
            MESSAGE = NUMRIIPORTIT(addr)  

        elif method == "BASHKETINGELLORE":
            teksti = "Shkruani tekstin: "
            s.sendto(teksti.encode(), addr)
            txt = s.recvfrom(1024).decode() 
            MESSAGE = "Teksti i pranuar përmban " + str(BASHKETINGELLORE(txt)) + " bashketingellore" 

        elif method == "PRINTIMI":
            teksti = "Shkruani tekstin: "
            s.sendto(teksti.encode(),addr)
            txt = s.recvfrom(1024).decode() 
            MESSAGE = txt.strip() 

        elif method == "EMRIIKOMPJUTERIT":
             MESSAGE = EMRIKOMPJUTERIT(s)   

        elif method == "KOHA":
             MESSAGE = KOHA()  

        elif method == "LOJA":
             MESSAGE = LOJA()    

        elif method == "FIBONACCI":
            numri = "Shkruani numrin: "
            s.sendto(numri.encode(),addr)
            num = int(s.recvfrom(1024).decode())
            MESSAGE = str(Fibonacci(num))

        elif method == "KONVERTIMI":
            opcionet = """Zgjedhni njerin nga numrat korespondues me poshte: 
                    1:  KilowattToHorsepower
                    2:  HorsepowerToKilowatt
                    3:  DegreesToRadians
                    4:  RadiansToDegrees
                    5:  GallonsToLiters
                    6:  LitersToGallons
            """
            s.sendto(opcionet.encode(),addr)
            try: 
                num = int(s.recvfrom(1024).decode())
                MESSAGE = KONVERTIMI(s)
            except:
                print("Duhet te shtypni nje numer.")
            
        elif method == 'exit':
            break    
        else: 
            MESSAGE = "Ju nuk keni zgjedhur asnje nga opcionet e mesiperme.\nA deshironi te nderpreni lidhjen?(JO)"
            s.sendto(str.encode(MESSAGE),addr)
            response = s.recvfrom(1024).decode().upper()
            if response == 'JO':
               MESSAGE = "Vazhdoni"
            else: 
                MESSAGE = "Lidhja me " + str(addr[0]) + ":" + str(addr[1]) + " u nderpre"
                MESSAGE = ""
                s.sendto(str.encode(MESSAGE),addr)
                print(MESSAGE)
                break    

        print(MESSAGE)
        
        s.sendto(str.encode(MESSAGE) + ("\n").encode() + welcome.encode(), addr)  
        
    s.close()        

