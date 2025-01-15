from startup_handler import StartupHandler


def main():
    while True:
        start_up_handler =  StartupHandler()
        start_up_handler.get_amount_of_data()
        print("The amount of data is: ", start_up_handler.amount_of_data)
        print("The amount of data in bytes is: ", start_up_handler.amount_of_data_in_bytes)
        print("Client started, listening for offer requests...")
        
        
        
if __name__ == "__main__":
    main()