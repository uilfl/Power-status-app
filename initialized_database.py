import streamlit as st

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.experimental_connection('main_db', type='sql')
# Insert some data with conn.session.
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS User (ID INT PRIMARY KEY, Age INT);')
    s.execute('CREATE TABLE IF NOT EXISTS User_Response (fk INT, Time_response CHAR(50), Response INT, Change BOOLEAN, Changed_answer INT, Change_interval_time CHAR(50), group_num INT, Field1 VARCHAR(255), Field2 VARCHAR(255), FOREIGN KEY (fk) REFERENCES User(ID));')
    s.execute('CREATE TABLE IF NOT EXISTS Robot (Response VARCHAR(255));')
    
    s.execute('DELETE FROM User;')
    s.execute('DELETE FROM User_Response;')
    s.execute('DELETE FROM Robot;')
    
    users = [(1, 25), (2, 30), (3, 22)]
    user_responses = [
        (1, '2023-01-01 10:00:00', 1, False, None, None, 1, 'Field1_data', 'Field2_data'),
        (2, '2023-01-01 10:05:00', 2, True, 3, '5 minutes', 1, 'Field1_data', 'Field2_data'),
        (3, '2023-01-01 10:10:00', 3, False, None, None, 2, 'Field1_data', 'Field2_data')
    ]
    robots = [('Response data',)]
    
    for user in users:
        s.execute('INSERT INTO User (ID, Age) VALUES (?, ?);', user)
    
    for response in user_responses:
        s.execute('INSERT INTO User_Response (fk, Time_response, Response, Change, Changed_answer, Change_interval_time, group_num, Field1, Field2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);', response)
    
    for robot in robots:
        s.execute('INSERT INTO Robot (Response) VALUES (?);', robot)
    
    s.commit()

# Query and display the data you inserted
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)