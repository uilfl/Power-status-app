import streamlit as st
from sqlalchemy import text
import sqlite3


# Function for the main experiment interface
def main():
    st.title("Experimental Procedures ＆ Guidelines")
    st.subheader("Context Introduction")

    # Context instructions
    st.markdown(
        """
        Welcome, and thank you for participating in this study!  
        You will be randomly assigned to one of two roles: **Creative Worker** or **Support Worker**.  
        As a member of a consulting company, you will collaborate with a **Robot** colleague online to make quick business decisions together.  
        At the end of the study, a bonus will be awarded, and one of the collaborators in the group will be responsible for distributing it.  
        Therefore, we encourage you to put in your best effort during this interactive session.  
        After the experiment, we will ask you to complete a questionnaire.  
        If you have any questions during the study, please raise your hand to notify the experimenter.
        """
    )

    # Text input for experiment code
    custom_response = st.text_input("Please enter your experiment code:")

    # Handle experiment code submission
    if st.button("Submit Response"):
        if custom_response:  # Ensure input is not empty
            if custom_response == "01":
                st.session_state["role_assigned"] = True
                st.session_state["success_message"] = (
                    "Your role is **Creative Worker**. "
                    "This role is primarily responsible for generating and managing key ideas. "
                    "During conversations, you are expected to use **a more commanding tone** when interacting with other collaborators. "
                    "In the final stage, **you have the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**Your collaborator does not** have such control over you."
                )
            elif custom_response == "02":
                st.session_state["role_assigned"] = True
                st.session_state["success_message"] = (
                    "Your role is **Creative Worker**. "
                    "This role is primarily responsible for generating and managing key ideas. "
                    "During conversations, you are expected to use **a more commanding tone** when interacting with other collaborators. "
                    "In the final stage, **your collaborator has the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**You do not** have such control over them."
                )
            elif custom_response == "03":
                st.session_state["role_assigned"] = True
                st.session_state["success_message"] = (
                    "Your role is **Support Worker**. "
                    "This role is mainly responsible for small tasks and record-keeping. "
                    "During conversations, you are expected to use **a more polite tone** when interacting with other collaborators. "
                    "In the final stage, **you have the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**Your collaborator does not** have such control over you."
                )
            elif custom_response == "04":
                st.session_state["role_assigned"] = True
                st.session_state["success_message"] = (
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

    # Show success message if available
    if st.session_state.get("success_message"):
        st.success(st.session_state["success_message"])

    # Only show the checkbox and next button after a valid code is submitted
    if st.session_state.get("role_assigned"):
        # Add checkbox to confirm reading
        confirmation = st.checkbox(
            "I have read and understand the above.",
            value=st.session_state.get("confirmation", False),
        )

        # Save checkbox state
        st.session_state["confirmation"] = confirmation

        # Add Next Page button to proceed
        if st.button("Next Page"):
            if confirmation:
                st.session_state["current_page"] = "guide"
                st.query_params.update({"page": "guide"})
            else:
                st.warning("Please make sure you have finished reading before clicking on the next page.")

    # Database interaction (SQLAlchemy example)
    # if st.button("Save Numeric Value"):
    #     numeric_value = st.slider(
    #         "Set a numeric value:",
    #         min_value=0, max_value=100, value=50
    #     )
    #     with st.experimental_connection("main_db", type="sql").session as conn:
    #         conn.execute(
    #             text('INSERT INTO User (ID) VALUES (:ID);'),
    #             {'ID': numeric_value}
    #         )
    #         conn.commit()
    #         st.success("Numeric value saved successfully.")

# Function for the task comparison system
def task_comparison_system():
    st.title("Task Comparison System")

    # Placeholder for task comparison
    st.write("This is the task comparison system.")

    # Handle number input
    number = st.number_input("Please enter your number:", min_value=0)
    st.write("Disclaimer: This is a demo application for task comparison purposes.")

    # Start button handling
    if st.button("Start Task Comparison"):
        st.session_state["current_page"] = "task_instruction"
        st.query_params.update({"page": "task_instruction"})


# Main entry point
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "main"

query_params = st.query_params  # Use `st.query_params` to get query parameters

if query_params.get("page") == "guide" or st.session_state["current_page"] == "guide":
    task_comparison_system()
else:
    main()