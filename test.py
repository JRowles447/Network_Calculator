from socket import *
import unittest


serverName = '127.0.0.1'
serverPort = 61012
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

class TestStringMethods(unittest.TestCase):

    # test the addition operator
    def test_addition1(self):
        operation = "+ 9 1111"
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        self.assertEqual(1120, int(result.decode().split(' ')[1]))
        clientSocket.close()

    def test_addition2(self):
        operation = "+ 0 0"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        self.assertEqual(0, int(result.decode().split(' ')[1]))
        clientSocket.close()

    def test_addition3(self):
        operation = "+ 123 999"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        self.assertEqual(1122, int(result.decode().split(' ')[1]))
        clientSocket.close()

    # test the subtraction operator
    def test_subtraction(self):
        operation = "- 9 1"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        self.assertEqual(8, int(result.decode().split(' ')[1]))
        clientSocket.close()

        operation = "- 0 0"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        clientSocket.close()
        self.assertEqual(0, int(result.decode().split(' ')[1]))

        operation = "- 53 21"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        self.assertEqual(32, int(result.decode().split(' ')[1]))
        clientSocket.close()

    # test the multiplication * operator
    def test_multiplication(self):
        operation = "* 9 1"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        self.assertEqual(9, int(result.decode().split(' ')[1]))
        clientSocket.close()

        operation = "* 0 0"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        self.assertEqual(0, int(result.decode().split(' ')[1]))
        clientSocket.close()

        operation = "* 53 0"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        self.assertEqual(0, int(result.decode().split(' ')[1]))
        clientSocket.close()

        operation = "* 29 2"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        self.assertEqual(58, int(result.decode().split(' ')[1]))
        clientSocket.close()

        operation = "* 5 7"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        self.assertEqual(35, int(result.decode().split(' ')[1]))
        clientSocket.close()

    # test the division "/" operator
    def test_division(self):
        operation = "/ 9 1"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        clientSocket.close()
        self.assertEqual(str(9.0), result.decode().split(' ')[1])

        # divide 0 by another int
        operation = "/ 0 12"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        clientSocket.close()
        self.assertEqual(str(0.0), result.decode().split(' ')[1])

        operation = "/ 3 2"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        clientSocket.close()
        self.assertEqual(str(1.5), result.decode().split(' ')[1])

        operation = "/ 30 6"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        clientSocket.close()
        self.assertEqual(str(5.0), result.decode().split(' ')[1])

        operation = "/ 1000 10"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        clientSocket.close()
        self.assertEqual(str(100.0), result.decode().split(' ')[1])

    # test divide by zero
    def test_invalid_divide_by_zero(self):
        operation = "/ 29183 0"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        clientSocket.close()
        self.assertEqual(-1, int(result.decode().split(' ')[1]))
        self.assertEqual(300, int(result.decode().split(' ')[0]))

    # test invalid operator
    def test_invalid_operator(self):
        operation = "q 929 32"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        clientSocket.close()
        self.assertEqual(-1, int(result.decode().split(' ')[1]))
        self.assertEqual(300, int(result.decode().split(' ')[0]))

    # test invalid non-integer operands
    def test_invalid_operands(self):
        operation = "+ k 63"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        clientSocket.close()
        self.assertEqual(-1, int(result.decode().split(' ')[1]))
        self.assertEqual(300, int(result.decode().split(' ')[0]))

        operation = "+ 371 /"
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(str(operation).encode())
        result = clientSocket.recv(1024)
        clientSocket.close()
        self.assertEqual(-1, int(result.decode().split(' ')[1]))
        self.assertEqual(300, int(result.decode().split(' ')[0]))

if __name__ == '__main__':
    unittest.main()
