from socket import *
import time
import select

while True:
    serverName = '127.0.0.1'
    serverPort = 61012
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.setblocking(0)
    operation = input('Input operator and two integers:')

    clientSocket.sendto(str(operation).encode(), (serverName, serverPort))

    d = 0.1
    timedout = True
    while(d < 2.0 and timedout):
        clientSocket.settimeout(d)
        print("in the loop")
        current_time = time.clock()
        print(current_time)
        try:
            timedout = False
            # time.sleep(d)
            response, addr = clientSocket.recvfrom(1024)
            print(response.decode())
        # No response in the timer, loop back and send again
        except timeout:
            timedout = True
            d = d * 2
            clientSocket.sendto(str(operation).encode(), (serverName, serverPort))

    if (d < 1.6 and not timedout):
        print(d)
        print("START " + response.decode() + " END")
        print('Result From Server: ' + response.decode().split(' ')[1] + " Status: " + response.decode().split(' ')[0])
    else:
        print("IT FAILED")
        print(d)
        print('Request timed out')
# set up a timer