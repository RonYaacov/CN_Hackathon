from typing import List
from abstractions.base_handler_factory import BaseHandlerFactory
from abstractions.base_request_handler import BaseRequestHandler
from enums.connection_type_enum import ConnectionTypeEnum
from request_msg import RequestMsg
from threading import Thread

class SpeedTester:
    
    def __init__(self, num_of_tcp_connections:int, num_of_udp_connections:int, requested_file_size:int, handler_factory:BaseHandlerFactory):
        self.num_of_tcp_connections = num_of_tcp_connections
        self.num_of_udp_connections = num_of_udp_connections
        self.requested_file_size = requested_file_size
        self.handler_factory = handler_factory
        
    def run_speed_tests(self):
        counter = 1
        thread_list:List[Thread] = []
        for _ in range(self.num_of_tcp_connections):
            thread_list.append(Thread(target=self.tcp_speed_test, args=(counter,)))
            counter += 1
        
        for _ in range(self.num_of_udp_connections):
            thread_list.append(Thread(target=self.udp_speed_test, args=(counter,)))
            counter += 1
            
        for thread in thread_list:
            thread.start()
        
        for thread in thread_list:
            thread.join()
    
    def tcp_speed_test(self, counter:int):
        tcp_handler:BaseRequestHandler = self.handler_factory.get_handler(ConnectionTypeEnum.TCP)
        tcp_handler.connect()
        tcp_handler.send(RequestMsg(self.requested_file_size))
        time_took = tcp_handler.receive()
        print(f"TCP transfer #{counter} finished, total time:"+
              f" {time_took} seconds, total speed: {(self.requested_file_size/time_took)*8} bits/second")
        
        
    
    def udp_speed_test(self, counter:int):
        udp_handler:BaseRequestHandler = self.handler_factory.get_handler(ConnectionTypeEnum.UDP)
        udp_handler.send(RequestMsg(self.requested_file_size))
        time_took = udp_handler.receive()
        percentage = (udp_handler.bytes_received/self.requested_file_size) * 100
        print(f"UDP transfer #{counter} finished, total time: {time_took}"+
              f" seconds, total speed: {(self.requested_file_size/time_took)*8} bits/second, "
              +f"percentage of packets received successfully: {percentage}%")
        
     
        
        