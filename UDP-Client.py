from socket import *
serverName = 'hostname'
serverPort = 12000

# Make Socket
# TCP is SOCK_STREAM, UDP is SOCK_DGRAM
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get Input from User
message = input('Input lowercase sentence:')

# Do Encode from User input becasue all OS uses diffrent encoding way
# send message using serverName and serverPort
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Waiting until receiving data from client Socket. under 2048
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# decoding and print
print(modifiedMessage.decode())

# close Socket
clientSocket.close()
