#B.Write a client side program in such a way that it must accept a number from the keyboard, send to the server side program and get its square from the server side program.
#ClientSquare.py
import socket
s=socket.socket()
s.connect(("localhost",8888))
print("Client Got Connection Server:")
#accept the number from KEy Board
n=input("Enter a Number for Getting Its Square:")
s.send(n.encode())
ssdata=s.recv(1024).decode()
print("Square({})={}".format(n,ssdata))