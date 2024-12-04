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
    return pyodbc.connect(connection_string)

conn = get_connection()
cursor = conn.cursor()
print("Connected to the database!")

try:
    print("Tables created successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    cursor.close()
    conn.close()