from enums.data_metric_enum import DataMetricEnum



class StartupHandler:
    
    def __init__(self):
        self.amount_of_data = 0
        self.data_metric = DataMetricEnum.DEFAULT
        self.number_of_TCP_connections = 0
        self.number_of_UDP_connections = 0
        self.amount_of_data_in_bytes = 0
        self.conversion_map = { # mybe need to find a better plcae for this
            "KB" : 1000,
            "MB" : 1000_000,
            "GB" : 1000_000_000,
            "TB" : 1000_000_000_000,
            "Kb" : 1000 / 8,
            "Mb" : 1000 ** 2 / 8,
            "Gb" : 1000 ** 3 / 8,
            "Tb" : 1000 ** 4 / 8,
            "B" :  1,
            "b" :  1/8,
        }
        
        
    def get_amount_of_data(self):   
        self.amount_of_data = self._get_valid_input("Enter the file size you wish to receive: ", is_data_metric=True)
        self.number_of_TCP_connections = self._get_valid_input("Enter the number of TCP connections: ")
        self.number_of_UDP_connections = self._get_valid_input("Enter the number of UDP connections: ")
        self.amount_of_data_in_bytes = self._convert_data_to_bytes()

    def _get_valid_input(self, prompt, is_data_metric=False):
        while True:
            input_data = input(prompt)
            if is_data_metric:
                try:
                    data_metric_index = self._find_data_metric_index(input_data)
                    self.data_metric = DataMetricEnum(input_data[data_metric_index:])
                    return int(input_data[:data_metric_index])
                except ValueError or IndexError:
                    print("Please enter a valid file size")
                    continue
            try:
                return int(input_data)
            except ValueError:
                print("Please enter a valid number")
    
    def _find_data_metric_index(self, data:str):
        for i in range(len(data)):
            if data[i].isalpha():
                return i
    
    def _convert_data_to_bytes(self):
        data_metric_list = DataMetricEnum.__members__.values()
        for metric in data_metric_list:
            if metric == self.data_metric:
                return self.amount_of_data * self.conversion_map[metric.name]
