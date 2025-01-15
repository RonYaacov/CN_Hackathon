import struct
from config import MAGIC_COOKIE, OFFER_MESSAGE_TYPE, PAYLOAD_MESSAGE_TYPE

def create_offer_message(udp_port, tcp_port):
    """
    Create an offer message to be sent to clients.
    
    Args:
        udp_port (int): The UDP port number that the client should connect to for UDP requests.
        tcp_port (int): The TCP port number that the client should connect to for TCP requests.
    
    Returns:
        bytes: The packed offer message as a byte string.
    """
    # Convert MAGIC_COOKIE from hex to int
    # Pack the values into a byte string using network byte order (big-endian)
    return struct.pack('!IBHH', int(MAGIC_COOKIE, 16), int(OFFER_MESSAGE_TYPE, 16), udp_port, tcp_port)


def create_payload_message(total_segments, current_segment, segment_data):
    return struct.pack(f"!IBQQ{len(segment_data)}s", int(MAGIC_COOKIE, 16), int(PAYLOAD_MESSAGE_TYPE, 16), total_segments, current_segment, segment_data)

