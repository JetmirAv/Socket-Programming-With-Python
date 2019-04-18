import socket
import sys 
import datetime
import random


#metoda IPADRESA
def IPADRESA(addr):
    return "IP Adresa e klientit është: " + str(addr[0])
#metoda NUMRIIPORTIT
def NUMRIIPORTIT(addr):
    return "Klienti është duke përdorur portin: " + str(addr[1]) 
#metoda EMRIKOMPJUTERIT
def EMRIKOMPJUTERIT(s):
    return "Emri I hostit është: " + socket.gethostname()
#metoda BASHKETINGELLORE
def BASHKETINGELLORE(conn):
    lista = ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U' , ' ' , '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    teksti = "Shkruani tekstin: "
    conn.send(teksti.encode())
    txt = conn.recv(1024).decode() 
    numero=0
    for i in txt:
      #if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i==' ' or i == '1'):
       if(i in lista):
            numero+=1
    return "Teksti i pranuar përmban " + str(len(txt) - numero) + " bashketingellore" 
    
#metoda Fibonacci
def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci(n-1)+Fibonacci(n-2)
#metoda KOHA
def KOHA():
    return datetime.datetime.now().strftime("DATA: %Y-%m-%d KOHA: %H:%M")
#metoda LOJA
def LOJA():
    numArray = []
    for x in range(7):
        numArray.append(random.randint(1,49))
    return str(numArray)[1:-1]    
#metoda PRINTIMI
def PRINTIMI(conn):
    teksti = "Shkruani tekstin: "
    conn.send(teksti.encode())
    txt = conn.recv(1024).decode() 
    return txt.strip() 
#metoda KONVERTIMI
def KONVERTIMI(conn):
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
        return "Duhet te shtypni nje numer.(INT)"
           
    val = "Jepni sasine: "
    conn.send(val.encode())
    try: 
        value = float(conn.recv(1024).decode())
    except:
        return "Duhet te shtypni nje numer.(Float)"
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
        return str("Vlere e panjohur")

#metoda Gjenero Password
def PASSWORDGEN():
    Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Lowercase = "abcdefghijklmnopqrstuvwxyz"
    Digits = "0123456789"
    Symbols = "()!?*+=_-"

    Mixedbag = Uppercase + Lowercase + Digits + Symbols
    while True:
        word_length = random.randint(10, 20)

        Madeword = ""
        for x in range(word_length):
            ch = random.choice(Mixedbag)
            Madeword = Madeword + ch
        break
    return ("Password: " + Madeword)    

#metoda KONTROLLOPORTIN
def KONTROLLOPORTIN(conn):
    teksti = "Shkruani hostin te cilin doni ta testoni: "
    conn.send(teksti.encode())
    host = conn.recv(1024).decode() 
    isIp = validate_ip(host)
    if not isIp:
        try:
            host_ip = socket.gethostbyname(host)
            host = host_ip
        except socket.gaierror:
            return "Nuk ishte e mundur te gjindet hosti"
    teksti = "Shkruani portin te cilin doni ta testoni: "
    conn.send(teksti.encode())
    try:
        port = int(conn.recv(1024).decode())
        if (port < 0 or port > 65535): 
            return ("Porti duhet te jete nje numer ne intervalin 0-65535") 
        
    except:
        return ("Porti duhet te jete nje numer.") 
    
    if check_port(host, port):
        return ("Porti " + str(port) + " ne hostin " + str(host) + " eshte i hapur")     
    else: 
        return ("Porti " + str(port) + " ne hostin " + str(host) + " eshte i mbyllur")     

#metoda CHECK PORT
def check_port(host, port):
    SUCCESS = 0
    timeout = 0.5
    sock = socket.socket()
    sock.settimeout(timeout)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connected = sock.connect_ex((host, port)) is SUCCESS
    sock.close()
    print(connected)
    return connected

#metoda Per validimin e IP te tipit IPv4
def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True