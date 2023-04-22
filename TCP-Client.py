from socket import *
serverName = "127.0.0.1"
serverPort = 12000

# TCP is SOCK_STREAM, UDP is SOCK_DGRAM
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# Server connect가 안될 때의 예외처리 추가 필요

sentence = input('Input lowercase sentence: ')

# TCP는 Socket간의 데이터가 내장되어 있기에 그냥 send, recv 함수 사용하면 해당 socket으로부터 받아 옴.
# UDP는 sendTo로 server 정보를 담아 보내야함.
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print('From Server', modifiedSentence.decode())
clientSocket.close()