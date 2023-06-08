from socket import *
import threading
import tkinter as tk

serverSocket = socket(AF_INET,SOCK_STREAM)
connectionSocket=None
def startServer():
	print (server_Port_Input.get())
	serverSocket.bind(('127.0.0.1',int(server_Port_Input.get())))
	serverSocket.listen(1)
	global connectionSocket
	connectionSocket, addr = serverSocket.accept()
	t1 = threading.Thread(target=rcv).start()

def callStartServer():
	t1=threading.Thread(target=startServer).start()


def rcv():
	while True:
		sentence = connectionSocket.recv(1024).decode()
		if sentence:
			print('\nClient: ', sentence)
			message_view.insert(tk.END,'Client : '+sentence+'\n')
		else:
			return
		
def snd(val):
		sentence= val
		connectionSocket.send(sentence.encode())
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

t2 = threading.Thread(target=snd).start()   