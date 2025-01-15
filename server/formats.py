import struct

# Constants for the offer message
MAGIC_COOKIE = 0xabcddcba  # Unique identifier to validate the message
OFFER_MESSAGE_TYPE = 0x2  # Message type for offer (server to client)

def create_offer_message(udp_port, tcp_port):
    """
    Create an offer message to be sent to clients.
    
    Args:
        udp_port (int): The UDP port number that the client should connect to for UDP requests.
        tcp_port (int): The TCP port number that the client should connect to for TCP requests.
    
    Returns:
        bytes: The packed offer message as a byte string.
    """
    # Pack the values into a byte string using network byte order (big-endian)
    return struct.pack('!IBHH', MAGIC_COOKIE, OFFER_MESSAGE_TYPE, udp_port, tcp_port)