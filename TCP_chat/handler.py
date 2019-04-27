from metodat import *

def handler(data, addr):
    data = data.decode()
    data = data.split(" ", 1)

    method = data[0].upper().strip()
    
    if method == "{help}".upper():
        MESSAGE = """Zgjedhni njerin nga Operacionet (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI, KONTROLLOPORTIN, PASSWORDGEN)? """ 
         
    elif method == "IPADRESA":
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
        MESSAGE =  EMRIKOMPJUTERIT()   

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
    else: 
        MESSAGE = "null"
    
    return MESSAGE
