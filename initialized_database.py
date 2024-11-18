import sqlite3
import os

def initialize_database():
    # Define the paths
    db_path = os.path.join("Database", "responses.db")
    sql_file_path = os.path.join("Database", "main.sql")

    # Check if the SQL file exists
    if not os.path.exists(sql_file_path):
        raise FileNotFoundError(f"SQL file not found: {sql_file_path}")

    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Read the SQL file
    with open(sql_file_path, 'r') as file:
        sql_script = file.read()

    # Execute the SQL script
    cursor.executescript(sql_script)

    # Commit and close the connection
    connection.commit()
    connection.close()

    print(f"Database initialized successfully at {db_path}")

if __name__ == "__main__":
    initialize_database()