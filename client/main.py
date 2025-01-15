from speed_tester import SpeedTester
from startup_handler import StartupHandler
from offer_seeker import OfferSeeker


def main():
    while True:
        start_up_handler =  StartupHandler()
        start_up_handler.get_amount_of_data()
        print("The amount of data is: ", start_up_handler.amount_of_data)
        print("The amount of data in bytes is: ", start_up_handler.amount_of_data_in_bytes)
        print("Client started, listening for offer requests...")
        offer_seeker = OfferSeeker()
        offer_seeker.seek_for_offer()
        tcp_handler = None
        udp_handler = None
        speed_tester = SpeedTester(start_up_handler.number_of_TCP_connections,
                                   start_up_handler.number_of_UDP_connections,
                                   start_up_handler.amount_of_data_in_bytes,
                                   tcp_handler, udp_handler)
        speed_tester.run_speed_tests()
        print("All transfers complete, listening to offer requests")

        
        

if __name__ == "__main__":
    main()