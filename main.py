from utility import ModbusReader

# IP address of the Modbus device
ip_address = '192.168.68.245'

# Register address to read data from
register_address = 23298

if __name__ == "__main__":
    # Create an instance of the ModbusReader class
    modbus_reader = ModbusReader(ip_address)

    try:
        # Call the method to read data from the Modbus device
        data = modbus_reader.real_time_data(register_address)
    except KeyboardInterrupt:
        pass  # Allow Ctrl+C to stop the script gracefully

