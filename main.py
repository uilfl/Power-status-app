import streamlit as st

def main():
    st.title("Q&A Interactive Interface")
    
    # Set up the UI header
    st.title("Pull Response Interface")
    st.subheader("Interact with the options below to submit your response.")

    # Add a dropdown (select box) for choosing options
    option = st.selectbox(
        "Choose an option from the list:",
        ["Option 1", "Option 2", "Option 3", "Option 4"]
    )

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

if __name__ == "__main__":
    main()