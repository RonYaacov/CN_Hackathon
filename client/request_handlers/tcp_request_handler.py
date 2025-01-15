import time
from abstractions.base_request_handler import BaseRequestHandler
from socket import socket, AF_INET, SOCK_STREAM
from abstractions.base_request import BaseRequest
from config import receive_file_max_size

class TcpRequestHandler(BaseRequestHandler):
    
    def __init__(self, server_ip:str, server_port:int):
        super().__init__(server_ip, server_port)
    
    def connect(self):
        self.connection_socket = socket(AF_INET, SOCK_STREAM)
        self.connection_socket.connect((self.server_ip, self.server_port))
        
    def send(self, request:BaseRequest):
        message = (str(request.file_size)+"\n").encode("utf-8")
        self.connection_socket.send(message)
        self.send_time = time.time()
    
    def receive(self)->int:
        self.bytes_received = self.connection_socket.recv(receive_file_max_size)
        self.receive_time = time.time()
        return self.receive_time - self.send_time