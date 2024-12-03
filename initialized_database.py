import streamlit as st
import pyodbc

def get_connection():
    secrets = st.secrets["azure_sql"]
    connection_string = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={secrets["server"]};'
        f'DATABASE={secrets["database"]};'
        f'UID={secrets["username"]};'
        f'PWD={secrets["password"]};'
        f'Encrypt=yes;'
        f'TrustServerCertificate=no;'
        f'Connection Timeout=30;'
    )   # Connect to the database
    return pyodbc.connect(connection_string), print("Connection successful")

conn = get_connection()
cursor = conn.cursor()

try:
    cursor.execute('''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'User' AND xtype = 'U')
        BEGIN
            CREATE TABLE [User] (
                ID INT PRIMARY KEY,
                Age INT
            );
        END;
    ''')

    cursor.execute('''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'User_Response' AND xtype = 'U')
        BEGIN
            CREATE TABLE User_Response (
                fk INT,
                Time_response CHAR(50),
                Response INT,
                Change BIT,
                Changed_answer INT,
                Change_interval_time CHAR(50),
                group_num INT,
                Field1 VARCHAR(255),
                Field2 VARCHAR(255),
                FOREIGN KEY (fk) REFERENCES [User](ID)
            );
        END;
    ''')

    cursor.execute('''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Robot' AND xtype = 'U')
        BEGIN
            CREATE TABLE Robot (
                Response VARCHAR(255)
            );
        END;
    ''')

    conn.commit()
    print("Tables created successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    cursor.close()
    conn.close()