# Network_Calculator
---
<!-- add description of the project (the goal) -->

<!-- description of files -->
## File Directory
----
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
---
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
---

## Testing
---
Extensive testing was preformed over both of the UDP and TCP protocols.
## Dependencies
---
Uses Python version 3.5.3





<!-- For our examples we test
Once the server waits and -->
<!-- add description of the program (the goal) and design FOR CLASS -->

<!-- Extensions/ improvements -->

<!-- add description of the tests -->


<!-- Page or so of description of overall design, how it works, and tradeoffs considered and made. Improvements or extensions (and how they can be made). Instructions on how to run the program -->


<!-- 3. Description of tests ran on programs. -->
