import socket
from threading import Thread
import tkinter
from textwrap import wrap
from connect import *
 

#Funksioni qe menaxhon pranimin e mesazheve nga serveri
def pranimi():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode()
            #Mesazhin e pranuar e ndan ne nje varg mesazh me gjatesi 100 karakteresh
            msg = wrap(msg, 110)
            for item in msg:
              #Mesazhet i vendos ne fund te dritares
              msg_list.insert(tkinter.END , item)
        #Shikon per gabime
        #Zakonisht paraqitet ky exception kur clienti mbyll lidhjen
        except OSError:  
            break

#Funksioni qe menaxhon dergimin e mesazheve te serveri
def dergo(event=None): 
    #Mer vleren qe ndodhet ne textbox
    msg = my_msg.get()
    #Pastron inputin ne tekstbox
    my_msg.set("") 
    #Dergon vleren nga tekstboxi ne server 
    client_socket.send(bytes(msg, "utf8"))
    #Kontrollon se mos mesazhi ishte quit
    if msg == "{quit}":
        #Mbyll socketin
        client_socket.close()
        #Mbyll dritaren
        top.quit()

#Funksioni per menaxhimin e mbylljes se lidhjes
def mbyll(event=None):
    my_msg.set("{quit}")
    #Dergon ne server mesazhin {quit}
    dergo()


#Kerkojme hostin dhe portin ne te cilin duam te konektohemi 
HOST = hosti()
PORT = porti()
BUFSIZ = 1024
ADDR = (HOST, PORT)
#Krijojme socketin
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)


#Faqja fillestare e applikacionit
top = tkinter.Tk()
#Titulli i faqes
top.title("FIEK Chat")
messages_frame = tkinter.Frame(top)
#Variabla ku ruhet inputi
my_msg = tkinter.StringVar() 
#Vlera fillestare
my_msg.set("Shkruaj ketu...")
#Krijimi i nje scrollbari
scrollbar = tkinter.Scrollbar(messages_frame)  
#Hapsire ku do te shfaqen mesazhet me lartesi 100x30 pixela
msg_list = tkinter.Listbox(messages_frame, height=30, width=100, yscrollcommand=scrollbar.set)
#Vendos scroll bar ne anen e djatht
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
#Vendo hapsiren e mesazheve ne te majte
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()
#Krijimi i hapsires per input
entry_field = tkinter.Entry(top, textvariable=my_msg, width= 80)
#Bene bind nje event dhe theret funksionin dergo
entry_field.bind("<Return>", dergo)
entry_field.pack()
#Krijon nje button per dergim
send_button = tkinter.Button(top, text="Dergo", command=dergo)
send_button.pack()
#Eventi per mbylljen e dritares
top.protocol("WM_DELETE_WINDOW", mbyll)

#Krijojme nje thread te ri
receive_thread = Thread(target=pranimi)
receive_thread.start()
 #Fillon ekzekutimi i GUI-t.
tkinter.mainloop()



