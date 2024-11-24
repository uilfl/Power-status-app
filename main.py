import streamlit as st
import sqlite3
import os


def main():
    st.title("Experiment Procedure and Instructions")
    
    # Set up the UI header
    st.subheader("Introduction to the Scenario:")

    # Add a dropdown (select box) for choosing options
    option = st.caption("Dear Participant, You will be interacting online with a robot coworker from the same consulting company to make quick business decisions. Please note that you will not meet the robot in person. You will be randomly assigned to one of two roles: **Creative Worker** or **Support Worker**. Together, you will discuss and make decisions on several tasks to determine which strategies should be prioritized for the company you are assisting. After the interaction phase, we will ask you to complete a questionnaire to share your thoughts and feedback. At the end of the study, a team bonus will be provided. Therefore, we encourage you to put in your best effort during this research discussion.")

    option = st.caption("The procedure for this experiment is as follows:\n"" 1. Online Decision-Making Interaction \n""2. Post-Interaction Questionnaire\n\n\n")
    # Add a slider to adjust a numeric value
    numeric_value = st.slider(
        "Set a numeric value:",
        min_value=0, max_value=100, value=50
    )

    # Add a text input for custom responses
    custom_response = st.text_input("Enter your custom response:")

    # Add a submit button
    if st.button("Submit Response"):
        st.success("Response Submitted!")
        st.write("### Your Response Summary:")
        st.write(f"- Selected Option: {option}")
        st.write(f"- Numeric Value: {numeric_value}")
        st.write(f"- Custom Response: {custom_response}")
    else:
        st.info("Submit your response after filling in the fields.")

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