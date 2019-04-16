from metodat import *

def clientthread(conn, addr, s):
    welcome = """Zgjedhni njerin nga Operacionet 
                (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, 
                PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA,
                FIBONACCI, KONVERTIMI)? """ 
    conn.send(welcome.encode())

    while True:
               
        data = conn.recv(1024).decode() 
        
        print("Server received data:", data)
        method = data.upper()
        
        if method == "IPADRESA":
            MESSAGE = IPADRESA(addr)

        elif method == "NUMRIIPORTIT":
            MESSAGE =  NUMRIIPORTIT(addr)

        elif method == "BASHKETINGELLORE":
            MESSAGE = BASHKETINGELLORE(conn)
        elif method == "PRINTIMI":
            MESSAGE = PRINTIMI(conn)

        elif method == "EMRIIKOMPJUTERIT":
            MESSAGE =  EMRIKOMPJUTERIT(s)   

        elif method == "KOHA":
            MESSAGE = KOHA()  

        elif method == "LOJA":
            MESSAGE =  LOJA()   
             
        elif method == "KONTROLLOPORTIN":
            MESSAGE = KONTROLLOPORTIN(conn)

        elif method == "PASSWORDGEN":
            MESSAGE = PASSWORDGEN()

        elif method == "FIBONACCI":
            numri = "Shkruani numrin: "
            conn.send(numri.encode())
            try: 
                num = int(conn.recv(1024).decode())
                MESSAGE = str(Fibonacci(num))
            except:
                MESSAGE = 'Duhet te shtypni nje numer.(INT)'

            
        elif method == "KONVERTIMI":
           MESSAGE = KONVERTIMI(conn)
        elif method == 'EXIT' or  method == 'ProcessTerminatedByUser'.upper():
            MESSAGE = 'Klienti nderpreu lidhjen\n'
            break   
        else: 
            try:
                MESSAGE = "Ju nuk keni zgjedhur asnje nga opcionet e mesiperme.\nA deshironi te nderpreni lidhjen?(JO)"
                conn.send(str.encode(MESSAGE))
                response = conn.recv(1024).decode().upper()
                if response == 'JO':
                    MESSAGE = "Vazhdoni"
                else: 
                    print(MESSAGE)
                    MESSAGE = 'exit'
                    conn.send(MESSAGE.encode())
                    break      
            except socket.error:
                print("Lidhja u ndepre")
                break
        
        try:
            conn.send(str.encode(MESSAGE) + ("\n").encode() + welcome.encode())  
        except socket.error:
            print("Nuk eshte e mundur ti dergohet nje pergjigje klientit")  
            break      
    MESSAGE += "Lidhja me " + str(addr[0]) + ":" + str(addr[1]) + " u nderpre"
    print(MESSAGE) 
    conn.close()        

