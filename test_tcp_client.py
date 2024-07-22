import unittest
import socket
import threading
from tcp_client import connect_to_server

class TestTCPClient(unittest.TestCase):
    def setUp(self):
        self.server_thread = threading.Thread(target=connect_to_server)
        self.server_thread.start()

    def tearDown(self):
        self.server_thread.join(timeout=1)  # Wait for client thread to terminate

    def test_server_response(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', 65432))
        server_socket.listen(5)
        
        client_socket, client_address = server_socket.accept()
        client_message = client_socket.recv(1024)
        self.assertEqual(client_message.decode(), "Hello, client!")

        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    unittest.main()

