import socket
import threading
from offer_sender import OfferSender
from config import udp_port, tcp_port, ip_address, network_config

# List to keep track of all threads
threads = []
shutdown_event = threading.Event()

def main():
    if not network_config.initialized:
        print("Network configuration failed. Terminating.")
        return
    
    print("Server started, listening on IP address", ip_address)
    offer_sender = OfferSender(udp_port, tcp_port)

    _start_broadcasting(offer_sender)
    
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

if __name__ == "__main__":
    main()