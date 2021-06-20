### UDP client

import socket

def connectClient(HOST='127.0.0.1', PORT=8000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    return s

def recvStr(s): #s = socket.socket(...)
    data = s.recv(1024)

    return data.decode()

