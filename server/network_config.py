import socket
import struct
import fcntl
from config import broadcast_port

class NetworkConfig:
    def __init__(self):
        self.ip_address = None
        self.subnet_mask = None
        self.broadcast_address = None
        self.initialized = False

        try:
            self.ip_address = self.__get_ip_address()
            if self.ip_address is None:
                raise ValueError("Failed to get IP address")
            print(f"IP Address: {self.ip_address}")

            self.subnet_mask = self.__get_netmask(self.ip_address)
            if self.subnet_mask is None:
                raise ValueError("Failed to get subnet mask")
            print(f"Subnet Mask: {self.subnet_mask}")

            self.broadcast_address = self.__get_broadcast_address(self.ip_address, self.subnet_mask)
            if self.broadcast_address is None:
                raise ValueError("Failed to get broadcast address")
            self.broadcast_address = (self.broadcast_address, broadcast_port)
            print(f"Broadcast Address: {self.broadcast_address}")

            self.initialized = True
        except Exception as e:
            print(f"Error initializing NetworkConfig: {e}")
            print(f"IP Address: {self.ip_address}")
            print(f"Subnet Mask: {self.subnet_mask}")
            print(f"Broadcast Address: {self.broadcast_address}")

    def __get_ip_address(self):
        """
        Get the IP address of the current machine.
        
        Returns:
            str: The IP address of the current machine.
        """
        try:
            return socket.gethostbyname(socket.gethostname())
        except socket.error as e:
            print(f"Error getting IP address: {e}")
            return None

    def __get_netmask(self, ip):
        """
        Get the subnet mask for the given IP address.
        
        Args:
            ip (str): The IP address of the current machine.
        
        Returns:
            str: The subnet mask as a dotted-decimal string.
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x891b,  # SIOCGIFNETMASK: Request code to get the subnet mask
                struct.pack('256s', ip.encode('utf-8'))
            )[20:24])
        except (socket.error, struct.error) as e:
            print(f"Error getting subnet mask: {e}")
            return None

    def __get_broadcast_address(self, ip, netmask):
        """
        Calculate the broadcast address for the current machine's network.
        
        Args:
            ip (str): The IP address of the current machine.
            netmask (str): The subnet mask of the current machine.
        
        Returns:
            str: The broadcast address as a dotted-decimal string.
        """
        try:
            ip_bin = struct.unpack('!I', socket.inet_aton(ip))[0]  # Convert IP address to binary format
            netmask_bin = struct.unpack('!I', socket.inet_aton(netmask))[0]  # Convert subnet mask to binary format
            broadcast_bin = ip_bin | ~netmask_bin  # Calculate the broadcast address in binary format
            broadcast_ip = socket.inet_ntoa(struct.pack('!I', broadcast_bin & 0xFFFFFFFF))  # Convert binary broadcast address to dotted-decimal format
            return broadcast_ip
        except (socket.error, struct.error, IndexError) as e:
            print(f"Error getting broadcast address: {e}")
            return None

# Create an instance of NetworkConfig to calculate and store the values
network_config = NetworkConfig()
ip_address = network_config.ip_address
subnet_mask = network_config.subnet_mask
broadcast_address = network_config.broadcast_address