#B.Write a client side program in such a way that it should accept a msg from a keyboard,send to the server isde program and get reply
#ChatClient.py
import socket
while(True):
	s=socket.socket()
	s.connect(("127.0.0.1",8558))
	csdata=input("Friend---->")
	if(csdata.lower()=="bye"):
		s.send(csdata.encode())
		break	
	else:
		s.send(csdata.encode())
		ssdata=s.recv(1024).decode()
		print("sneha--->{}".format(ssdata))