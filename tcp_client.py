import socket

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65432))
    message = client_socket.recv(1024)
    print("Alyndy:", message.decode())
    client_socket.close()

if __name__ == "__main__":
    connect_to_server()

