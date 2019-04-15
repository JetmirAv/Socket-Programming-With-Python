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

        elif method == "FIBONACCI":
            numri = "Shkruani numrin: "
            conn.send(numri.encode())
            num = int(conn.recv(1024).decode())
            MESSAGE = str(Fibonacci(num))

        elif method == "KONVERTIMI":
           MESSAGE = KONVERTIMI(conn)
        elif method == 'exit' or  method == 'ProcessTerminatedByUser'.upper():
            break   
        else: 
            MESSAGE = "Ju nuk keni zgjedhur asnje nga opcionet e mesiperme.\nA deshironi te nderpreni lidhjen?(JO)"
            conn.send(str.encode(MESSAGE))
            response = conn.recv(1024).decode().upper()
            if response == 'JO':
                MESSAGE = "Vazhdoni"
            else: 
                print(MESSAGE)
                MESSAGE = 'terminate'
                conn.send(MESSAGE.encode())
                break      
        
        
        
        conn.send(str.encode(MESSAGE) + ("\n").encode() + welcome.encode())  
    MESSAGE = "Lidhja me " + str(addr[0]) + ":" + str(addr[1]) + " u nderpre"
    print(MESSAGE) 
    conn.close()        

