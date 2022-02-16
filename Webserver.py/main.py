#from socket import *

#serverName = 'localhost'
#serverPort = 6565
#serverSocket = socket(AF_INET, SOCK_STREAM)
#serverSocket.bind(('',serverPort))
#serverSocket.listen(1)
#print ("The server is ready to receive")
#while 1:
#    connectionSocket, addr = serverSocket.accept()
#    sentence = connectionSocket.recv(1024)
#    capitalizedSentence = sentence.upper()
#    connectionSocket.send(capitalizedSentence)
#    connectionSocket.close()

#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('', 1098))
serverSocket.listen(1)
while True:
    print ('Ready to serve...')
    #Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        #Send one HTTP header line into socket
        #header = '\nHTTP/1.1 200 OK\n\n'
        connectionSocket.sendall(str.encode("HTTP/1.0 200 OK\n",'iso-8859-1'))
        connectionSocket.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
        connectionSocket.send(str.encode('\r\n'))

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send(b'\r\n\r\n')

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        errorMessage = '<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n'
        connectionSocket.send(errorMessage.encode())
        connectionSocket.send(b'\r\n\r\n')

serverSocket.close()




