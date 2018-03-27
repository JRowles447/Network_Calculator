from socket import *
import time
import select

while True:
    serverName = '127.0.0.1'
    serverPort = 61012
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    operation = input('Input operator and two integers:')

    clientSocket.sendto(str(operation).encode(), (serverName, serverPort))

    d = 0.1
    timedout = True
    while(d < 2.0 and timedout):
        print("in the loop")
        current_time = time.clock()
        print(current_time)
        try:
            timedout = False
            response, addr = clientSocket.recvfrom(1024)
            print(response.decode())
        # print(timedout)

        # d = d * 2
        # read, write, x = select.select([clientSocket], [], [], d)
        # print(read[0])
        # print(write[0])
        # print(x[0])
        #
        # if(read[0] != ""):
        #     print(read[0])
        #     result = clientSocket.recv(1024)
        #     pass
        # else:
        #     # clientSocket.connect((serverName, serverPort))
        #     clientSocket.send(str(operation).encode())
        #     d = d * 2
        #     timedout = True
        except timeout:
            print("EXCEPT")
            timedout = True
            clientSocket.connect((serverName, serverPort))
            clientSocket.send(str(operation).encode())
            d = d* 2.0

    if (d < 1.6 and not timedout):
        print(clientSocket.gettimeout())
        print(d)

        print("START " + response.decode() + " END")
        print('Result From Server: ' + response.decode().split(' ')[1] + " Status: " + response.decode().split(' ')[0])
    else:
        print("IT FAILED")
        print(d)
        print('Request timed out')
# set up a timer