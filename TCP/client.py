import socket 
import sys

def connect(host, port):
    BUFFER_SIZE = 1024 
    MESSAGE = ''
    data = ''
    fiekTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try:
        fiekTCP.connect((host, port))
        print("Socket-i u krijua me sukses ne hostin " + host + " me port " + str(port))
    except ConnectionRefusedError:
        print("Nuk mund te krijohet lidhja me server")
        vazhdo()
    
    while MESSAGE != 'exit' and data != 'exit':
        
        try:
            data = fiekTCP.recv(BUFFER_SIZE).decode()
            if  data == 'exit':
                break
            MESSAGE = input("Serveri: " + data + "\n")
            if not MESSAGE:
                MESSAGE = 'null'
            fiekTCP.send(str.encode(MESSAGE))
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
    
    fiekTCP.close() 
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
        print("\nScripta u ndal")
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
    except KeyboardInterrupt:
        print("\nScripta u ndal")
def porti():
    try:
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
    except KeyboardInterrupt:
        print("\nScripta u ndal")            
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

print("""
:::::::::::::::::::::::::::::::::::::::'########:'####:'########:'##:::'##:::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ##.....::. ##:: ##.....:: ##::'##::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ##:::::::: ##:: ##::::::: ##:'##:::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ######:::: ##:: ######::: #####::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ##...::::: ##:: ##...:::: ##. ##:::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ##:::::::: ##:: ##::::::: ##:. ##::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::: ##:::::::'####: ########: ##::. ##:::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::..::::::::....::........::..::::..::::::::::::::::::::::::::::::::::::::
::::::'########::'######::'########::::::::::::'######::'##:::::::'####:'########:'##::: ##:'########:'####::::
::::::... ##..::'##... ##: ##.... ##::::::::::'##... ##: ##:::::::. ##:: ##.....:: ###:: ##:... ##..::. ##:::::
::::::::: ##:::: ##:::..:: ##:::: ##:::::::::: ##:::..:: ##:::::::: ##:: ##::::::: ####: ##:::: ##::::: ##:::::
::::::::: ##:::: ##::::::: ########::'#######: ##::::::: ##:::::::: ##:: ######::: ## ## ##:::: ##::::: ##:::::
::::::::: ##:::: ##::::::: ##.....:::........: ##::::::: ##:::::::: ##:: ##...:::: ##. ####:::: ##::::: ##:::::
::::::::: ##:::: ##::: ##: ##::::::::::::::::: ##::: ##: ##:::::::: ##:: ##::::::: ##:. ###:::: ##::::: ##:::::
::::::::: ##::::. ######:: ##:::::::::::::::::. ######:: ########:'####: ########: ##::. ##:::: ##::::'####::::
:::::::::..::::::......:::..:::::::::::::::::::......:::........::....::........::..::::..:::::..:::::....:::::
    """)
host = hosti()
port = porti()
connect(host, port)
