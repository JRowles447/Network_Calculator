from socket import *
import select

while True:
    serverName = '127.0.0.1'
    serverPort = 61012
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    operation = input('Input operator and two integers:')
    d = .1
    clientSocket.send(str(operation).encode())
    while(d < 2):
        clientSocket.settimeout(d)

        d = d * 2
        # read, write, x = select.select(clientSocket, [], [], d)
        # if(read != ""):
        #     pass
        # else:
        #     d = d * 2
    if (d < 2):
        result = clientSocket.recv(1024)
        print('Result From Server: ' + result.decode().split(' ')[1] + " Status: " + result.decode().split(' ')[0])
    else:
        print(d)
        print('Request timed out')
# set up a timer