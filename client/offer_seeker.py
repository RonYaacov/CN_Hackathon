import socket
from config import listen_broadcast_port, receive_offer_size



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
                print("Received offer from ", addr)
                print("Offer is: ", data.decode())#need to remove
                self.servers_address = addr[0]
                self.server_port_tcp = int(data.decode().split(":")[1])#this needs to be changed once we have the real msg
                self.server_port_udp = int(data.decode().split(":")[2])#this needs to be changed once we have the real msg
                self.data = data.decode()
                break
            except Exception as e:
                print(f"Error in receiving offer: {e}")
                continue
        