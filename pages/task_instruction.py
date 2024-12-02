import streamlit as st
import random
import time

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="Survey & Experiment", page_icon="📊")

# Initialize session state
if "experiment_step" not in st.session_state:
    st.session_state.experiment_step = "guide"
if "low_status_online" not in st.session_state:
    st.session_state.low_status_online = None
if "high_status_online" not in st.session_state:
    st.session_state.high_status_online = None
if "confirmed" not in st.session_state:
    st.session_state.confirmed = False

def survey_guidance():
    """Initial Survey Guidance Page"""
    st.title("Welcome!")
    st.markdown("""
    We appreciate your participation in this survey. Here are a few things to keep in mind before you begin:

    1. **Confidentiality**: Your responses will be kept confidential and will only be used for research purposes.
    2. **Voluntary Participation**: Your participation is completely voluntary. You may choose to skip any question or withdraw from the survey at any time.
    3. **Time Commitment**: The survey should take approximately 10-15 minutes to complete.
    4. **Honesty**: Please answer the questions as honestly as possible. There are no right or wrong answers.

    Thank you for your time and participation!
                
    **Also, because of technical issues, so please help us by clicking twice on each button.**
    """)
    
    if st.button("Proceed to the Experiment Instructions"):
        st.session_state.experiment_step = 0  # Proceed to the next step

def start():
    """Start Page: Role Assignment and Instructions"""
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
                st.session_state.experiment_step = 1

def step_1():
    """Step 1: Initial Decision"""
    st.title("Task Instructions")
    st.subheader("[Advertising Investment Decision-Making]")
    st.markdown("""
    The company is planning a marketing campaign for a clothing brand and needs your help in developing an advertising strategy. 
    Your goal is to maximize brand exposure and sales conversion rates. With a total budget of 1 million NT dollars, you must allocate funds between **online** and **offline advertising** channels within the budget constraints.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.image("online_advertising.jpg", caption="Online Advertising", use_container_width=True)
        st.markdown("""
        **Online Advertising:**  
        - Social media, search engine ads, email campaigns  
        - Reaches a younger audience  
        - Requires precise targeting strategies
        """)
    with col2:
        st.image("offline_advertising.jpg", caption="Offline Advertising", use_container_width=True)
        st.markdown("""
        **Offline Advertising:**  
        - Billboards, event sponsorships, in-store promotions  
        - Effective for local audiences  
        - Limited reach and higher costs
        """)
    st.caption("""
    Please carefully weigh the advantages and limitations of both options and allocate the budget percentages based on your judgment.
    """)
    
    numeric_value = st.slider(
        "Set a percentage for online advertising (percentage):",
        min_value=0, max_value=100, value=50, key="decision_slider"
    )
    
    if st.button("Confirm", key="confirm_button"):
        st.session_state.low_status_online = max(0, min(100, numeric_value + random.randint(-17, 17)))
        st.session_state.high_status_online = max(0, min(100, numeric_value + random.randint(-17, 17)))
        st.session_state.low_status_offline = 100 - st.session_state.low_status_online
        st.session_state.high_status_offline = 100 - st.session_state.high_status_online
        st.session_state.initial_online_avg = (
            st.session_state.low_status_online + st.session_state.high_status_online
        ) // 2
        st.session_state.initial_offline_avg = 100 - st.session_state.initial_online_avg
        st.session_state.experiment_step = "processing"

def processing():
    """Processing Step"""
    st.title("Waiting for Robot")
    
    with st.spinner("Please wait..."):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.05)
    
    st.success("Task completed successfully!")
    
    if st.button("Next Step"):
        st.session_state.experiment_step = 2

def step_2():
    """Step 2: System Guidance and Review"""
    st.title("System Review")
    st.info("After submitting your answer, please wait for your collaborator to complete their response.")
    
    st.write(f"Low-status participant: {st.session_state.low_status_online}% online, {st.session_state.low_status_offline}% offline.")
    st.write(f"High-status participant: {st.session_state.high_status_online}% online, {st.session_state.high_status_offline}% offline.")
    st.write(f"The average decision is {st.session_state.initial_online_avg}% online and {st.session_state.initial_offline_avg}% offline.")
    
    final_value = st.slider(
        "Adjust your final value for online advertising (percentage):",
        min_value=0, max_value=100, value=st.session_state.initial_online_avg, key="final_slider"
    )
    if st.button("Submit Final Decision", key="final_submit"):
        st.session_state.final_online = final_value
        st.session_state.final_offline = 100 - final_value
        st.session_state.experiment_step = "questionnaire"

def questionnaire():
    """Questionnaire Page"""
    st.title("Questionnaire")
    st.markdown("""
    Next, we kindly ask you to complete a short survey to help us better understand your interaction experience and feelings.
    """)
    questionnaire_url = "https://docs.google.com/forms/d/e/1FAIpQLSehHPA4ny-bSevnnfEnqCeRHSSQSumRJyyephxXlBiSjsJzxQ/viewform"
    st.components.v1.iframe(questionnaire_url, width=800, height=600, scrolling=True)
    st.info("Submit your response after filling in the fields.")
    
    if st.button("Finish Questionnaire"):
        st.session_state.experiment_step = "post_experiment"

def post_experiment_page():
    """Post-Experiment Instructions"""
    st.title("Post-Experiment Instructions")
    st.markdown("""
    Thank you for completing this experiment!\n  
    As a token of our appreciation, we will provide you with a small candy gift.\n  
    Additionally, we would like to clarify that the **group bonus** mentioned during the experiment is purely a part of the experimental design and **does not** have any actual impact based on the evaluation results with the robot.  
    \n Thank you again for your participation! Do you have any questions?
    """)

# Main Navigation
if st.session_state.experiment_step == "guide":
    survey_guidance()
elif st.session_state.experiment_step == 0:
    start()
elif st.session_state.experiment_step == 1:
    step_1()
elif st.session_state.experiment_step == "processing":
    processing()
elif st.session_state.experiment_step == 2:
    step_2()
elif st.session_state.experiment_step == "questionnaire":
    questionnaire()
elif st.session_state.experiment_step == "post_experiment":
    post_experiment_page()
