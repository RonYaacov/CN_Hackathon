# Configuration parameters
import sys


broadcast_port = 1234  # Agreed-upon port for broadcasting
broadcast_interval = 1  # Interval in seconds
broadcast_address = ('<broadcast>', broadcast_port)  # Broadcast address to use for broadcasting

udp_port = 13117  # Example UDP port
tcp_port = 13118  # Example TCP port

# Constants for the offer message
MAGIC_COOKIE = "0xabcddcba"  # Unique identifier to validate the message
OFFER_MESSAGE_TYPE = "0x2"  # Message type for offer (server to client)
REQUEST_MESSAGE_TYPE = "0x3"  # Message type for request (client to server)
PAYLOAD_MESSAGE_TYPE = "0x4"  # Message type for the Payload (server to slient)

max_receive_buffer_size = 1024
size_of_udp_packet_payload = 1024