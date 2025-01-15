import socket
import struct
from config import listen_broadcast_port, receive_offer_size, magic_cookie, offer_message_type



class OfferSeeker:
    
    def __init__(self):
        self.servers_address = None
        self.server_port_tcp = None
        self.server_port_udp = None
        self.data = None
    
    def seek_for_offer(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        soc.bind(("", listen_broadcast_port))
        while True:
            try:
                data, addr = soc.recvfrom(receive_offer_size)
                self.servers_address = addr[0]
                server_magic_cookie, server_offer_message_type, udp_port, tcp_port = struct.unpack('!IBHH', data)
                server_magic_cookie = hex(server_magic_cookie)
                server_offer_message_type = hex(server_offer_message_type)
                if server_magic_cookie != magic_cookie or \
                    server_offer_message_type != offer_message_type:
                    continue
                print("Received offer from ", addr)
                self.server_port_tcp = tcp_port
                self.server_port_udp = udp_port
                break
            except Exception as e:
                print(f"Error in receiving offer: {e}")
                continue
        