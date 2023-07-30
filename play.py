# import pyodbc

# # Replace the following variables with your actual server and login details
# server = '192.168.68.55'
#    # Replace with your SQL Server's IP address or domain name
# database = 'NawabDB'
# username = 'araf'
# password = '1234567890'
# driver = '{ODBC Driver 17 for SQL Server}'  # Make sure the appropriate ODBC driver is installed

# connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'



# try:
#     # Establish the connection
#     conn = pyodbc.connect(connection_string)
#     cursor = conn.cursor()

#     # Execute a simple query to test the connection
#     cursor.execute('SELECT @@VERSION')
#     row = cursor.fetchone()

#     # Output the result
#     if row:
#         print('Connected to SQL Server successfully!')
#         print('Server version:', row[0])
#     else:
#         print('Failed to retrieve data from the server.')

#     # Close the cursor and connection
#     cursor.close()
#     conn.close()

# except pyodbc.Error as e:
#     print('Error connecting to SQL Server:', e)





import pyodbc

# Replace the following variables with your actual server and login details
server = '192.168.68.55'
database = 'Cricketer'
username = 'araf'
password = '1234567890'
driver = '{ODBC Driver 17 for SQL Server}'  # Make sure the appropriate ODBC driver is installed

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Establish the connection
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Execute the INSERT query
    insert_query = '''
    INSERT INTO dbo.test_app_cricketer (player_id, name, country)
    VALUES
        (10, 'Mohammad Amir', 'Pakistan')
 
    '''
    cursor.execute(insert_query)

    # Commit the changes to the database
    conn.commit()

    print('Data inserted successfully!')

    # Close the cursor and connection
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print('Error connecting to SQL Server:', e)

