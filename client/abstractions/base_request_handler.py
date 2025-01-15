from abc import ABC, abstractmethod
from typing import Optional
from abstractions.base_request import BaseRequest
from socket import socket

class BaseRequestHandler(ABC):
    
    def __init__(self, server_ip:str, server_port:int):
        self.server_ip = server_ip
        self.server_port = server_port
        self.send_time = 0
        self.receive_time = 0
        self.connection_socket:socket = None
        self.bytes_received:Optional[int] = None
        
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def send(self, request:BaseRequest):
        pass
    
    @abstractmethod
    def receive(self) ->int:
        pass
