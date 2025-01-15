from abc import ABC, abstractmethod

class BaseRequest(ABC):
    
    @abstractmethod
    def __init__(self):
        self.magic_cookie:str
        self.message_type:str
        self.file_size:int
        