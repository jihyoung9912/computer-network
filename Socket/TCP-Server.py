from socket import *
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

# client로부터의 연결을 하나만 기다리겠다. 동시에 여러개의 요청이 있을 수 있기 때문.
serverSocket.listen(1)

print('The Server is ready to receive')

while True:
  # Client로부터 요청이 온다면 socket을 생성하여 return
  connectionSocket, addr = serverSocket.accept()
  
  sentence = connectionSocket.recv(1024).decode()
  capitalizedSentence = sentence.upper()
  connectionSocket.send(capitalizedSentence.encode())
  print('Success!!')
  
  connectionSocket.close()