import socket 
import sys


defaultHost = 'localhsot'
defaultPort = 12000

### Metoda me te cilen starton Klienti
def connect(host, port):
    BUFFER_SIZE = 1024 
    MESSAGE = ''
    data = ''
    ### Krijojm socketin ne protokollin TCP
    fiekTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try:
        ### Tetojme kyqjen ne hostin dhe portin e kerkuar. 
        fiekTCP.connect((host, port))
        print("Socket-i u krijua me sukses ne hostin " + host + " me port " + str(port))
    ### Kontrolli per gabime  
    except ConnectionRefusedError:
        print("Nuk mund te krijohet lidhja me server")
        vazhdo()
    
    while MESSAGE != 'exit' and data != 'exit':
        
        try:
            ### Presim pergjigje nga serveri
            data = fiekTCP.recv(BUFFER_SIZE).decode()
            ### Kontrollojm pergjigjen
            if  data == 'exit':
                break
            ### Presim kerkesen nga tastiera    
            MESSAGE = input("Serveri: " + data + "\n")
            if not MESSAGE:
                MESSAGE = 'null'
            ### Dergojme kerkesen ne servers     
            fiekTCP.send(str.encode(MESSAGE))
        ### Kontrolli per gabime  
        except KeyboardInterrupt:
            MESSAGE = 'ProcessTerminatedByUser'
            fiekTCP.send(str.encode(MESSAGE))
            print('\nJu e mbyllet socketin')
            break
        except BrokenPipeError:
            print('\nServeri eshte down')
            break    
        except OSError:  
            break
    print('Socketi u mbyll') 
    ### Mbyllim socketin me serverin
    fiekTCP.close() 
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
        input1 = input("Shkruani host-in me te cilin doni te lidheni.(default %s): " %defaultHost)
        if not input1:
            return defaultHost
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
        input2 = input("Shkruani portin me te cilin doni te lidheni.(default %s): " %defaultPort)        
        if not input2 :
            return defaultPort
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
