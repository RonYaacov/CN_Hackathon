import socket
import struct
from threading import Thread
from config import udp_port, max_receive_buffer_size, MAGIC_COOKIE, REQUEST_MESSAGE_TYPE, size_of_udp_packet_payload
from formats import create_payload_message

class UDPHandler:
    
    def __init__(self):
        self.connection_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.workers = []
        
    def listen(self):
        self.connection_socket.bind(("",udp_port))
        while True:
            data, addr = self.connection_socket.recvfrom(max_receive_buffer_size)
            
            client_magic_cookie, client_message_type, file_size = struct.unpack('!IBQ', data)
            client_magic_cookie = hex(client_magic_cookie)
            client_message_type = hex(client_message_type)
            if client_magic_cookie != MAGIC_COOKIE or client_message_type != REQUEST_MESSAGE_TYPE:
                continue
            
            self.create_worker(file_size, addr)

    def create_worker(self, file_size, addr):
        worker = Thread(target=self.handle, args=(file_size, addr))
        self.workers.append(worker)
        worker.start()
        
    def handle(self, file_size, addr):
        try:
            response_data = b'a' * file_size
            chunks = [response_data[i:i + size_of_udp_packet_payload] for i in range(0, file_size, size_of_udp_packet_payload)]
            for index, cunk in enumerate(chunks):
                msg = create_payload_message(len(chunks), index+1, cunk)
                self.connection_socket.sendto(msg, addr)
                      
        except Exception as e:
            print(f"Error in handling connection: {e}")
        