#a.write a server side program in such a way that it should accept a msg from client side program and give reply to the client msg.
#ChatServer.py
import socket
s=socket.socket()
s.bind(("127.0.0.1",8558))
s.listen(2)
while(True):
	cs,ca=s.accept()
	csdata=cs.recv(1024).decode()
	print("Friend---->:{}".format(csdata))
	ssdata=input("Sneha--->:")
	cs.send(ssdata.encode())
