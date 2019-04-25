import socket 
import sys

def connect(host, port):
    BUFFER_SIZE = 1024 
    MESSAGE = ''
    data = ''
    ### Krijojm socketin ne protokollin TCP
    fiekUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    try:
        ### Tetojme kyqjen ne hostin dhe portin e kerkuar. 
        fiekUDP.connect((host, port))
        print("Socket-i u krijua me sukses ne hostin " + host + " me port " + str(port))
    ### Kontrolli per gabime  
    except ConnectionRefusedError:
        print("Nuk mund te krijohet lidhja me server")
        vazhdo()

    fiekUDP.sendall("Hello".encode())    
    
    while MESSAGE != 'exit' and data != 'EXIT':
        
        try:
            ### Presim pergjigje nga serveri
            data = fiekUDP.recvfrom(BUFFER_SIZE)[0].decode()
            ### Kontrollojm pergjigjen
            if data == 'exit':
                break
            ### Presim kerkesen nga tastiera    
            MESSAGE = input("Serveri: " + data + "\nShkruaj kerkesen: ")
            if not MESSAGE:
                MESSAGE = 'null'
            if MESSAGE.upper() == 'EXIT':
                break     
            ### Dergojme kerkesen ne server   
            fiekUDP.sendto(str.encode(MESSAGE), (host, port))

            data = fiekUDP.recvfrom(BUFFER_SIZE)[0].decode()
            
            print(data)

            data = fiekUDP.recvfrom(BUFFER_SIZE)[0].decode().upper()
            
        ### Kontrolli per gabime  
        except KeyboardInterrupt:
            MESSAGE = 'ProcessTerminatedByUser'
            fiekUDP.send(str.encode(MESSAGE))
            print('\nJu e mbyllet socketin')
            break
        except BrokenPipeError:
            print('\nServeri eshte down')
            break    
        except OSError:  
            break
    print('Socketi u mbyll') 
    ### Mbyllim socketin me serverin
    fiekUDP.close() 
    vazhdo()

### Metode ndihmese per te vazhduar apo jo 
def vazhdo(): 
    try:
        input1 = input("A deshironi te lidheni me ndonje server tjeter(PO): ").upper()
        if not input1 or input1 == "PO":
            host = hosti()
            port = porti()    
            connect(host, port)
        else: 
            print("Scripta u ndal")    
    ### Kontrolli per gabime          
    except KeyboardInterrupt:
        print("\nScripta u ndal")
## Metoda per te zgjedhur hostin              
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
                    print("Nuk ishte e mundur te gjindet hosti, Provoni serish")
                    hosti()
            else: 
                return input1    
    ### Kontrolli per gabime                    
    except KeyboardInterrupt:
        print("\nScripta u ndal")
### Metoda per te zgjedhur portin   
def porti():
    try:
        input2 = input("Shkruani portin me te cilin doni te lidheni.(default 8000): ")        
        if not input2 :
            return 8000
        else:
            try:
                val = int(input2)
                return val
            except:
                print("Porti duhet te jete nje numer.") 
                porti()   
    except KeyboardInterrupt:
        print("\nScripta u ndal")    
### Metoda e cila teston ip se a jan ne formartin IPv4        
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


