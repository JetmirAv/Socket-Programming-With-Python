import socket
import sys 
import datetime
import random


#IPADRESA
def IPADRESA(addr):
    return "IP Adresa e klientit është: " + str(addr[0])
#NUMRIIPORTIT
def NUMRIIPORTIT(addr):
    return "Klienti është duke përdorur portin: " + str(addr[1]) 
#EMRIKOMPJUTERIT
def EMRIKOMPJUTERIT(s):
    return "Emri I hostit është: " + socket.gethostname()
# BASHKETINGELLORE
def BASHKETINGELLORE(conn):
    teksti = "Shkruani tekstin: "
    conn.send(teksti.encode())
    txt = conn.recv(1024).decode() 
    vowels=0
    for i in txt:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    return "Teksti i pranuar përmban " + str(vowels) + " bashketingellore" 
    
#Fibonacci
def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci(n-1)+Fibonacci(n-2)
#KOHA
def KOHA():
    return datetime.datetime.now().strftime("DATA: %Y-%m-%d KOHA: %H:%M")
#LOJA
def LOJA():
    numArray = []
    for x in range(7):
        numArray.append(random.randint(1,49))
    return str(numArray)[1:-1]    
#PRINTIMI
def PRINTIMI(conn):
    teksti = "Shkruani tekstin: "
    conn.send(teksti.encode())
    txt = conn.recv(1024).decode() 
    return txt.strip() 
#KONVERTIMI
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
        value = Double(conn.recv(1024).decode())
    except:
        return "Duhet te shtypni nje numer.(Double)"
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

