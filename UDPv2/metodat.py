import socket
import sys 
import datetime
import random


#metoda IPADRESA
def IPADRESA(addr):
    return "IP Adresa e klientit është: " + str(addr)
#metoda NUMRIIPORTIT
def NUMRIIPORTIT(addr):
    return "Klienti është duke përdorur portin: " + str(addr) 
#metoda EMRIKOMPJUTERIT
def EMRIKOMPJUTERIT(s):
    return "Emri I hostit është: " + socket.gethostname()
#metoda BASHKETINGELLORE
def BASHKETINGELLORE(txt):
    lista = ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U' , ' ' , '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numero=0
    for i in txt:
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
def PRINTIMI(data):
    return data.strip() 
    
#metoda KONVERTIMI
def KONVERTIMI(opcioni, sasia):               
    if opcioni == "KilowattToHorsepower".upper():
        return str(sasia*1.34102)
    elif opcioni == "HorsepowerToKilowatt".upper(): 
        return str(sasia*0.7457)
    elif opcioni == "DegreesToRadians".upper():
        return str(sasia*0.0174533)
    elif opcioni == "RadiansToDegrees".upper():
        return str(sasia*57.2958)
    elif opcioni == "GallonsToLiters".upper():
        return str(sasia*3.78541)
    elif opcioni == "LitersToGallons".upper():
        return str(sasia*0.264172)
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
def KONTROLLOPORTIN(host, port):
    isIp = validate_ip(host)
    if not isIp:
        try:
            host_ip = socket.gethostbyname(host)
            host = host_ip
        except socket.gaierror:
            return "Nuk ishte e mundur te gjindet hosti"
    try:
        port = int(port)
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
    ### Krijon nje socket te ri
    sock = socket.socket()
    ### Vendos kohen se sa duhet te pres pergjgjen nga hosti
    sock.settimeout(timeout)
    ### Vendos parametrat mbi te cilat do punoj socketi i ri
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ### Teston nese mund te lidhet me hostin ne portin e kerkuar
    connected = sock.connect_ex((host, port)) is SUCCESS
    sock.close()
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