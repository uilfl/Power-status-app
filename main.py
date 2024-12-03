import streamlit as st
import sqlite3
import os


# Set the starting page
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "hello"  # Default starting page

# Route to appropriate pages
if st.session_state["current_page"] == "hello":
    from Hello import main as hello_page
    hello_page()
elif st.session_state["current_page"] == "start":
    from test_files.start import main as start_page
    start_page()
elif st.session_state["current_page"] == "task_instruction":
    from pages.task_instruction import task_instruction as task_instruction_page
    task_instruction_page()
    
    # Optional: Add a reset button to clear inputs
    if st.button("Reset"):
        st.experimental_rerun()  # Refreshes the app to reset inputs

        # Add a text input for user questions
        user_question = st.text_input("Ask your question:")
        if user_question:
            # Add user question to chat history
            st.session_state.chat_history.append({"user": user_question})
            
            # Here you can add your answer generation logic
            # For now, we'll just echo the question as an answer
            answer = f"You asked: {user_question}"
            st.session_state.chat_history.append({"assistant": answer})

        # Display chat history
        for chat in st.session_state.chat_history:
            if "user" in chat:
                st.write("You: " + chat["user"])
            if "assistant" in chat:
                st.write("Assistant: " + chat["assistant"])


def connect_to_database():
    # Get the absolute path to the database directory
    db_file_path = os.path.join("Database", "main.sql")
    
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



if __name__ == "__main__":
    connection = connect_to_database()
    print("Connected to the SQLite database from 'Database/main.sql'")
