import socket

defaultHost = 'localhost'
defaultPort = 12000
## Metoda per te zgjedhur hostin              
def hosti():
    try:
        input1 = input("Shkruani host-in me te cilin doni te lidheni.(default %s): " %defaultHost)
        if not input1:
            return ''
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
