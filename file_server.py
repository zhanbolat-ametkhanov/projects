import socket

def send_file():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 65432))
    server_socket.listen(1)
    print("Server is listening on port 65432")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    with open('file_to_send.txt', 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    send_file()

