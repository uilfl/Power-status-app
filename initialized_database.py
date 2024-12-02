import streamlit as st
from sqlalchemy import text
import pyodbc

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
)

# Connect to the database
conn = pyodbc.connect(connection_string)
print("Connection successful")


# Database operations
with conn.session as s:
    # Create tables
    s.execute(text('''
        CREATE TABLE IF NOT EXISTS User (
            ID INT PRIMARY KEY,
            Age INT
        );
    '''))
    s.execute(text('''
        CREATE TABLE IF NOT EXISTS User_Response (
            fk INT,
            Time_response CHAR(50),
            Response INT,
            Change BOOLEAN,
            Changed_answer INT,
            Change_interval_time CHAR(50),
            group_num INT,
            Field1 VARCHAR(255),
            Field2 VARCHAR(255),
            FOREIGN KEY (fk) REFERENCES User(ID)
        );
    '''))
    s.execute(text('''
        CREATE TABLE IF NOT EXISTS Robot (
            Response VARCHAR(255)
        );
    '''))

    # Insert data
    users = [(1, 25), (2, 30), (3, 22)]
    for user in users:
        s.execute(text('INSERT INTO User (ID, Age) VALUES (:id, :age);'), {'id': user[0], 'age': user[1]})

    s.commit()

# Query and display the data
users_data = conn.query("SELECT * FROM User;")
st.dataframe(users_data)