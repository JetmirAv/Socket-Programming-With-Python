import socket 
import sys

def connect():
    BUFFER_SIZE = 1024 
    MESSAGE = ''
    fiekTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    fiekTCP.connect((host, port))
    print("Socket-i u krijua me sukses ne hostin " + host + " me port " + str(port))
    
    while MESSAGE != 'exit':
        
        try:
            data = fiekTCP.recv(BUFFER_SIZE).decode()
            if  data == 'terminate':
                break
            MESSAGE = input("Serveri: " + data + "\n")
            if not MESSAGE:
                MESSAGE = 'null'
            fiekTCP.send(str.encode(MESSAGE))
        except KeyboardInterrupt:
            MESSAGE = 'ProcessTerminatedByUser'
            fiekTCP.send(str.encode(MESSAGE))
            print('Ju e mbyllet socketin')
            break
    print('Socketi u mbyll') 
    fiekTCP.close() 
    vazhdo()

def vazhdo():
    input1 = input("A deshironi te lidheni me ndonje server tjeter(PO): ").upper()
    if not input1 or input1 == "PO":
        hosti()
        porti()    
        connect()
    else: 
        print("Scripta u ndal")    

def hosti():
    input1 = input("Shkruani host-in me te cilin doni te lidheni.(default localhost): ")
    if not input1:
        return 'localhost'
    else: 
        isIp = validate_ip(input1)
        if not isIp:
            try:
                host_ip = socket.gethostbyname(input1)
                return host_ip
            except socket.gaierror:
                print("There was an error resolving the host. Try again")
                hosti()
        else: 
            return input1               
def porti():
    input2 = input("Shkruani portin me te cilin doni te lidheni.(default 12000): ")        
    if not input2 :
        return 12000
    else:
        try:
            val = int(input2)
            return val
        except:
            print("Porti duhet te jete nje numer.") 
            porti()   
               
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


host = hosti()
port = porti()
connect()
