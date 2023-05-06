from socket import *
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

# 생성한 ServerSocket을 포트 넘버와 Binding
serverSocket.bind(("", serverPort))

print("The Server is ready to receive")

while True:
  message, clientAddress = serverSocket.recvfrom(2048)
  modifiedMessage = message.decode().upper()
  serverSocket.sendto(modifiedMessage.encode(), clientAddress)
  print('Success!!')