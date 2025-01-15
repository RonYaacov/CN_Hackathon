from socketserver import BaseRequestHandler
from request_handlers.tcp_request_handler import TcpRequestHandler
from request_handlers.udp_request_handler import UdpRequestHandler
from enums.connection_type_enum import ConnectionTypeEnum

class HandlerFactory:
    def __init__(self, server_address:str, server_tcp_port:int, server_udp_port:int):
        self.servers_address = server_address
        self.server_tcp_port = server_tcp_port
        self.server_udp_port = server_udp_port

    def get_handler(self, connectionType:ConnectionTypeEnum)->BaseRequestHandler:
        if connectionType == ConnectionTypeEnum.TCP:
            return TcpRequestHandler(self.servers_address, self.server_tcp_port)
        elif connectionType == ConnectionTypeEnum.UDP:
            return UdpRequestHandler(self.servers_address, self.server_udp_port)
        else:
            return None