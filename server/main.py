import socket
from offer_sender import OfferSender


def main():
    ip = get_ip_address() 
    print("Server started, listening on IP address", ip)
    offer_sender = OfferSender(get_ip_address(), ip) #the message needs to be change, this is just for testing
    offer_sender.send_offer()# this should be in a thread
    
    
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
    main()