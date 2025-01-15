import socket
from config import listen_broadcast_port, receive_offer_size



class OfferSeeker:
    
    def __init__(self):
        self.servers_address = None
        self.data = None
    
    def seek_for_offer(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        soc.bind(("", listen_broadcast_port))
        while True:
            data, addr = soc.recvfrom(receive_offer_size)
            print("Received offer from ", addr)
            print("Offer is: ", data.decode())#need to remove
            self.servers_address = addr
            self.data = data.decode()
            break
        
        