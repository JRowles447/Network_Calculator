from socket import *


serverPort = 61012
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('SERVER IS READY TO RECEIVE')

while True:
    connectionSocket, addr = serverSocket.accept()
    # TODO change this for numeric and op
    # connectionSocket.close()

    operation = connectionSocket.recv(1024).decode().split(' ')

    # TODO checks
    # TODO some stuff (AKA the calculations)
    result = 0


    connectionSocket.send(str(result).encode())
    connectionSocket.close()