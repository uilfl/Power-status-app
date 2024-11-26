
import streamlit as st
st.set_page_config(page_title="Questionaire", page_icon=":memo:")

st.title("Questionnaire")
st.markdown("""
Next, we kindly ask you to complete a short survey to help us better understand your interaction experience and feelings.
""")


questionnaire_url = "https://docs.google.com/forms/d/e/1FAIpQLSehHPA4ny-bSevnnfEnqCeRHSSQSumRJyyephxXlBiSjsJzxQ/viewform"
st.components.v1.iframe(questionnaire_url, width=800, height=600, scrolling=True)
st.info("Submit your response after filling in the fields.")
