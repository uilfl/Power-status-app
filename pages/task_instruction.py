import streamlit as st
import time
import random
from utils.initialized_database import get_connection 

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="Survey & Experiment", page_icon="📊")

# Initialize session state
if "experiment_step" not in st.session_state:
    st.session_state.experiment_step = "guide"
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "group_ID" not in st.session_state:
    st.session_state.group_ID = ""
if "participant_decision" not in st.session_state:
    st.session_state.participant_decision = None
if "robot_decision" not in st.session_state:
    st.session_state.robot_decision = None
if "participant_final_decision" not in st.session_state:
    st.session_state.participant_final_decision = None
if "time_interval_response" not in st.session_state:
    st.session_state.time_interval_response = 0
if "time_interval_change" not in st.session_state:
    st.session_state.time_interval_changee = 0  
if "answer_change" not in st.session_state:
    st.session_state.answer_change = 0

# name ='' #st.session_state.custom_name
# group_ID = '01' #st.session_state.group_ID
# participant_answer = 0 #st.session_state.participant_decision
# time_interval_response = 0 
# robot_decision = 0 #st.session_state.robot_decision
# final_value = 0 #st.session_state.participant_final_decision
# time_interval_change = 0
# answer_change = 0 #st.session_state.answer_change




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
    """)
    
    # if st.button("Proceed to the Experiment Instructions"):
        # st.session_state.experiment_step = "start"  # Proceed to the next step
    st.button("Proceed to the Experiment Instructions", key="start", on_click=lambda: st.session_state.update(experiment_step="start"), type="primary")


def start():
    """Start Page: Role Assignment and Instructions"""
    st.title("Experimental Procedures")
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
    

    # name = st.session_state.custom_name
     # Text input for experiment name
    st.session_state.user_name = st.text_input("Please enter your name:")
    # Text input for experiment code assigned as int 
    st.session_state.group_ID = st.text_input("Please enter your experiment code:")
    
    
    
    # Handle experiment code submission
    if st.button("Submit Response", type="primary"):
        if st.session_state.group_ID:  # Ensure input is not empty
            if st.session_state.group_ID == "01":
                st.session_state["role_assigned"] = True
                st.session_state["success_message"] = (
                    "Your role is **Creative Worker**. "
                    "This role is primarily responsible for generating and managing key ideas. "
                    "During conversations, you are expected to use **a more commanding tone** when interacting with other collaborators. "

                    "In the final stage, **you have the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**Your collaborator does not** have such control over you."
                )
            elif st.session_state.group_ID == "02":
                st.session_state["role_assigned"] = True
                st.session_state["success_message"] = (
                    "Your role is **Creative Worker**. "
                    "This role is primarily responsible for generating and managing key ideas. "
                    "During conversations, you are expected to use **a more commanding tone** when interacting with other collaborators. "

                    "In the final stage, **your collaborator has the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**You do not** have such control over them."
                )
            elif st.session_state.group_ID == "03":
                st.session_state["role_assigned"] = True
                st.session_state["success_message"] = (
                    "Your role is **Support Worker**. "
                    "This role is mainly responsible for small tasks and record-keeping. "
                    "During conversations, you are expected to use **a more polite tone** when interacting with other collaborators. "

                    "In the final stage, **you have the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**Your collaborator does not** have such control over you."
                )
            elif st.session_state.group_ID == "04":
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
    
    # group_ID = st.session_state.group_ID
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
        st.button("Next Page", key="to_step1", on_click=lambda: st.session_state.update(experiment_step="step1"), type="primary")
def step_1():
    """Step 1: Initial Decision"""
    st.title("Task Instructions")
    st.subheader("Advertising Investment Decision-Making")
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
    
    start_time = time.time()
    numeric_value = st.slider(
        "Set a percentage for online advertising (percentage):",
        min_value=0, max_value=100, value=50, key="decision_slider"
    )
    end_time = time.time()
    
    st.session_state.time_interval_response = end_time - start_time
    # participant_answer = numeric_value

    
    
    def confirm_logic():
        st.session_state.participant_decision = numeric_value

        # Robot decision: adjust based on boundary conditions
        if numeric_value - 27 <= 0:
            st.session_state.robot_decision = max(0, min(100, numeric_value + 27))
        elif numeric_value + 27 >= 100:
            st.session_state.robot_decision = max(0, min(100, numeric_value - 27))
        else:
            st.session_state.robot_decision = max(0, min(100, numeric_value - 27))

        # 更新狀態
        st.session_state.experiment_step = "step2"
    robot_decision = st.session_state.robot_decision
    # 按鈕與邏輯綁定
    st.button("Confirm", key="confirm_button", on_click=confirm_logic, type="primary")
    
       
def step_2():
    """Step 2: System Guidance and Review"""
    st.title("System Review")
    
    if "loading_complete" not in st.session_state:
        st.session_state.loading_complete = False

    if not st.session_state.loading_complete:
        st.write("Please wait for Robot...")
        with st.spinner("Please be patient and give us some time."):
            progress_bar = st.progress(0)
            for i in range(100):
                progress_bar.progress(i + 1)
                time.sleep(0.05)
        st.session_state.loading_complete = True  # 加载完成后更新状态

   
    participant_decision = st.session_state.participant_decision
    robot_decision = st.session_state.robot_decision


    # Determine roles and images based on group_ID
    if st.session_state.group_ID == "01":
        participant_status = "Creative Worker"
        robot_status = "Support Worker"
        participant_image = "4.png"
        participant_power="have the authority to distribute the group bonus"
        robot_image = "1.png"
        robot_power="do not have the authority to distribute the group bonus"
    elif st.session_state.group_ID == "02":
        participant_status = "Creative Worker"
        robot_status = "Support Worker"
        participant_power="do not have the authority to distribute the group bonus"
        participant_image = "3.png"
        robot_power="have the authority to distribute the group bonus"
        robot_image = "2.png"
    elif st.session_state.group_ID == "03":
        participant_status = "Support Worker"
        robot_status = "Creative Worker"
        participant_power="have the authority to distribute the group bonus"
        participant_image = "4.png"
        robot_power="do not have the authority to distribute the group bonus"
        robot_image = "1.png"
    elif st.session_state.group_ID == "04":
        participant_status = "Support Worker"
        robot_status = "Creative Worker"
        participant_power="do not have the authority to distribute the group bonus"
        participant_image = "3.png"
        robot_power="have the authority to distribute the group bonus"
        robot_image = "2.png"
    else:
        participant_status = "Unknown"
        robot_status = "Unknown"
        participant_image = None
        robot_image = None

    col1, col2 = st.columns(2)

    # Robot's decision on the left
    with col1:
        st.subheader(f"Robot: {robot_status}")
        if robot_image:
            st.image(robot_image, caption=robot_power, width=150)  # Reduced size
        st.progress(robot_decision / 100)  # Robot progress bar
        st.write(f"Robot's decision for online advertising: **{robot_decision}%**")

    # Participant's decision on the right
    with col2:
        st.subheader(f"You: {participant_status}")
        if participant_image:
            st.image(participant_image, caption=participant_power, width=150)  # Reduced size
        st.progress(participant_decision / 100)  # Participant progress bar
        st.write(f"Your decision for online advertising: **{participant_decision}%**")
    
    # Final adjustment slider
    st.info("You can adjust the final answer, or not adjust it at all! But you will eventually see each other's average answers.")
    
    start_time = time.time()
    
    final_value = st.slider(
        label="Your decision for online advertising:",
        min_value=0, max_value=100, value=participant_decision, key="final_slider"
    )
    end_time = time.time()
    st.session_state.participant_final_decision=final_value
    st.session_state.time_interval_change = end_time - start_time
    # check whether the user change the answer
    
    if final_value == participant_decision:
        st.session_state.answer_change = 0
    else:
        st.session_state.answer_change = 1
    

    # Submit button with unique key
    if st.button("Submit Final Decision", key="questionnaire", on_click=lambda: st.session_state.update(experiment_step="questionnaire"), type="primary"):
        st.session_state.final_online = final_value
        st.session_state.final_offline = 100 - final_value

    

def questionnaire():
    """Questionnaire Page"""
    st.title("Questionnaire")
    if "participant_decision" in st.session_state and "robot_decision" in st.session_state:
        robot_avg = (st.session_state.participant_decision+st.session_state.robot_decision)/2
        st.info(f"You & Robot average decision for online advertising: **{robot_avg}%**")
    else:
        st.warning("Decision data is not available yet.")
    st.markdown("""
    Next, we kindly ask you to complete a short survey to help us better understand your interaction experience and feelings.
    """)
    questionnaire_url = "https://docs.google.com/forms/d/e/1FAIpQLSehHPA4ny-bSevnnfEnqCeRHSSQSumRJyyephxXlBiSjsJzxQ/viewform"
    st.components.v1.iframe(questionnaire_url, width=800, height=600, scrolling=True)
    st.info("Submit your response after filling in the fields.")
    
    st.button("Finish Questionnaire", key="go_post_experiment", on_click=lambda: st.session_state.update(experiment_step="post_experiment"), type="primary")

def post_experiment_page():
    """Post-Experiment Instruction"""
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
elif st.session_state.experiment_step == "start":
    start()
elif st.session_state.experiment_step == "step1":
    step_1()
elif st.session_state.experiment_step == "step2":
    step_2()
elif st.session_state.experiment_step == "questionnaire":
    questionnaire()
elif st.session_state.experiment_step == "post_experiment":
    post_experiment_page()
    # user_id = random.randint(1, 1000)
    try:
        conn = get_connection()
        cursor = conn.cursor()

            # Insert all columns into the User_Response table
        cursor.execute(
            """
            INSERT INTO User_Response 
<<<<<<< HEAD
            (user_id, user_name, group_id, response_answer,response_time, robot_answer, Change, Changed_answer, Change_interval_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
            """,
            (
                user_id,                   # INT
                name,                      # VARCHAR(MAX)
                custom_response,           # VARCHAR(50)
                participant_answer,
                time_interval_response,        # VARCHAR(50)    # INT
                robot_decision,            # INT
                answer_change,             # INT
                final_value,               # INT
                time_interval_change       # CHAR(50)
=======
            (user_name, group_id, response_answer, response_time, robot_answer, Change, Changed_answer, Change_interval_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """,
            (
                # user_id,                   # INT
                st.session_state.user_name,# VARCHAR(MAX)
                st.session_state.group_ID,# VARCHAR(50)
                st.session_state.participant_decision,# VARCHAR(50)
                st.session_state.time_interval_response,# INT
                st.session_state.robot_decision,# INT
                st.session_state.answer_change,# INT
                st.session_state.participant_final_decision,# INT
                st.session_state.time_interval_change# CHAR(50)
>>>>>>> 56e93d4b1be71053e5b3438b1ddb43b9c7a56e69
            )
        )
        conn.commit()
        st.success("User ID saved successfully!")

    except Exception as e:
        st.error(f"An error occurred: {e}")

    finally:
        cursor.close()
        conn.close()