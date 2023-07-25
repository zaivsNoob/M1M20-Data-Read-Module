import pyodbc

DATABASE_HOST='DESKTOP-E2AADH4'
DATABASE_NAME='M1M20'
DATABASE_USER='sa'
DATABASE_PASSWORD='123456'

def insertToDatabase(timestamp,voltage,ip):
    
        # Save the data to the database
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={DATABASE_HOST};DATABASE={DATABASE_NAME};UID={DATABASE_USER};PWD={DATABASE_PASSWORD}"
        connection = pyodbc.connect(conn_str)
        cursor = connection.cursor()

        insert_query = "INSERT INTO Test_data (Timestamp, Voltage,Ip) VALUES (?, ?,?);"
        cursor.execute(insert_query, timestamp,voltage,ip)

        connection.commit()
        cursor.close()
        connection.close()






def convert_to_voltage(reg_values):
        #data is stored as an unsigned 32-bit integer
        combined_value = (reg_values[0] << 16) + reg_values[1]
        voltage = combined_value * 0.1  # Adjust the scaling factor as needed based on your device configuration
        return voltage


