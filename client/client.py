from socket import *
serverName = raw_input('IP Address: ')
serverPort = 12000
while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    print 'Waiting for input...'
    command = raw_input('')
    clientSocket.send(command)
    command = command.split()
    if command[0] == 'LIST':
        print clientSocket.recv(1024)
    elif command[0] == 'RETR':
        print clientSocket.recv(1024)
        filename = command[1]
        file = open(filename, 'wb')
        bytefile = clientSocket.recv(1024)
        while(bytefile):
            bytefile = clientSocket.recv(1024)
            file.write(bytefile)           
        file.close()
        print ('Complete')
    else:
		filename = command[1]
		try:
			file = open(filename, 'rb')
			clientSocket.send('BETUL')
			print clientSocket.recv(1024)
			bytefile = file.read(1024)
			clientSocket.send(bytefile)
			while (bytefile):
			    clientSocket.send(bytefile)
			    bytefile = file.read(1024)
			file.close()
			print ('Complete')
		except IOError:
			clientSocket.send('SALAH')
			print ('452 Error writing file')
    clientSocket.close()
