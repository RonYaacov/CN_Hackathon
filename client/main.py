from startup_handler import StartupHandler


def main():
    while True:
        print("Client started, listening for offer requests...")
        start_up_handler =  StartupHandler()
        start_up_handler.get_amount_of_data()
        # Remove the following print statements later
        print("Received the following data:")
        print(f"File size: {start_up_handler.amount_of_data}{start_up_handler.data_metric.name}")
        print(f"Number of TCP connections: {start_up_handler.number_of_TCP_connections}")
        print(f"Number of UDP connections: {start_up_handler.number_of_UDP_connections}")
        
        
if __name__ == "__main__":
    main()