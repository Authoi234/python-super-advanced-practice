import socket

HOST = "portfolio.jacksargey.com"
PORT = 443

s = socket.socket()
s.connect((HOST, PORT))
command = "GET / HTTP/1.1\nHost: portfolio.jacksargey.com\nConnection:close\n\n"
s.send(command.encode())

while True:
    data = s.recv(512)
    if data == b'':
        break
    print(data.decode())

s.close()