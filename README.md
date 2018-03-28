# Network_Calculator
<!-- add description of the project (the goal) -->
Network_Calculator contains code to run a TCP server and client and UDP server and client. The client provides the server with an operator and two operands and the server acts as a calculator and returns the result of the operation. In the case of the UDP server and client, the user specifies the drop rate (to simulate unreliability of UDP and the Network layer).

<!-- description of files -->
## File Directory
Description of the files within the directory:
+ README.md: Contains helpful information on the project.
+ TCPClient.py: Contains the client-side code for the TCP protocol.
+ TCPServer.py: Contains the server-side code for the TCP protocol.
+ TCPTest.py: Contains the test code for implementation of TCP.
+ UDPClient.py: Contains the client-side code for the UDP protocol.
+ UDPServer.py: Contains the server-side code for the UDP protocol.
+ UDPTest.py: Contains the test code for the implementation of UDP.

<!-- add how to run the program  -->
## Running Network_Calculator
### TCP Protocol
Run the TCP server from the directory with: `python TCPServer.py`

Once the server begins listening and can receive responses, it prints:
`SERVER IS READY TO RECEIVE`    

We can now run the TCP client in a separate terminal with the following command:
`python TCPClient.py`    

The client program will then print:    
`Input operator and two integers:`    
This indicates that the user can enter information.

Information must be entered in the form:
`operator, operand1, operand2` in order for the machine to produce a logical output. For example, suppose the desired calculation to be entered on the calculator is:  `5 * 6`. We would enter this on the command line of the client as `*, 5, 6`. The result would be: `Result From Server: 30 Status: 200`, where `Result from Server` is the calculated value for the computation and `Status` is the status code for the response (200 is OK, 300 is ERROR).

### UDP Protocol
Run the UDP server from the directory with:   
`python UDPServer.py`   

You will then be able to specify the drop rate at the following prompt:   
`Specify drop rate:`    
Which accepts values between 0.0 and 1.0 (where 0 indicates no packet loss and 1 indicates every packet being dropped).

Once the server is set up and can receive responses, it prints:
`SERVER IS READY TO RECEIVE`

We can then run the UDP client from the directory with:
`python UDPClient.py`    
After which time we will receive the same
`Input operator and two integers:` prompt that we received when we were ran the client code for the TCP implementation.

Once the client sends a string of the form: `operator, operand1, operand2`, the server prints the request it received from the client and determines if it will drop the packet, after every timeout exponential backoff occurs (until it reaches a limit of 2.0). Every random number that is generated (and used to determine if the server will drop the packet) is printed as `Generated number: #`. If the timeout value on the client-side reaches 2.0, the client will print: `Server is DEAD`. Otherwise the client will print `Result From Server: # Status: 200` if the request was valid, otherwise it will print: `Result From Server: -1 Status: 300`.

## Description of Design
Description of each component and design decisions:
### TCPServer.py
First, I set up a serverSocket, began listening for requests, and entered a loop. Once the server receives a request it sets up a connection socket, decodes the request, and parses the arguments. There are then several checks to evaluate whether or not the arguments are valid. These checks include:
+ Check for length of three (there must be three arguments (one operator and two operands)). If the length is not three, send back an error status.
+ If the length is three, we check if the operands are numbers, if they are not send back error status.
+ After this, if the operator is '/', we check whether operand2 is 0. If it is we reject and send back an error status as we disallow division by 0.
If all the checks pass, then we perform the evaluation and send the response back through the connection socket.

### TCPClient.py
Enter a loop to allow the user to continuously send requests. Set up the client socket and connect to the server. The client then requests an operation from the user (expecting a format of "operator, operand1, operand2"). Once it receives the input from the user, it encodes the string and sends it to the server via is client socket. The client then waits for a response. When it receives it's response, it parses and prints it.

### UDPServer.py
First, I set up a serverSocket, request the drop rate from the user, and entered a loop. Once the server receives a request it stores the operation and the address of the client, decodes the request, and parses the arguments. The server then generates a random float between 0.0 and 1.0. If the random number is larger than the drop rate, drop the request. Otherwise we perform several checks to evaluate whether or not the arguments are valid. These checks include:
+ Check for length of three (there must be three arguments (one operator and two operands)). If the length is not three, send back an error status.
+ If the length is three, we check if the operands are numbers, if they are not send back error status.
+ After this, if the operator is '/', we check whether operand2 is 0. If it is we reject and send back an error status as we disallow division by 0.
If all the checks pass, then we perform the evaluation and send the response back using the client address (from the initial request).

### UDPClient.py
Enter a loop to allow the user to continuously send requests. The client then requests an operation from the user (expecting a format of "operator, operand1, operand2"). Once it receives the input from the user, it encodes the string and sends it to the server. We then set up d, which is the amount of time that the client waits before retransmitting the request (if there is no response within d seconds). Enter a loop with conditions on the amount of time the client waits for the reply (must reply within 2.0 seconds or it gives up) and whether the previous attempt was a timeout (in which case, we retransmit). Within the loop we set the timeout to d seconds. We then enter a try block where we attempt to read from the client socket. If there is no reply within d seconds, an exception is thrown. During the handling of the exception, we set timedout to True (so we can reenter the loop), double the value of d (since it is exponential backoff), and retransmit the request. We exit the loop one of two ways:
1. We receive a response from the server when d < 2.0 seconds.
2. We do not receive a response from the server (we give up and exit the loop when d > 2.0).   

In case 1, we have that timedout is false (since it exited the loop without encountering the exception code for the timeout). Then we parse and print the result from the server.
In case 2, we timed out and the value of d is larger than 2.0. When this condition is true, we report to the client user that `Server is DEAD`.

## Extensions
Possible extensions to the project include adding support for complex expressions. For example, being able to solve (3*4)/(2+1). We could also add support for more operations (beyond '+', '-', '\*', '\') including operations that do not have an arity 2.

## Testing
Extensive testing was performed over both of the UDP and TCP protocols (found in UDPTest.py and TCPTest.py). For the both, several tests for each of the four operations were performed and the results (the calculated value and the status code) were checked. There was also a test checking that divide by zero was rejected by the server (Result = -1 and Status = 300). A check was also performed to check that invalid operators (i.e. ones that are not '+', '-', '\*', '\') were rejected. Another test was performed to test whether invalid operands (i.e. that the operands are digits and not operators or letters) were rejected. A final check was performed to test whether arguments of an invalid length (e.g. '+, 4' or '8'), were rejected.

## Dependencies
Uses Python version 3.5.3
