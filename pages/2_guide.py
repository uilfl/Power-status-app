import streamlit as st
st.set_page_config(page_title="Guidance", page_icon="🌍")

def survey_guidance():
    guidance = st.markdown("""
    Welcome to the Survey!

    We appreciate your participation in this survey. Here are a few things to keep in mind before you begin:

    1. **Confidentiality**: Your responses will be kept confidential and will only be used for research purposes.
    2. **Voluntary Participation**: Your participation is completely voluntary. You may choose to skip any question or withdraw from the survey at any time.
    3. **Time Commitment**: The survey should take approximately 10-15 minutes to complete.
    4. **Honesty**: Please answer the questions as honestly as possible. There are no right or wrong answers.
    5. **Contact Information**: If you have any questions or concerns about the survey, please contact us at [your contact information].

    Thank you for your time and participation!

    Sincerely,
    [Your Organization]
     """)


survey_guidance()