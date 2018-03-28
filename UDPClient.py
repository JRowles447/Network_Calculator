from socket import *

while True:
    serverName = '127.0.0.1'
    serverPort = 61012
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.setblocking(0)
    operation = input('Input operator and two integers:')

    clientSocket.sendto(str(operation).encode(), (serverName, serverPort))

    d = 0.1
    timedout = True
    # Request and retransmit request until we receive response or the timeout (d) reaches 2.0
    while(d < 2.0 and timedout):
        clientSocket.settimeout(d)
        try:
            timedout = False
            response, addr = clientSocket.recvfrom(1024)
            # print(response.decode())
        # No response in the timer, loop back and send again
        except timeout:
            timedout = True
            d = d * 2
            # Retransmit the request
            clientSocket.sendto(str(operation).encode(), (serverName, serverPort))

    # There is a response from the server within the exponential backoff time
    if (d < 2.0 and not timedout):
        print('Result From Server: ' + response.decode().split(' ')[1] + " Status: " + response.decode().split(' ')[0])
    # There is no response from the server within the allocated time
    else:
        print("Server is DEAD")