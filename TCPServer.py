from socket import *


serverPort = 61012
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('SERVER IS READY TO RECEIVE')

while True:
    connectionSocket, addr = serverSocket.accept()
    operation = connectionSocket.recv(1024).decode().split(' ')

    print(operation)
    op = operation[0]

    # Check if the operands are digits
    operable =not(not operation[1].isdigit() or not operation[2].isdigit())
    if(not operable):
        result = "300 -1"
        connectionSocket.send(str(result).encode())

    # operands entered are digits, cast
    if(operable):
        operand1 = int(operation[1])
        operand2 = int(operation[2])

    # Check that OC is valid
    if(op != '+' and op != '-' and op != '/' and op != '*'):
        result = "300 -1"
        connectionSocket.send(str(result).encode())

    # Check for divide by zero
    if (op == '/' and operand2 == 0):
        result = "300 -1"
        connectionSocket.send(str(result).encode())

    # Request is valid, compute and send to client
    else:
        result = "good request"
        if(op == "+"):
            result = "200 " + str(operand1 + operand2)
        elif(op == "-"):
            result = "200 " + str(operand1 - operand2)
        elif(op == "*"):
            result = "200 " + str(operand1 * operand2)
        # operator is /
        else:
            result = "200 " + str(operand1 / operand2)
        connectionSocket.send(str(result).encode())
    connectionSocket.close()