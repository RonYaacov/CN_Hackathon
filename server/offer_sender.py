import socket
from time import sleep
from config import broadcast_interval, broadcast_address


class OfferSender:
    def __init__(self, server_address:str, offer_msg:str):
        self.offer_msg = offer_msg
        self.server_address = server_address
    
    def send_offer(self):
        broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        while True:
            try:
                broadcast_socket.sendto(self.offer_msg.encode(), broadcast_address)
                sleep(broadcast_interval)
                continue
            except KeyboardInterrupt:
                print("Broadcasting stopped.")
                broadcast_socket.close()
                break      
