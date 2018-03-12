from socket import *

#TODO what about servername?
serverName = '127.0.0.1'
serverPort = 61012
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input operator and two integers:')
clientSocket.send(str(sentence).encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()