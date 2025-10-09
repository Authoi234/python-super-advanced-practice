import socket

HOST = "localhost"
PORT = 8888

s = socket.socket()
s.connect((HOST, PORT))
command = "GET / HTTP/1.1\nHost: localhost\nConnection:close\n\n"
s.send(command.encode())

while True:
    data = s.recv(512)
    if data == b'':
        break
    print(data.decode())

s.close()