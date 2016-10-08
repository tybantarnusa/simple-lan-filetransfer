from socket import *
import os
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Server is running...')
while 1:
	connectionSocket, addr = serverSocket.accept()
	command = connectionSocket.recv(1024)
	command = command.split()
	if command[0] == 'LIST':
		file_list = ''
		files = [f for f in os.listdir('.') if os.path.isfile(f)]
		for f in files:
			file_list = file_list + f + '\n'
		connectionSocket.send(file_list)
	elif command[0] == 'RETR':
		connectionSocket.send('125 Data connection already open;\ntransfer starting')
		filename = command[1]
		file = open(filename, 'rb')
		bytefile = file.read(1024)
		connectionSocket.send(bytefile)
		while(bytefile):
			connectionSocket.send(bytefile)
			bytefile = file.read(1024)
		file.close()
	else:
		success = connectionSocket.recv(1024)
		if (success == 'BETUL'):
			connectionSocket.send('125 Data connection already open;\ntransfer starting')
			filename = command[1]
			file = open(filename, 'wb')
			bytefile = connectionSocket.recv(1024)
			while(bytefile):
				bytefile = connectionSocket.recv(1024)
				file.write(bytefile)			
			file.close()
	connectionSocket.close()
