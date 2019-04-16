import socket 
import sys

def connect(host, port):

    MESSAGE = ''
    fiekUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)
    fiekUDP.connect(server_address)
    print("Socket-i u krijua me sukses ne hostin " + host + " me port " + str(port))
    
    while MESSAGE != 'exit':
        try:
            fiekUDP.sendto(MESSAGE.encode(), server_address)
            data, address = fiekUDP.recvfrom(1024)
            if data == 'Lidhja u nderpre':
                break
            MESSAGE = input("Serveri: " + data.decode() + "\n")
            if not MESSAGE:
                MESSAGE = 'null'
        except KeyboardInterrupt:
            MESSAGE = 'ProcessTerminatedByUser'
            fiekUDP.sendto(str.encode(MESSAGE), server_address)
            print('\nJu e mbyllet socketin')
            break
        except BrokenPipeError:
            print('\nServeri eshte down')
            break       
    print('Socketi u mbyll socket')       
    fiekUDP.close()
    vazhdo()

def vazhdo():
    try:
        input1 = input("A deshironi te lidheni me ndonje server tjeter(PO): ").upper()
        if not input1 or input1 == "PO":
            host = hosti()
            port = porti()    
            connect(host, port)
        else: 
            print("Scripta u ndal")    
    except KeyboardInterrupt:
        print("Scripta u ndal")
def hosti():
    try:
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
    except KeyboardInterrupt:  
        print("Scripta u ndal")                      
def porti():
    input2 = input("Shkruani portin me te cilin doni te lidheni: ")        
    if not input2 :
        return 12000
    else:
        try:
            val = int(input2)
            return val
        except:
            print("Port must be a number.") 
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
connect(host, port)

