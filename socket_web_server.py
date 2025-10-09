from socket import *

HOST = "localhost"
PORT = 8888

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("localhost", 8888))
server_socket.listen(5)

try:
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    while True:
        print("Server is ready to receive request!")
        client_socket, address = server_socket.accept()
        print("Client Address", address)
        request_data = client_socket.recv(1024)
        request_data = request_data.decode()
        print()
        print("Request Data:")
        print(request_data)

        response_data = "HTTP/1.1 200 OK\n\r"
        response_data += "Content-Type: text/html; charset=utf-8\r\n\r\n"
        response_data += "<html><body><h1>Hello World!"
        response_data += "</h1><img src='https://images.unsplash.com/photo-1716467891152-1b43a96de578?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWFsZSUyMGNhdHxlbnwwfHwwfHx8MA%3D%3D'></body></html>\r\n\r\n"
        response_data = response_data.encode()

        client_socket.sendall(response_data)
        client_socket.shutdown(SHUT_RDWR)
except Exception as e:
    print(e)