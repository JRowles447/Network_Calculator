from socket import *
import select

while True:
    serverName = '127.0.0.1'
    serverPort = 61012
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # clientSocket.connect((serverName, serverPort))
    operation = input('Input operator and two integers:')

    clientSocket.sendto(str(operation).encode(), (serverName, serverPort))

    # clientSocket.connect((serverName, serverPort))
    d = 0.1
    result = ""
    timedout = True
    while(d < 2.0 and timedout):
        # clientSocket.settimeout(d)

        try:
            timedout = False
            response, addr = clientSocket.recvfrom (1024)
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
        # result = clientSocket.recv(1024)
        print("START " + result.decode() + " END")
        print('Result From Server: ' + result.decode().split(', ')[1] + " Status: " + result.decode().split(', ')[0])
    else:
        print("IT FAILED")
        print(d)
        print('Request timed out')
# set up a timer