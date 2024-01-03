# A.Write a server program in such a way that it accept a numerical value from client side program,it squares the square of the number as a result to the client side program.
#ServerSquare.py
import socket
s=socket.socket()
s.bind(("localhost",8888))
s.listen(2)
print("Server side program ready to acceptany Request:")
while(True):
	try:
		cs,ca=s.accept()
		csdata=cs.recv(1024).decode()
		cval=float(csdata)
		print("Value of Client at Server={}".format(cval))
		res=cval**2
		cs.send(str(res).encode())
	except ValueError:
		cs.send("Don't Enter alnums,str and symbols".en)
