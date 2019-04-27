import socket
import sys

defaultHost = 'localhost'
defaultPort = 12000


### Metoda me te cilen starton Klienti
def connect(host, port):
    HOST, PORT = host, port
    data = " ".join(sys.argv[1:])
    received = ''
    
    ### Krijojm socketin ne protokollin UDP
    fiekUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        ### Tetojme kyqjen ne hostin dhe portin e kerkuar. 
        fiekUDP.connect((host, port))
        print("Socket-i u krijua me sukses ne hostin " + host + " me port " + str(port))
        data = ""
        ### Dergojme kerkesen per kycje ne server
        fiekUDP.sendall(data.encode() + "\n".encode())
        ### Presim pergjigje nga serveri
        received = fiekUDP.recv(1024)
        ### Printojm pergjigje nga serveri
        print("Serveri: %s"%received.decode())  
        ### Presim kerkesen nga tastiera dhe e dergojme
        data = input("Shkruani emrin e kerkeses: ")
        fiekUDP.sendall(data.encode())
        ### Presim pergjigje nga serveri per keresen
        received = fiekUDP.recv(1024)
        ### Printojm pergjigje nga serveri
        print("Serveri: %s"%received.decode())     
        print("Lidhja me serverin perfundoi")
    ### Kontrolli per gabime    
    except KeyboardInterrupt:
        print("\nScripta u ndal")    
    except BrokenPipeError:
            print('\nServeri eshte down')   
    except ConnectionRefusedError:
        print("Nuk mund te krijohet lidhja me serverin")                        
    finally:
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
    except TypeError:
        print("\nScripta u ndal")        
### Metoda per te zgjedhur hostin  
#           
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
    ### Kontrolli per gabime              
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
### Metoda qe gjen fjalen ne nje fjali
def contains_word(s, w):
    return f' {w} ' in f' {s} '