from enums.data_metric_enum import DataMetricEnum



class StartupHandler:
    
    def __init__(self):
        self.amount_of_data = 0
        self.data_metric = DataMetricEnum.DEFAULT
        self.number_of_TCP_connections = 0
        self.number_of_UDP_connections = 0
        
        
    def get_amount_of_data(self):   
        self.amount_of_data = self._get_valid_input("Enter the file size you wish to receive: ", is_data_metric=True)
        self.number_of_TCP_connections = self._get_valid_input("Enter the number of TCP connections: ")
        self.number_of_UDP_connections = self._get_valid_input("Enter the number of UDP connections: ")

    def _get_valid_input(self, prompt, is_data_metric=False):
        while True:
            input_data = input(prompt)
            if is_data_metric:
                try:
                    self.data_metric = DataMetricEnum(input_data[-2:]) # Get the last two characters of the input
                    return int(input_data[:-2]) # Get the number of the input
                except ValueError or IndexError:
                    print("Please enter a valid file size")
                    continue
            try:
                return int(input_data)
            except ValueError:
                print("Please enter a valid number")

