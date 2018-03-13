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

    print(operation)
    result = "empty"
    op = operation[0]

    # Check if the operands are digits
    if(not operation[1].isdigit() or not operation[2].isdigit()):
        result = "operand(s) not digits"
        connectionSocket.send(str(result).encode())
    # operands entered are digits, cast
    operand1 = int(operation[1])
    operand2 = int(operation[2])

    # Check that OC is valid
    if(op != '+' and op != '-' and op != '/' and op != '*'):
        result = "bad request"
        connectionSocket.send(str(result).encode())

    # Check for divide by zero
    if (op == '/' and operand2 == 0):
        result = "bad request, divide by zero"
        connectionSocket.send(str(result).encode())

    # Request is valid, compute and send to client
    else:
        result = "good request"
        if(op == "+"):
            result = str(operand1 + operand2)
        elif(op == "-"):
            result = str(operand1 - operand2)
        elif(op == "*"):
            result = str(operand1 * operand2)
        # operator is /
        else:
            result = str(operand1 / operand2)
        connectionSocket.send(str(result).encode())

    # TODO checks
    # TODO some stuff (AKA the calculations)


    connectionSocket.send(str(result).encode())
    connectionSocket.close()