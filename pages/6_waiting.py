import streamlit as st 
import time 


st.title("Processing")
    
    # Display a spinner and progress bar
with st.spinner("Please wait..."):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.01)
    
st.success("Task completed successfully!")
    
if st.button("Start New Task"):
        st.session_state.current_page = 'start'
        st.experimental_rerun()