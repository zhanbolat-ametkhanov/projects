import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 65432))
    server_socket.listen(5)
    print("Server is listening on port 65432")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        client_socket.sendall(b"Hello, client!")
        client_socket.close()

if __name__ == "__main__":
    start_server()

