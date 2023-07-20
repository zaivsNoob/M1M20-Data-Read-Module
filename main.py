from pymodbus.client import ModbusTcpClient
from utility import read_modbus_data
# IP address of the Modbus device
ip_address = '192.168.68.245'

# Register address to read data from
register_address = 23298




if __name__ == "__main__":
    # Call the function to read data from the Modbus device
    read_modbus_data(ip_address, register_address)
