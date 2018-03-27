from socket import *
from random import *

serverPort = 61012
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
# serverSocket.listen(1)

# User enter drop rate
dropRate = float(input("Specify drop rate: "))
print('SERVER IS READY TO RECEIVE')

while True:
    # connectionSocket, addr = serverSocket.accept()
    operation, clientAddress = serverSocket.recvfrom(1024)
    operation = operation.decode().split(', ')
    print(operation)
    # generate a real number between 0 and 1
    dropDraw = random()
    print("Drop rate is: " + str(dropRate))
    print("Generated number: " + str(dropDraw))
    # service if the draw number is above drop rate
    if(dropDraw > dropRate):

        print(operation)
        op = operation[0]
        print(operation[1])
        print(operation[1] + " is operable?    ")
        print(operation[1].isdigit())
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
                serverSocket.sendto(str(result).encode(), clientAddress)
    # connectionSocket.close()