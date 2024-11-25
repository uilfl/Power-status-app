
import streamlit as st
st.set_page_config(page_title="Questionaire", page_icon=":memo:")

st.title("Questionnaire")
st.write("Please fill out the questionnaire below:")

questionnaire_url = "https://docs.google.com/forms/d/e/1FAIpQLSehHPA4ny-bSevnnfEnqCeRHSSQSumRJyyephxXlBiSjsJzxQ/viewform"
st.components.v1.iframe(questionnaire_url, width=800, height=600, scrolling=True)
st.info("Submit your response after filling in the fields.")
