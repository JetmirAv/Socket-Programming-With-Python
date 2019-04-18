import socket
import sys 
from _thread import *

from clientThread import *

host = 'localhost'
port = 12000
### Krijojm socketin te protokolit TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
### Header per scripten fiek tcp-serveri
    print("""
:::::::::::::::::::::::::::::::::::::::'########:'####:'########:'##:::'##::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ##.....::. ##:: ##.....:: ##::'##:::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ##:::::::: ##:: ##::::::: ##:'##::::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ######:::: ##:: ######::: #####:::::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ##...::::: ##:: ##...:::: ##. ##::::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ##:::::::: ##:: ##::::::: ##:. ##:::::::::::::::::::::::::::::::::::::: 
::::::::::::::::::::::::::::::::::::::: ##:::::::'####: ########: ##::. ##::::::::::::::::::::::::::::::::::::: 
:::::::::::::::::::::::::::::::::::::::..::::::::....::........::..::::..:::::::::::::::::::::::::::::::::::::: 
'########::'######::'########::::::::::::'######::'########:'########::'##::::'##:'########:'########::'####::::
... ##..::'##... ##: ##.... ##::::::::::'##... ##: ##.....:: ##.... ##: ##:::: ##: ##.....:: ##.... ##:. ##:::::
::: ##:::: ##:::..:: ##:::: ##:::::::::: ##:::..:: ##::::::: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##:: ##:::::
::: ##:::: ##::::::: ########::'#######:. ######:: ######::: ########:: ##:::: ##: ######::: ########::: ##:::::
::: ##:::: ##::::::: ##.....:::........::..... ##: ##...:::: ##.. ##:::. ##:: ##:: ##...:::: ##.. ##:::: ##:::::
::: ##:::: ##::: ##: ##:::::::::::::::::'##::: ##: ##::::::: ##::. ##:::. ## ##::: ##::::::: ##::. ##::: ##:::::
::: ##::::. ######:: ##:::::::::::::::::. ######:: ########: ##:::. ##:::. ###:::: ########: ##:::. ##:'####::::
:::..::::::......:::..:::::::::::::::::::......:::........::..:::::..:::::...:::::........::..:::::..::....:::::
Startoi serveri ne %s:%s.
Ne Pritje te kerkesave.   
    """ %(host, port))
    ### Bashkangjesim hostin dhe portin ne te cilin do te punoj serveri
    s.bind((host, port))
    ### Vendosja e numrit se sa kerkesa do te le ne pritje deri sa te refuzoj kerkesen e ardhshme
    s.listen(10)

    while True:
        try:
            ### Presim per lidhje te ndonje serveri
            conn, addr = s.accept()
        ### Kontrolli per gabime     
        except KeyboardInterrupt:
            print('\nJu e ndalet serverin') 
            break       
        print("Connected with " + str(addr[0]) + ":" + str(addr[1]))
        ### Krijimi i nje threadi te veqant per klientin e lidhur
        start_new_thread(clientthread, (conn, addr, s))   
    s.close()
### Kontrolli per gabime      
except KeyboardInterrupt:
    MESSAGE = 'exit'
    conn.send(str.encode(MESSAGE))
    print("\nJu e ndalet serverin")
except ConnectionAbortedError: 
    print("Klienti nderpreu lidhjen me server")       
except socket.error:
    print("Porti eshte duke u perdorur")
 
 




