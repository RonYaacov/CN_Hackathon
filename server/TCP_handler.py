import socket
from typing import Tuple
from config import tcp_port, max_receive_buffer_size
from threading import Thread

class TCPHandler:
    
    def __init__(self):
        self.connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.workers = []
    
    def listen(self):
        self.connection_socket.bind(("",tcp_port))
        while True:
            self.connection_socket.listen()
            conn, addr = self.connection_socket.accept()
            self.create_worker(conn, addr)
        
    def create_worker(self, conn: socket.socket, addr: Tuple[str, int]):
        worker = Thread(target=self.handle, args=(conn, addr))
        self.workers.append(worker)
        worker.start()
        
    def handle(self, conn: socket.socket, addr: Tuple[str, int]):
        try:
            data = conn.recv(max_receive_buffer_size)
            file_size = int(float(data.decode()))
            response_data = b'a' * file_size
            conn.sendall(response_data)
                      
        except Exception as e:
            print(f"Error in handling connection: {e}")        
        
        
        
    