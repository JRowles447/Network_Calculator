from socket import *

#TODO what about servername?
serverName = '127.0.0.1'
serverPort = 61012
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
operation = input('Input operator and two integers:')
clientSocket.send(str(operation).encode())
result = clientSocket.recv(1024)
print('From Server: ', result.decode())
clientSocket.close()