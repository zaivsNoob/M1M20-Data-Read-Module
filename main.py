# from ModbusReader import ModbusReader
# import threading
# # IP address of the Modbus device
# ip_address_1 = '192.168.68.145'
# ip_address_2 = '192.168.68.146'
# ip_address_3 = '192.168.68.147'

# # Register address to read data from 
# register_address_1 = 23298
# register_address_2 = 23299



# if __name__ == "__main__":
#     # Create an instance of the ModbusReader class
#     modbus_reader_1 = ModbusReader(ip_address_1)
#     modbus_reader_2 = ModbusReader(ip_address_2)
#     modbus_reader_3 = ModbusReader(ip_address_3)



#     try:
#         # Call the method to read data from the Modbus device
#         data = modbus_reader_1.real_time_data(register_address_1)
#         data = modbus_reader_2.real_time_data(register_address_1)
#         data = modbus_reader_3.real_time_data(register_address_1)
#         modbus_reader_1.close()
#         modbus_reader_2.close()
#         modbus_reader_3.close()
#         # data = modbus_reader.real_time_data(register_address2)
#     except KeyboardInterrupt:
#         pass  # Allow Ctrl+C to stop the script gracefully






# from ModbusReader import ModbusReader
# import threading

# # IP address of the Modbus devices
# ip_address_1 = '192.168.68.145'
# ip_address_2 = '192.168.68.146'
# ip_address_3 = '192.168.68.147'

# stop_event_1 = threading.Event()
# stop_event_2 = threading.Event()
# stop_event_3 = threading.Event()

# # Register address to read data from
# register_address_1 = 23298
# register_address_2 = 23299

# # Define a function to read data from the Modbus device in a thread
# def read_data_in_thread(modbus_reader, register_address):
#     data = modbus_reader.real_time_data(register_address)
#     modbus_reader.close()

# if __name__ == "__main__":
#     # Create instances of the ModbusReader class
#     modbus_reader_1 = ModbusReader(ip_address_1)
#     modbus_reader_2 = ModbusReader(ip_address_2)
#     modbus_reader_3 = ModbusReader(ip_address_3)


#         # Create threads for each ModbusReader instance
#     thread1 = threading.Thread(target=read_data_in_thread, args=(modbus_reader_1, register_address_1))
#     thread2 = threading.Thread(target=read_data_in_thread, args=(modbus_reader_2, register_address_1))
#     thread3 = threading.Thread(target=read_data_in_thread, args=(modbus_reader_3, register_address_1))

#         # Start the threads
#     thread1.start()
#     thread2.start()
#     thread3.start()

#     try:
#         # Keep the main process alive while the child processes are running
#         while True:
#             if (
#                 not thread1.is_alive()
#                 and not thread2.is_alive()
#                 and not thread3.is_alive()
#             ):
#                 break
#     except KeyboardInterrupt:
#         # Terminate the processes if a keyboard interrupt occurs
#         stop_event_1.set()
#         stop_event_2.set()
#         stop_event_3.set()
#         thread1.join()
#         thread2.join()
#         thread3.join()


  

## WORKING

from ModbusReader import ModbusReader
import multiprocessing

# IP address of the Modbus devices
ip_address_1 = '192.168.68.145'
ip_address_2 = '192.168.68.146'
ip_address_3 = '192.168.68.147'

# Register address to read data from
register_address_1 = 23298
register_address_2 = 23299

# Define a function to read data from the Modbus device in a process
def read_data_in_process(ip_address, register_address, stop_event):
    modbus_reader = ModbusReader(ip_address)
    try:
        while not stop_event.is_set():
            data = modbus_reader.real_time_data(register_address)
    except Exception as e:
        print(f"Error reading data from {ip_address}: {e}")
    finally:
        modbus_reader.close()

if __name__ == "__main__":
    # Create stop events for each process
    stop_event_1 = multiprocessing.Event()
    stop_event_2 = multiprocessing.Event()
    stop_event_3 = multiprocessing.Event()

    # Create processes for each ModbusReader instance
    process1 = multiprocessing.Process(target=read_data_in_process, args=(ip_address_1, register_address_1, stop_event_1))
    process2 = multiprocessing.Process(target=read_data_in_process, args=(ip_address_2, register_address_1, stop_event_2))
    process3 = multiprocessing.Process(target=read_data_in_process, args=(ip_address_3, register_address_1, stop_event_3))

    # Start the processes
    process1.start()
    process2.start()
    process3.start()

    try:
        # Keep the main process alive while the child processes are running
        while True:
            if (
                not process1.is_alive()
                and not process2.is_alive()
                and not process3.is_alive()
            ):
                break
    except KeyboardInterrupt:
        # Terminate the processes if a keyboard interrupt occurs
        stop_event_1.set()
        stop_event_2.set()
        stop_event_3.set()
        process1.join()
        process2.join()
        process3.join()




# import threading
# from ModbusReader import ModbusReader

# # IP address of the Modbus devices
# ip_address_1 = '192.168.68.145'
# ip_address_2 = '192.168.68.146'
# ip_address_3 = '192.168.68.147'

# # Register address to read data from
# register_address_1 = 23298
# register_address_2 = 23299

# # Define stop events to gracefully stop the threads


# # Define a function to read data from the Modbus device in a thread
# def read_data_in_thread(modbus_reader, register_address, stop_event):
#     while not stop_event.is_set():
#         data = modbus_reader.real_time_data(register_address)
#         if stop_event.is_set():
#             break
#     modbus_reader.close()

# if __name__ == "__main__":

#     stop_event_1 = threading.Event()
#     stop_event_2 = threading.Event()
#     stop_event_3 = threading.Event()
#     # Create instances of the ModbusReader class
#     modbus_reader_1 = ModbusReader(ip_address_1)
#     modbus_reader_2 = ModbusReader(ip_address_2)
#     modbus_reader_3 = ModbusReader(ip_address_3)

#     # Create threads for each ModbusReader instance
#     thread1 = threading.Thread(target=read_data_in_thread, args=(modbus_reader_1, register_address_1, stop_event_1))
#     thread2 = threading.Thread(target=read_data_in_thread, args=(modbus_reader_2, register_address_1, stop_event_2))
#     thread3 = threading.Thread(target=read_data_in_thread, args=(modbus_reader_3, register_address_1, stop_event_3))

#     # Start the threads
#     thread1.start()
#     thread2.start()
#     thread3.start()

#     try:
#         # Keep the main process alive while the child threads are running
#         while True:
#             if (
#                 not thread1.is_alive()
#                 and not thread2.is_alive()
#                 and not thread3.is_alive()
#             ):
#                 break
#     except KeyboardInterrupt:
#         # Set the stop events to stop the threads gracefully
#         stop_event_1.set()
#         stop_event_2.set()
#         stop_event_3.set()

#     # Wait for the threads to complete their tasks
#     thread1.join()
#     thread2.join()
#     thread3.join()
