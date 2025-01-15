from abc import ABC, abstractmethod
from typing import Optional
from abstractions.base_request import BaseRequest
from socket import socket

class BaseRequestHandler(ABC):
    
    @abstractmethod
    def __init__(self, ip:str, port:int):
        self.ip = ip
        self.port = port
        self.send_time = 0
        self.receive_time = 0
        self.connection:socket = None
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
