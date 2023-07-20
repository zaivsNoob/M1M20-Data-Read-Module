from pymodbus.client import ModbusTcpClient
import time
import datetime
class ModbusReader:
    def __init__(self, ip):
        self.ip = ip
        self.client = ModbusTcpClient(ip)

    def __del__(self):
        if self.client:
            self.client.close()




    def convert_to_voltage(self, reg_values):
        #data is stored as an unsigned 32-bit integer

        combined_value = (reg_values[0] << 16) + reg_values[1]
        voltage = combined_value * 0.1  # Adjust the scaling factor as needed based on your device configuration
        return voltage
    




    def read_modbus_data(self, register_address):
        try:
            # Read data from the specified register address (two consecutive holding registers)
            result = self.client.read_holding_registers(register_address, count=2, unit=0x01)

            # Check if the read was successful
            if result.isError():
                print(f"Modbus Read Error: {result}")
            else:
                # Extract and return the data value
                register_values = result.registers
                voltage = self.convert_to_voltage(register_values)
                print(f"Data read from date {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} register {register_address}: {voltage} ")
                return voltage

        except Exception as e:
            print(f"Error occurred: {e}")


    def real_time_data(self,register_address):
        print("Running indefinitely... (Press Ctrl+C to stop)")
        try:
            while True:

                self.read_modbus_data(register_address)
                time.sleep(5)


                

        except KeyboardInterrupt:
        # This block is executed when a KeyboardInterrupt (Ctrl+C) is raised
            print("Loop interrupted. Exiting...")



