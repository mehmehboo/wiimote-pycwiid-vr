### UDP server for sending yaw pitch roll between frames
### rather than putting directly into code

import socket

def startServer(HOST=127.0.0.1, PORT=8000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    (conn, addr) = s.accept()
    
    return conn, s ##conn and s are both constantly running


def sendStr(data, conn):
    conn.send(sendData.encode())
