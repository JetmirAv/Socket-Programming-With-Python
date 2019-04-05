import socket
import sys 
import datetime
import random
from _thread import *

host = 'localhost'
port = 8888

#EMRIKOMPJUTERIT
def EMRIKOMPJUTERIT():
    print(s.getsockname())
    return s.getsockname()[0]
# BASHKETINGELLORE
def BASHKETINGELLORE(input):
    #vowel_list = set(['a','e','i','o','u'])
    #vowels = 0
    #for char in input:
     #   if char in vowel_list:
     #       vowels += 1
    #return vowels
    vowels=0
    for i in input:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    return vowels
#Fibonacci
def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci(n-1)+Fibonacci(n-2)
#KOHA
def KOHA():
    return datetime.datetime.now().strftime("Date: %Y-%m-%d Time: %H:%M")
#LOJA
def LOJA():
    numArray = []
    for x in range(7):
        numArray.append(random.randint(1,49))
    return numArray    
#PRINTIMI
def PRINTIMI(input):
    return input
#KONVERTIMI
def KONVERTIMI(num):
    val = "Jepni masen qe doni te konvertoni: "
    conn.send(val.encode())
    try: 
        value = int(conn.recv(1024).decode())
    except:
        return "You must enter a number"
    if num == 1:
        return str(value*1.34102)
    elif num == 2: 
        return str(value*0.7457)
    elif num == 3:
        return str(value*0.0174533)
    elif num == 4:
        return str(value*57.2958)
    elif num == 5:
        return str(value*3.78541)
    elif num == 6:
        return str(value*0.264172)
    else:
        return str("Invalid Value")





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    s.bind((host, port))
except socket.error:
    print("Bind error")

s.listen(10)

def clientthread(conn, addr):
    welcome =   """Mirseerdhet!
                Zgjedhni njerin nga Operacionet 
                (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, 
                PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA,
                FIBONACCI, KONVERTIMI)? """
    conn.send(welcome.encode())

    while True:
        welcome2 = """Zgjedhni njerin nga Operacionet 
                (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, 
                PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA,
                FIBONACCI, KONVERTIMI)? """        
        data = conn.recv(1024).decode() 
        if not data:
            break
        print("Server received data:", data)
        method = data.upper()
        
        if method == "IPADRESA":
            MESSAGE = "IP Adresa e klientit është: " + str(addr[0])
        elif method == "NUMRIIPORTIT":
            MESSAGE = "Klienti është duke përdorur portin: " + str(addr[1])    
        elif method == "BASHKETINGELLORE":
            teksti = "Shkruani tekstin: "
            conn.send(teksti.encode())
            txt = conn.recv(1024).decode() 
            MESSAGE = "Teksti i pranuar përmban " + str(BASHKETINGELLORE(txt)) + " bashketingellore" 
        elif method == "PRINTIMI":
            teksti = "Shkruani tekstin: "
            conn.send(teksti.encode())
            txt = conn.recv(1024).decode() 
            MESSAGE = txt.strip() 
        elif method == "EMRIIKOMPJUTERIT":
             MESSAGE = "Emri I klientit është: " +  str(s.getsockname()[0])   
        elif method == "KOHA":
             MESSAGE = KOHA()  
        elif method == "LOJA":
             MESSAGE = str(LOJA())[1:-1]      
        elif method == "FIBONACCI":
            numri = "Shkruani numrin: "
            conn.send(numri.encode())
            num = int(conn.recv(1024).decode())
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
            conn.send(opcionet.encode())
            try: 
                num = int(conn.recv(1024).decode())
            except:
                print("You must type a number")
            MESSAGE = KONVERTIMI(num)
        else: 
           MESSAGE = "We dont know what to do with your request"
        print(MESSAGE)
        if MESSAGE == 'exit':
            break
        conn.send(str.encode(MESSAGE) + ("\n").encode() + welcome2.encode())  # echo 
        
    conn.close()        



while 1:
    conn, addr = s.accept()
    print("Connected with " + str(addr[0]) + ":" + str(addr[1]))
    start_new_thread(clientthread, (conn, addr)) 


s.close()