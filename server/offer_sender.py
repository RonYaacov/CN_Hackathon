import socket
from time import sleep
from config import broadcast_interval, broadcast_address
from formats import create_offer_message

class OfferSender:
    def __init__(self, udp_port, tcp_port):
        # Create the offer message once during initialization
        self.offer_msg = create_offer_message(udp_port, tcp_port)
    
    def send_offer(self, shutdown_event):
        """
        Broadcast the offer message at regular intervals until the shutdown event is set.
        
        Args:
            shutdown_event (threading.Event): An event to signal when to stop broadcasting.
        """
        # Create a UDP socket for broadcasting
        broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Broadcast the offer message at regular intervals until shutdown_event is set
        while not shutdown_event.is_set():
            broadcast_socket.sendto(self.offer_msg, broadcast_address)
            sleep(broadcast_interval)
        
        # Close the socket when done
        broadcast_socket.close()
        print("Broadcasting stopped.")
        
