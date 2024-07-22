import unittest
import socket
import threading
import time
from tcp_server import start_server

class TestTCPServer(unittest.TestCase):
    def setUp(self):
        self.server_thread = threading.Thread(target=start_server)
        self.server_thread.start()
        time.sleep(1)  # Allow server to start listening

    def tearDown(self):
        self.server_thread.join(timeout=1)  # Wait for server thread to terminate

    def test_client_connection(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 65432))
        message = client_socket.recv(1024)
        client_socket.close()
        self.assertEqual(message.decode(), "Hello, client!")

if __name__ == "__main__":
    unittest.main()

