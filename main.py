import streamlit as st
import sqlite3
import os


def main():
    st.title("Experimental Procedures and Guidelines")

    # Set up the UI header
    st.subheader("Context Introduction")

    # Provide experiment details
    st.markdown("Welcome, and thank you for participating in this study!")
    st.markdown(
        "You will be randomly assigned to one of two roles: **Creative Worker** or **Support Worker**. "
        "As a member of a consulting company, you will collaborate with a **Robot** colleague online to make quick business decisions together. "
        "At the end of the study, a bonus will be awarded, and one of the collaborators in the group will be responsible for distributing it. "
        "Therefore, we encourage you to put in your best effort during this interactive session."
    )
    st.markdown(
        "After the experiment, we will ask you to complete a questionnaire. The estimated time for this is approximately ... minutes."
    )
    st.markdown("If you have any questions during the study, please raise your hand to notify the experimenter.")

    # Add a text input for experiment code
    custom_response = st.text_input("Please enter your experiment code:")

    # Handle experiment code submission
    if st.button("Submit Response"):
        if custom_response:  # Ensure input is not empty
            if custom_response == "01":
                st.success(
                    "Your role is **Creative Worker**. "
                    "This role is primarily responsible for generating and managing key ideas. "
                    "During conversations, you are expected to use **a more commanding tone** when interacting with other collaborators. "
                    "In the final stage, **you have the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**Your collaborator does not** have such control over you."
                )
            elif custom_response == "02":
                st.success(
                    "Your role is **Creative Worker**. "
                    "This role is primarily responsible for generating and managing key ideas. "
                    "During conversations, you are expected to use **a more commanding tone** when interacting with other collaborators. "
                    "In the final stage, **your collaborator has the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**You do not** have such control over them."
                )
            elif custom_response == "03":
                st.success(
                    "Your role is **Support Worker**. "
                    "This role is mainly responsible for small tasks and record-keeping. "
                    "During conversations, you are expected to use **a more polite tone** when interacting with other collaborators. "
                    "In the final stage, **you have the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**Your collaborator does not** have such control over you."
                )
            elif custom_response == "04":
                st.success(
                    "Your role is **Support Worker**. "
                    "This role is mainly responsible for small tasks and record-keeping. "
                    "During conversations, you are expected to use **a more polite tone** when interacting with other collaborators. "
                    "In the final stage, **your collaborator has the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**You do not** have such control over them."
                )
            else:
                st.error("Invalid input. Please enter a valid case (01, 02, 03, 04).")
        else:
            st.warning("Please enter your experiment code before submitting.")
    else:
        st.info("Submit your response after filling in the fields.")
    
    st.subheader("Task Instructions")
    # Add a slider to adjust a numeric value
    numeric_value = st.slider(
        "Set a numeric value:",
        min_value=0, max_value=100, value=50
    )
    
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
    main()