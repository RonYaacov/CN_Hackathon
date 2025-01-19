from handler_factory import HandlerFactory
from speed_tester import SpeedTester
from startup_handler import StartupHandler
from offer_seeker import OfferSeeker
from config import HEADER, OKGREEN, ENDC


def main():
    while True:
        start_up_handler =  StartupHandler()
        start_up_handler.get_amount_of_data()
        print(f"{HEADER}Client started, listening for offer requests...{ENDC}")
        offer_seeker = OfferSeeker()
        offer_seeker.seek_for_offer()
        handler_factory = HandlerFactory(server_address=offer_seeker.servers_address,
                                         server_tcp_port=offer_seeker.server_port_tcp,
                                         server_udp_port=offer_seeker.server_port_udp)
        speed_tester = SpeedTester(start_up_handler.number_of_TCP_connections,
                            start_up_handler.number_of_UDP_connections,
                            start_up_handler.amount_of_data_in_bytes,
                            handler_factory)
        speed_tester.run_speed_tests()
        print(f"{OKGREEN}All transfers complete, listening to offer requests{ENDC}")

if __name__ == "__main__":
    main()