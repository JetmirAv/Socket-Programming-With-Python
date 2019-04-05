import socket
import sys
import datetime
import random
from _thread import *

host = 'localhost'
port = 8888

#EMRIKOMPJUTERIT
def EMRIKOMPJUTERIT():
    print(s.getsockname())
    return s.getsockname()[0]
# BASHKETINGELLORE
def BASHKETINGELLORE(input):
    #vowel_list = set(['a','e','i','o','u'])
    #vowels = 0
    #for char in input:
     #   if char in vowel_list:
     #       vowels += 1
    #return vowels
    vowels=0
    for i in input:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    return vowels
#Fibonacci
def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci(n-1)+Fibonacci(n-2)
#KOHA
def KOHA():
    print(datetime.datetime.now().strftime("Date: %Y-%m-%d \nTime: %H:%M"))
#LOJA
def LOJA():
    for x in range(7):
        print(random.randint(1,49))
#PRINTIMI
def PRINTIMI(input):
    return input
#KONVERTIMI
def KONVERTIMI(num, value):
    if num == 1:
        print(value*1.34102)
    elif num == 2: 
        print(value*0.7457)
    elif num == 3:
        print(value*0.0174533)
    elif num == 4:
        print(value*57.2958)
    elif num == 5:
        print(value*3.78541)
    elif num == 6:
        print(value*0.264172)
    else:
        print("Invalid Value")





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    s.bind((host, port))
except socket.error:
    print("Bind error")

s.listen(10)

def clientthread(conn, addr):
    welcome =   "Welcome to the server.\n"
    conn.send(welcome.encode())

    while True:
        data = conn.recv(1024) 
        if not data:
            break
        print("Server received data:", data)
        data = data.upper()
        data = data.decode()
        print(data)
        method = data.split(" ")[0]
        if method == "FIBONACCI":
            if data.split(" ")[1] == '':
                MESSAGE = "You must enter a number after Fibonacci"
            else:
                MESSAGE = str(Fibonacci(int(data.split(" ")[1])))
        elif method == "IPADRESA":
            MESSAGE = str(addr[0])
        elif method == "NUMRIIPORTIT":
            MESSAGE = str(addr[1])
        elif method == "EMRIKOMPJUTERIT":
             MESSAGE = str(s.getsockname()[0])
        elif method == "BASHKETINGELLORE":
            if(data.split(" ")[1] == ''):
                MESSAGE = 'You must enter a text afer Bashketingellore.'
            else: 
                print(data.split("BASHKETINGELLORE"))
                MESSAGE = str(BASHKETINGELLORE(data.split("BASHKETINGELLORE")[1]))
        
        else: 
           MESSAGE = "We dont know what to do with your request"
        print(MESSAGE)
        if MESSAGE == 'exit':
            break
        conn.send(str.encode(MESSAGE))  # echo 
    conn.close()        



while 1:
    conn, addr = s.accept()
    print("Connected with " + str(addr[0]) + ":" + str(addr[1]))
    start_new_thread(clientthread, (conn, addr)) 


s.close()