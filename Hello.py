import streamlit as st
import os
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)



st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

# 初始化 Session State
if "task_completed" not in st.session_state:
    st.session_state["task_completed"] = False

st.title("Welcome to My App!")

# 提供進入第一頁的連結

if "task_completed" not in st.session_state:
    st.session_state["task_completed"] = False

if st.checkbox("Task Completed?"):
    st.session_state["task_completed"] = True
    st.success("Great! Task completed.")

# Navigate to next page when button clicked
if st.session_state["task_completed"]:
    if st.button("Go to Next Page"):
        st.experimental_set_query_params(page="start")  # Add query param
        st.experimental_rerun()


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

