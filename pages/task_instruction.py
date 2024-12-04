import streamlit as st
import time
from utils.initialized_database import get_connection 

# Set page configuration as the first Streamlit command
st.set_page_config(page_title="Survey & Experiment", page_icon="📊")

# Initialize session state
if "experiment_step" not in st.session_state:
    st.session_state.experiment_step = "guide"
if "participant_decision" not in st.session_state:
    st.session_state.participant_decision = None
if "robot_decision" not in st.session_state:
    st.session_state.robot_decision = None

if "custom_response" not in st.session_state:
    st.session_state.custom_response = None


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

    # Text input for experiment code
    st.session_state.custom_response = st.text_input("Please enter your experiment code:")
    
    if 'custom_response' in st.session_state.custom_response is not None:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Insert the data into the User table
            cursor.execute(
                "INSERT INTO [User] (ID) VALUES (?);",
                (st.session_state.custom_response,)
            )
            conn.commit()
            st.success("Numeric value saved successfully!")

        except Exception as e:
            st.error(f"An error occurred: {e}")

        finally:
            cursor.close()
            conn.close()
    # Handle experiment code submission
    if st.button("Submit Response"):
        if st.session_state.custom_response:  # Ensure input is not empty
            if st.session_state.custom_response == "01":
                st.session_state["role_assigned"] = True
                st.session_state["success_message"] = (
                    "Your role is **Creative Worker**. "
                    "This role is primarily responsible for generating and managing key ideas. "
                    "During conversations, you are expected to use **a more commanding tone** when interacting with other collaborators. "

                    "In the final stage, **you have the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**Your collaborator does not** have such control over you."
                )
            elif st.session_state.custom_response == "02":
                st.session_state["role_assigned"] = True
                st.session_state["success_message"] = (
                    "Your role is **Creative Worker**. "
                    "This role is primarily responsible for generating and managing key ideas. "
                    "During conversations, you are expected to use **a more commanding tone** when interacting with other collaborators. "

                    "In the final stage, **your collaborator has the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**You do not** have such control over them."
                )
            elif st.session_state.custom_response == "03":
                st.session_state["role_assigned"] = True
                st.session_state["success_message"] = (
                    "Your role is **Support Worker**. "
                    "This role is mainly responsible for small tasks and record-keeping. "
                    "During conversations, you are expected to use **a more polite tone** when interacting with other collaborators. "

                    "In the final stage, **you have the authority to distribute the group bonus** based on the contributions made during the collaboration. "
                    "**Your collaborator does not** have such control over you."
                )
            elif st.session_state.custom_response == "04":
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
        st.session_state.participant_decision = numeric_value
        
        # Robot decision: adjust based on boundary conditions
        if numeric_value - 17 < 0:
            st.session_state.robot_decision = max(0, min(100, numeric_value + 27))
        elif numeric_value + 17 > 100:
            st.session_state.robot_decision = max(0, min(100, numeric_value - 27))
        else:
            st.session_state.robot_decision = max(0, min(100, numeric_value - 27)) 
        
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

    participant_decision = st.session_state.participant_decision
    robot_decision = st.session_state.robot_decision
    
         # insert data to database, robot and user response
    if 'participant_decision' in st.session_state and 'robot_decision' in st.session_state:
        if st.session_state.participant_decision is not None and st.session_state.robot_decision is not None:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                # Insert participant decision into User_response table
                cursor.execute(
                    "INSERT INTO User_response (Response) VALUES (?);",
                    (st.session_state.participant_decision,)
                )
                conn.commit()
                st.success("Participant decision saved successfully!")

                # Insert robot decision into Robot table
                cursor.execute(
                    "INSERT INTO Robot (Response) VALUES (?);",
                    (st.session_state.robot_decision,)
                )
                conn.commit()
                st.success("Robot decision saved successfully!")

            except Exception as e:
                st.error(f"An error occurred: {e}")

            finally:
                cursor.close()
                conn.close()
    # Determine roles and images based on custom_response
    if st.session_state.custom_response == "01":
        participant_status = "Creative Worker"
        robot_status = "Support Worker"
        participant_image = "4.png"
        participant_power="have the authority to distribute the group bonus"
        robot_image = "1.png"
        robot_power="do not have the authority to distribute the group bonus"
    elif st.session_state.custom_response == "02":
        participant_status = "Creative Worker"
        robot_status = "Support Worker"
        participant_power="do not have the authority to distribute the group bonus"
        participant_image = "4.png"
        robot_power="have the authority to distribute the group bonus"
        robot_image = "2.png"
    elif st.session_state.custom_response == "03":
        participant_status = "Support Worker"
        robot_status = "Creative Worker"
        participant_power="have the authority to distribute the group bonus"
        participant_image = "3.png"
        robot_power="do not have the authority to distribute the group bonus"
        robot_image = "1.png"
    elif st.session_state.custom_response == "04":
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
    st.info("You can adjust the final answer or not at all!")
    
    start_time = time.time()
    final_value = st.slider(
        label="Your decision for online advertising:",
        min_value=0, max_value=100, value=participant_decision, key="final_slider"
    )
    end_time = time.time()
    time_interval = end_time - start_time
    # check whether the user change the answer
    answer_change = False
    if final_value == participant_decision:
        answer_change = False
    else:
        answer_change = True

    if answer_change:  # Fix the condition syntax
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Insert the answer change into the User_response table
            cursor.execute(
                "INSERT INTO User_response (Changed_answer) VALUES (?);",
                (answer_change,)  # Use 1 to indicate True in the database
            )
            conn.commit()
            st.success("Answer change saved successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
    # calculate the time interval on change the slider
    if time_interval >0:
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Insert the time_interval into the User_response table
            cursor.execute(
                "INSERT INTO User_response (Change_interval_time) VALUES (?);",
                (time_interval,)
            )
            conn.commit()
            st.success("Time interval saved successfully!")

        except Exception as e:
            st.error(f"An error occurred: {e}")

        finally:
            cursor.close()
            conn.close()

    # Submit button with unique key
    if st.button("Submit Final Decision"):
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
