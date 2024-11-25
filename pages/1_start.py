import streamlit as st 



st.title("Task Comparison System")
    
query_params = st.experimental_get_query_params()
current_page = query_params.get("page", ["start"])[0] 
    # Header with XXX placeholder
st.write("XXXX")
number = st.number_input("Please enter your number:", min_value=0)
st.write("Disclaimer: This is a demo application for task comparison purposes.")
    
if st.button("Start"):
    st.session_state.current_page = 'task'
    st.experimental_rerun()