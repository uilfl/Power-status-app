import streamlit as st
from sqlalchemy import text

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.experimental_connection('main_db', type='sql', url='sqlite:///Database/main.sql')

# Insert some data with conn.session.
with conn.session as s:
    # Wrap SQL statements in `text`
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

    # Clear existing data
    s.execute(text('DELETE FROM User;'))
    s.execute(text('DELETE FROM User_Response;'))
    s.execute(text('DELETE FROM Robot;'))

    # Insert new data
    users = [(1, 25), (2, 30), (3, 22)]
    user_responses = [
        (1, '2023-01-01 10:00:00', 1, False, None, None, 1, 'Field1_data', 'Field2_data'),
        (2, '2023-01-01 10:05:00', 2, True, 3, '5 minutes', 1, 'Field1_data', 'Field2_data'),
        (3, '2023-01-01 10:10:00', 3, False, None, None, 2, 'Field1_data', 'Field2_data')
    ]
    robots = [('Response data',)]

    # Insert into User table
    for user in users:
        s.execute(text('INSERT INTO User (ID, Age) VALUES (:id, :age);'), {'id': user[0], 'age': user[1]})

    # Insert into User_Response table
    for response in user_responses:
        s.execute(text('''
            INSERT INTO User_Response (
                fk, Time_response, Response, Change, Changed_answer, 
                Change_interval_time, group_num, Field1, Field2
            ) VALUES (
                :fk, :time_response, :response, :change, :changed_answer, 
                :change_interval_time, :group_num, :field1, :field2
            );
        '''), {
            'fk': response[0],
            'time_response': response[1],
            'response': response[2],
            'change': response[3],
            'changed_answer': response[4],
            'change_interval_time': response[5],
            'group_num': response[6],
            'field1': response[7],
            'field2': response[8]
        })

    # Insert into Robot table
    for robot in robots:
        s.execute(text('INSERT INTO Robot (Response) VALUES (:response);'), {'response': robot[0]})

    s.commit()

# Query and display the data from the User table
users = conn.query('SELECT * FROM User;')