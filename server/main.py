import socket
import threading
from threading import Thread
from offer_sender import OfferSender
from config import udp_port, tcp_port, FAIL, HEADER, ENDC
from TCP_handler import TCPHandler
from UDP_handler import UDPHandler

# List to keep track of all threads
threads = []
shutdown_event = threading.Event()

def main():
    try:
        ip = _get_ip_address()
    except socket.error as e:
        print(f"{FAIL}Error getting IP address: {e}{ENDC}")
        return
    except Exception as e:
        print(f"{FAIL}An error occurred: {e}{ENDC}")
        return
    
    print(f"{HEADER}Server started, listening on IP address {ip}{ENDC}" )
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
        print(f"{HEADER}Server shutting down.{ENDC}")
        shutdown_event.set()  # Signal the event to stop the program

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

def _start_broadcasting(offer_sender:OfferSender):
    # Create and start the broadcast thread
    broadcast_thread = threading.Thread(target=offer_sender.send_offer, args=(shutdown_event,))
    broadcast_thread.daemon = True  # This ensures the thread will exit when the main program exits
    broadcast_thread.start()
    
    # Add the thread to the list
    threads.append(broadcast_thread)

def _get_ip_address():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))  # Use a public server like Google's DNS
        ip = s.getsockname()[0]
    return ip
    

if __name__ == "__main__":
    main()