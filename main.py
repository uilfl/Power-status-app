import streamlit as st

def main():
    st.title("Q&A Interactive Interface")
    
    # Initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Input field for user question
    user_question = st.text_input("Ask your question here:")

    # When user submits a question
    if st.button("Submit"):
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