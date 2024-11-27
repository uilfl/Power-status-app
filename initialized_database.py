import streamlit as st
from sqlalchemy import text
import os

# Ensure the database directory and file exist
db_path = os.path.join("Database", "main.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Create the SQL connection to main.db as defined in secrets.toml
conn = st.experimental_connection('main_db', type='sql')

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