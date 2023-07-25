import logging
from pymodbus.client import ModbusTcpClient
import time
import datetime

from utility import insertToDatabase,convert_to_voltage

class ModbusReader:
    def __init__(self, ip):
        self.ip = ip
        self.client = ModbusTcpClient(ip)
        self.setup_logging()

    def setup_logging(self):
        # Configure logging
        log_file = "modbus_reader.log"
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.logger = logging.getLogger(__name__)

    def close(self):
        if self.client:
            self.client.close()


    def read_modbus_data(self, register_address):
        try:
            result = self.client.read_holding_registers(register_address, count=2, unit=0x01)

            # Check if the read was successful
            if result.isError():
                self.logger.error(f"Modbus Read Error: {result}")
            else:
                # Extract and return the data value
                register_values = result.registers
                voltage =convert_to_voltage(register_values)
                timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:23]
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:23])
                insertToDatabase(timestamp,voltage,self.ip)
                self.logger.info(f"{timestamp}    {register_address}          {voltage} { self.ip} ")

        except Exception as e:
            self.logger.exception(f"Error occurred: {e}")





    def real_time_data(self, register_address):
        self.logger.info("Running indefinitely... (Press Ctrl+C to stop)")
        self.logger.info("Date                 register      value")

        try:
            while True:


                self.read_modbus_data(register_address)
                # time.sleep(5)


        except KeyboardInterrupt:
            # This block is executed when a KeyboardInterrupt (Ctrl+C) is raised
            self.logger.info("Loop interrupted. Exiting...")







