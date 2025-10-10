import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), "ascii")
        cur_thread = threading.current_thread()
        response=bytes("{}: {}".format(cur_thread.name, data), "ascii")
        self.request.sendall(response)

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, "ascii"))
        response = str(sock.recv(1024))
        print(f"Received: {response}")

if __name__ == "__main__":
    HOST , PORT = "localhost", 0
    server = socketserver.ThreadingTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with server:
        ip, port = server.server_address

        # Start a thread with the server
        # that thread will then start one more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread: ", server_thread.name)

        client(ip, port, "HELLO world 1")
        client(ip, port, "Hello World 2")
        client(ip, port, "Hello World 2")

        server.shutdown()