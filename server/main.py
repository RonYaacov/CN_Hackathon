import socket
import threading
from threading import Thread
from offer_sender import OfferSender
from config import udp_port, tcp_port
from TCP_handler import TCPHandler
from UDP_handler import UDPHandler

# List to keep track of all threads
threads = []
shutdown_event = threading.Event()

def main():
    try:
        ip = _get_ip_address()
    except socket.error as e:
        print(f"Error getting IP address: {e}")
        return
        
    print("Server started, listening on IP address", ip)
    offer_sender = OfferSender(udp_port, tcp_port)

    _start_broadcasting(offer_sender)
    tcp_handler = TCPHandler()
    tcp_thread = Thread(target=tcp_handler.listen)
    threads.append(tcp_thread)
    udp_handler = UDPHandler()
    udp_thread = Thread(target=udp_handler.listen)
    threads.append(udp_thread)
    
    tcp_thread.start()
    udp_thread.start()
    
    
    # Keep the main thread alive to allow the broadcast thread to run
    try:
        shutdown_event.wait()  # Wait until the event is set
    except KeyboardInterrupt:
        print("Server shutting down.")
        shutdown_event.set()  # Signal the event to stop the program

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

def _start_broadcasting(offer_sender):
    # Create and start the broadcast thread
    broadcast_thread = threading.Thread(target=offer_sender.send_offer, args=(shutdown_event,))
    broadcast_thread.daemon = True  # This ensures the thread will exit when the main program exits
    broadcast_thread.start()
    
    # Add the thread to the list
    threads.append(broadcast_thread)

def _get_ip_address():
    try:
        # Create a socket and connect to a public server
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Use a public server like Google's DNS
            ip = s.getsockname()[0]
        return ip
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    main()