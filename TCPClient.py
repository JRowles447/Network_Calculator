from socket import *

while True:
    serverName = '127.0.0.1'
    serverPort = 61012
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # Connect to the server
    clientSocket.connect((serverName, serverPort))
    # Read operation from the user
    operation = input('Input operator and two integers:')
    # Send the encoded request
    clientSocket.send(str(operation).encode())
    result = clientSocket.recv(1024)
    # Print response
    print('Result From Server: ' + result.decode().split(' ')[1] + " Status: " + result.decode().split(' ')[0])

