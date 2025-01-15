import struct
import time
from abstractions.base_request import BaseRequest
from abstractions.base_request_handler import BaseRequestHandler
from socket import socket, AF_INET, SOCK_DGRAM
from config import receive_file_max_size, magic_cookie, payload_message_type, request_message_type

class UdpRequestHandler(BaseRequestHandler):
    
    def __init__(self, server_ip:str, server_port:int):
        super().__init__(server_ip, server_port)
        self.connection_socket = socket(AF_INET, SOCK_DGRAM)
        self.connection_socket.settimeout(1)
        self.bytes_received = 0
        
    def connect(self):
        pass
    
    def send(self, request:BaseRequest):
        msg = self.create_request_message(int(request.file_size))
        self.connection_socket.sendto(msg, (self.server_ip, self.server_port))
        self.send_time = time.time()
        
        
    def receive(self)->int:
        while True:
            try:
                bytes_from_server, addr = self.connection_socket.recvfrom(receive_file_max_size)
                server_magic_cookie, server_message_type, total_segments, current_segment = struct.unpack('!IBQQ', bytes_from_server[:21])
                payload = struct.unpack(f"{len(bytes_from_server)-21}s",bytes_from_server[21:]) 
                if server_magic_cookie != int(magic_cookie, 16) or \
                    server_message_type != int(payload_message_type, 16):
                    continue
                self.bytes_received += (len(payload[0]))
                if current_segment == total_segments:
                    return time.time() - self.send_time
            except Exception:
                return time.time() - self.send_time
                
        
        
    def create_request_message(self, file_size:int)->bytes:
        
        return struct.pack(f"!IBQ", int(magic_cookie, 16), int(request_message_type, 16), file_size)

