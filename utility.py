from pymodbus.client import ModbusTcpClient


def convert_to_voltage(reg_values):
        # Assuming the data is stored as an unsigned 32-bit integer
        # Combine the two 16-bit registers and convert to voltage using the scaling factor
        combined_value = (reg_values[0] << 16) + reg_values[1]
        voltage = combined_value * 0.1  # Adjust the scaling factor as needed based on your device configuration
        return voltage






def read_modbus_data(ip, register_address):
    try:
        # Connect to the Modbus device

        client = ModbusTcpClient(ip)
        print(client)
        # Read data from the specified register address (single holding register)
        result = client.read_holding_registers(register_address,count=2, unit=0X01)

        # Check if the read was successful
        if result.isError():
            print(f"Modbus Read Error: {result}")
        else:
            # Extract and print the data value
            register_values=result.registers
            voltage =convert_to_voltage(register_values)
            print(f"Data read from register {register_address}: {voltage}")

        # Close the Modbus connection
        client.close()

    except Exception as e:
        print(f"Error occurred: {e}")