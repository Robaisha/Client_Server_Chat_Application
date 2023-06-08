from socket import *
import threading
import tkinter as tk

clientSocket = socket(AF_INET, SOCK_STREAM)


def connectionEstab(serverName,serverPort):
    print(serverName,serverPort)
    clientSocket.connect((serverName,int(serverPort)))
    t1 = threading.Thread(target=rcv).start()

def rcv():
    while True:
        modifiedSentence = clientSocket.recv(1024)
        print('\nFrom Server: ', modifiedSentence.decode())
        message_view.insert(tk.END,'Server: '+modifiedSentence.decode()+'\n')

def snd(val):
    sentence = val
    print(sentence)
    clientSocket.send(sentence.encode())
    message_view.insert(tk.END,'Client : '+val+'\n')
    input_box_send.delete("0",tk.END)

root = None
message_view=None


root= tk.Tk();
port=0
server=''
label = tk.Label(root, text="Enter Client IP (LocalHost):")
server_IP_Input = tk.Entry(root)
label.pack()
server_IP_Input.pack()

label1 = tk.Label(root, text="Enter Port No:")
server_Port_Input = tk.Entry(root)
label1.pack()
server_Port_Input.pack()

button = tk.Button(root,text='Connection', command=lambda: connectionEstab(server_IP_Input.get(),server_Port_Input.get()))
button.pack()





t2 = threading.Thread(target=snd).start()

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


