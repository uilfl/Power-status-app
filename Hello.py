import streamlit as st
import os
import sqlite3

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# 初始化 Session State
if "task_completed" not in st.session_state:
    st.session_state["task_completed"] = False

st.title("Welcome to My App!")

# 提供進入第一頁的連結
if st.checkbox("Task Completed?"):
    st.session_state["task_completed"] = True
    st.success("Great! Task completed.")

# Navigate to next page when button clicked
if st.session_state["task_completed"]:
    if st.button("Go to Next Page"):
        # Use st.query_params to update the query parameter
        st.query_params.update({"page": "start"})

# 連接資料庫函數
def connect_to_database():
    # Get the absolute path to the database directory
    db_file_path = os.path.join("../Database", "main.db")
    
    # Check if the file exists
    if not os.path.exists(db_file_path):
        raise FileNotFoundError(f"Database file not found: {db_file_path}")

    # Connect to the SQLite database
    conn = sqlite3.connect(":memory:")  # In-memory for executing SQL scripts
    with open(db_file_path, 'r') as sql_file:
        sql_script = sql_file.read()

    # Execute the SQL script to set up the database
    conn.executescript(sql_script)
    print("Database initialized successfully!")
    return conn
