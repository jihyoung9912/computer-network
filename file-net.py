import os
import sys
import socket


HOST = ''
PORT = int(sys.argv[1])
MAX_SIZE = 1024


def get_file(con, filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
            con.sendall(data) 
    except FileNotFoundError:
        con.sendall(b'FILE NOT FOUND\r\n')


def put_file(con, filename, data):
    with open(filename, 'wb') as f:
        f.write(data)
        while True:
            temp = con.recv(MAX_SIZE)
            if not temp:
                break
            f.write(temp)


def ls_file(con, ext):
    files = [f for f in os.listdir() if f.endswith(ext)]  # 현재 디렉토리에서 확장자가 ext인 파일 목록을 가져옵니다.
    for filename in files:
        con.sendall(f"{filename}\r\n".encode())


def handle_connection(ans, con, temp):
    if ans[0] == "GET":
        get_file(con, ans[1])
    elif ans[0] == "PUT":
        data = b"\n".join(temp[1:])
        put_file(con, ans[1],data)
    elif ans[0] == "LS":
        ls_file(con, ans[1])


if __name__ == '__main__':
    print("Student-ID: 20180084")
    print("Name: JiHyung Kim")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()

    while True:
        con, addr = s.accept()
        with con:
            temp = con.recv(MAX_SIZE)
            if not temp:
                continue
            temp = temp.splitlines()
            ans = temp[0].decode().split()
            handle_connection(ans, con, temp)
