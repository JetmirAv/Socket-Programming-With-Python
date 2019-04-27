import socket 
from threading import Thread
from handler import *

#Krijojme nje objekte ku ruajme emrat dhe addresat e klienteve
klientet = {}
adresat = {}

#Vendosim hostin dhe portin ku do te punojne 
HOST = 'localhost'
PORT = 12000
BUFSIZ = 1024
ADDR = (HOST, PORT)
#Krijojme socket-in
FIEKChat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
FIEKChat.bind(ADDR)   

#Funksioni qe menaxhon pranimin e klienteve
def pranoKlientet():
    while True:
        #Pranon mesazhin e klientet dhe addresen      
        client, addr = FIEKChat.accept()
        print("%s:%s eshte lidhur." % addr)
        #Dergon mesazhin fillestar te klienti
        client.send(bytes("Mirseerdhet ne FIEK chat!" + 
        "Tani shkruani emrin me te cilin doni te perdorni kete chat dhe shtypni dergo!", "utf8"))
        #Ruan adresen dhe portin e klientit ne objektin adresat
        adresat[client] = addr
        #Starton nje thread per ate klient
        Thread(target=menaxhoKlientin, args=(client,)).start()

#Funksioni qe menaxhon pranim dergimin e mesazheve
def menaxhoKlientin(client):
    #Ruan emrin e klientit ne variablen emri    
    emri = client.recv(BUFSIZ).decode("utf8")
    #Dergon mesazhin welcome te klienti i sapo lidhur
    welcome = '''Pershendetje %s! Nese doni te mbyllni chat-in, shtypni {quit}. 
    Nese deshironi ndihme per te pare se cilat metoda perkrah, shtyp {help}''' % emri
    client.send(welcome.encode())
    #Transmeton mesazhin te cdo klient i lidhur ne ate moment
    msg = "%s i eshte bashkangjitur chat-it!" % emri
    transmeto(bytes(msg, "utf8"))
    #Shton emrin e klientit ne objectin klientet
    klientet[client] = emri
    #Fillojm nje loop-e me te cilen presim mesazhe dhe i procesojm 
    while True:
        #Pranon mesazhin nga kleinti
        msg = client.recv(BUFSIZ)
        #Kontrollon nese eshte i ndryshem nga {quit}
        if msg != bytes("{quit}", "utf8"):
            transmeto(msg, emri+": ")
            #Dergon mesazhin ne metoden handler e cila e kontrollon mesazhin 
            # se cka permban dhe varesisht se a ka ndonje pergjigje serveri e kthen ate
            msg = handler(msg, adresat[client]).encode()    
            if msg != "null".encode():
                print(msg)
                transmeto(msg, "Serveri: ")
        #Ne te kundert dergon te klienti po te njejtin mesazh 
        # dhe transmeton te klientet e tjere mesazhin me emrin + eshte skycur      
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            #Largon objektin e klientit
            del klientet[client]
            transmeto(bytes("%s eshte shkycur." % emri, "utf8"))
            break

#Funksioni i cili menaxhon transmetimin e mesazhit te secili klient            
def transmeto(msg, prefix=""):
    for sock in klientet:
        sock.send(bytes(prefix, "utf8")+msg)       

#Metoda main
if __name__ == "__main__":
    FIEKChat.listen(5)  
    print("Ne pritje te klienteve...")

    ACCEPT_THREAD = Thread(target=pranoKlientet)
    ACCEPT_THREAD.start()  
    ACCEPT_THREAD.join()
    FIEKChat.close()             