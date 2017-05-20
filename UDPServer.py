from socket import*
serverPort=12000
host=''
serverSocket=(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print "the server is ready to receive"
while true:
    message,clientAddress=serverSocket.recvfrom(2048)
    modifiedMessage=message.upper()
    serverSocket.sendto(modifiedMessage,clientAddress)
