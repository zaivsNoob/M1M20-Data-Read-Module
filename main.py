from utility import ModbusReader
import threading
# IP address of the Modbus device
ip_address = '192.168.68.245'

# Register address to read data from 
register_address_1 = 23298
register_address_2 = 23299



if __name__ == "__main__":
    # Create an instance of the ModbusReader class
    modbus_reader = ModbusReader(ip_address)



    try:
        # Call the method to read data from the Modbus device
        data = modbus_reader.real_time_data(register_address_2)
        modbus_reader.close()
        # data = modbus_reader.real_time_data(register_address2)
    except KeyboardInterrupt:
        pass  # Allow Ctrl+C to stop the script gracefully


# ip_address = '192.168.68.245'

# # Register addresses to read data from
# register_address = 23298
# register_address2 = 23299

# if __name__ == "__main__":
#     modbus_reader = ModbusReader(ip_address)

#     try:
#         # Create two threads for running the real_time_data method concurrently
#         thread1 = threading.Thread(target=modbus_reader.real_time_data, args=(register_address, 1))
#         thread2 = threading.Thread(target=modbus_reader.real_time_data, args=(register_address2, 2))

#         # Start both threads
#         thread1.start()
#         thread2.start()

#         # Wait for both threads to finish
#         thread1.join()
#         thread2.join()

#     except KeyboardInterrupt:
#         print("Loop interrupted. Exiting...")





  