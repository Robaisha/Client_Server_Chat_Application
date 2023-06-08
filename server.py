from socket import *
import threading
import tkinter as tk

serverSocket = socket(AF_INET,SOCK_STREAM)
connectionSockets=[]
def startServer():
    print (server_Port_Input.get())
    serverSocket.bind(('127.0.0.1',int(server_Port_Input.get())))
    serverSocket.listen(10)
    while True:
        connSocket, addr = serverSocket.accept()
        connectionSockets.append(connSocket)
        t1 = threading.Thread(target=rcv, args=(connSocket,))
        t1.start()

def callStartServer():
    t1=threading.Thread(target=startServer)
    t1.start()


def rcv(connSocket):
    while True:
        sentence = connSocket.recv(1024).decode()
        if sentence:
            print('\nClient: ', sentence)
            message_view.insert(tk.END,'Client : '+sentence+'\n')
            broadcast(sentence, connSocket)
        else:
            connSocket.close()
            connectionSockets.remove(connSocket)
            return
        
def broadcast(message, sourceConnSocket):
    for connSocket in connectionSockets:
        if connSocket != sourceConnSocket:
            connSocket.send(message.encode())

def snd(val):
    sentence= val
    broadcast(sentence, None)
    message_view.insert(tk.END,'Server: '+val+'\n')
    input_box_send.delete("0",tk.END)



root = None
message_view=None

root= tk.Tk();
port=0
server=''


label1 = tk.Label(root, text="Enter Port No:")
server_Port_Input = tk.Entry(root)
label1.pack()
server_Port_Input.pack()




button = tk.Button(root,text='Start Server', command=callStartServer)
button.pack()






message_view= tk.Text(root)
message_view.pack()


labelsend = tk.Label(root, text="Enter Message:")
input_box_send = tk.Entry(root)
labelsend.pack()
input_box_send.pack()


buttonsend = tk.Button(root,text='Send Message', command=lambda: snd(input_box_send.get()))
buttonsend.pack()
msg = tk.Message(root, text = input_box_send.get()) 
msg.pack()


root.mainloop()

t2 = threading.Thread(target=snd)
t2.start()
