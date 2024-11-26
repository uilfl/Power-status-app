import streamlit as st 
def main():
    st.title("Experimental Procedures and Guidelines")
    
    # Set up the UI header
    st.subheader("Context Introduction")

    # Add a dropdown (select box) for choosing options
    st.caption("Welcome, and thank you for participating in this study!")
    st.caption("You will be randomly assigned to one of two roles: **Creative Worker** or **Support Worker**. As a member of a consulting company, you will collaborate with a **Robot** colleague online to make quick business decisions together. At the end of the study, a bonus will be awarded, and one of the collaborators in the group will be responsible for distributing it. Therefore, we encourage you to put in your best effort during this interactive session.")
    st.caption("After the experiment, we will ask you to complete a questionnaire. The estimated time for this is approximately ... minutes.")
    st.caption("If you have any questions during the study, please raise your hand to notify the experimenter.")

    # Add a text input for custom responses
    custom_response = st.text_input("Please enter your experiment code:")

    # Add a submit button
    if st.button("Submit Response"):
        if custom_response:  # 確保輸入值不為空
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
                    "You do not have such control over them."
                )
            else:
                st.error("Invalid input. Please enter a valid case (01, 02, 03, 04).")
        else:
            st.warning("Please enter your experiment code before submitting.")
    else:
        st.info("Submit your response after filling in the fields.")

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



if __name__ == "__main__":
    print("Connected to the SQLite database from 'Database/main.sql'")
    main()