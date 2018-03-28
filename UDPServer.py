from socket import *
from random import *

serverPort = 61012
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

# User enter drop rate
dropRate = float(input("Specify drop rate: "))
print('SERVER IS READY TO RECEIVE')

while True:
    operation, clientAddress = serverSocket.recvfrom(1024)
    print("Request from client is: " + str(operation.decode()))
    operation = operation.decode().split(', ')

    # generate a real number between 0 and 1
    dropDraw = random()
    print("Drop rate is: " + str(dropRate))
    print("Generated number: " + str(dropDraw))

    # service if the draw number is above drop rate
    if(dropDraw > dropRate):
        operable = False
        # check that there are three arguments
        if(len(operation) != 3):
            result = "300 -1"
            serverSocket.sendto(str(result).encode(), clientAddress)

        else:
            op = operation[0]

            # Check if the operands are digits
            operable =not(not operation[1].isdigit() or not operation[2].isdigit())
            if(not operable):
                result = "300 -1"
                serverSocket.sendto(str(result).encode(), clientAddress)

        # operands entered are digits, cast
        if(operable):
            operand1 = int(operation[1])
            operand2 = int(operation[2])

            # Check that OC is valid
            if(op != '+' and op != '-' and op != '/' and op != '*'):
                result = "300 -1"
                serverSocket.sendto(str(result).encode(), clientAddress)

            # Check for divide by zero
            if (op == '/' and operand2 == 0):
                result = "300 -1"
                serverSocket.sendto(str(result).encode(), clientAddress)

            # Request is valid, compute and send to client
            else:
                if(op == "+"):
                    result = "200 " + str(operand1 + operand2)
                elif(op == "-"):
                    result = "200 " + str(operand1 - operand2)
                elif(op == "*"):
                    result = "200 " + str(operand1 * operand2)
                # operator is /
                else:
                    result = "200 " + str(operand1 / operand2)
                serverSocket.sendto(str(result).encode(), clientAddress)
