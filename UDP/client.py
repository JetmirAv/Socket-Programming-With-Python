import socket
import sys
def connect(host, port):
    HOST, PORT = "localhost", 12000
    data = " ".join(sys.argv[1:])
    received = ''
    # Create a socket (SOCK_STREAM means a TCP socket)
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect((host, port))
        print("Socket-i u krijua me sukses ne hostin " + host + " me port " + str(port))
        data = input("Type: ")
        sock.sendall(data.encode() + "\n".encode())
        received = sock.recv(1024)
        print("Serveri: %s"%received.decode())
    except KeyboardInterrupt:
        print("\nScripta u ndal")    
    except BrokenPipeError:
            print('\nServeri eshte down')   
    except ConnectionRefusedError:
        print("Nuk mund te krijohet lidhja me serverin")                        
    finally:
        sock.close()
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
    except TypeError:
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
:::'##::::'##:'########::'########::::::::::::'######::'##:::::::'####:'########:'##::: ##:'########:'####::::: 
::: ##:::: ##: ##.... ##: ##.... ##::::::::::'##... ##: ##:::::::. ##:: ##.....:: ###:: ##:... ##..::. ##:::::: 
::: ##:::: ##: ##:::: ##: ##:::: ##:::::::::: ##:::..:: ##:::::::: ##:: ##::::::: ####: ##:::: ##::::: ##:::::: 
::: ##:::: ##: ##:::: ##: ########::'#######: ##::::::: ##:::::::: ##:: ######::: ## ## ##:::: ##::::: ##:::::: 
::: ##:::: ##: ##:::: ##: ##.....:::........: ##::::::: ##:::::::: ##:: ##...:::: ##. ####:::: ##::::: ##:::::: 
::: ##:::: ##: ##:::: ##: ##::::::::::::::::: ##::: ##: ##:::::::: ##:: ##::::::: ##:. ###:::: ##::::: ##:::::: 
:::. #######:: ########:: ##:::::::::::::::::. ######:: ########:'####: ########: ##::. ##:::: ##::::'####::::: 
::::.......:::........:::..:::::::::::::::::::......:::........::....::........::..::::..:::::..:::::....::::::
""")
host = hosti()
port = porti()
connect(host, port)