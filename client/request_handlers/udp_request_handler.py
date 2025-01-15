import time
from abstractions.base_request import BaseRequest
from abstractions.base_request_handler import BaseRequestHandler
from socket import socket, AF_INET, SOCK_DGRAM
from config import receive_file_max_size

class UdpRequestHandler(BaseRequestHandler):
    
    def __init__(self, server_ip:str, server_port:int):
        super().__init__(server_ip, server_port)
        self.connection_socket = socket(AF_INET, SOCK_DGRAM)
        self.connection_socket.settimeout(1)
        self.bytes_received = 0
        
    def connect(self):
        pass
    
    def send(self, request:BaseRequest):
        self.connection_socket.sendto(str(request.file_size).encode(), (self.server_ip, self.server_port))
        self.send_time = time.time()
        
    def receive(self)->int:
        while True:
            try:
                bytes_from_server = self.connection_socket.recvfrom(receive_file_max_size)
                self.bytes_received += bytes_from_server.count()
            except TimeoutError:
                return time.time() - self.send_time
            except Exception as e:
                print(f"Error in receiving data from server: {e}")
                continue
        
        
        