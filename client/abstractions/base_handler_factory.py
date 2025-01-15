from abc import ABC, abstractmethod
from socketserver import BaseRequestHandler
from enums.connection_type_enum import ConnectionTypeEnum


class BaseHandlerFactory(ABC):
    
    @abstractmethod
    def get_handler(self, connectionType:ConnectionTypeEnum)->BaseRequestHandler:
        pass