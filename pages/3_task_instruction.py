import streamlit as st
import random

# Task Instructions Section
st.title("Task Instructions")
st.subheader("[Advertising Investment Decision-Making]")
st.markdown('''
The company is planning a marketing campaign for a clothing brand and needs your help in developing an advertising strategy. Your goal is to maximize brand exposure and sales conversion rates. With a total budget of **1 million NT dollars**, you must allocate funds between **online and offline advertising channels** within the budget constraints.  

**Online Advertising:**  
This includes social media, search engine ads, and email campaigns. It typically reaches a wide younger audience but is highly competitive and requires precise targeting strategies.  

**Offline Advertising:**  
This includes outdoor billboards, event sponsorships, and in-store promotions. It is effective at attracting specific local target audiences but has a more limited reach and higher costs.
''')
st.caption("Please carefully weigh the advantages and limitations of both options and allocate the budget percentages based on your judgment. After adjusting the slider, press the \"Confirm\" button to submit your answer.")

# Initialize session state to track progress
if "experiment_step" not in st.session_state:
    st.session_state.experiment_step = 1  # Tracks the experiment step
if "low_status_online" not in st.session_state:
    st.session_state.low_status_online = None
if "high_status_online" not in st.session_state:
    st.session_state.high_status_online = None

# Main Experiment Flow
if st.session_state.experiment_step == 1:
    # Step 1: Initial Decision
    st.subheader("Your Decision")
    numeric_value = st.slider(
        "Set a percentage for online advertising (percentage):",
        min_value=0, max_value=100, value=50
    )

    if st.button("Confirm"):
        # Random adjustment of participant's choices within ±10%
        st.session_state.low_status_online = max(0, min(100, numeric_value + random.randint(-10, 10)))
        st.session_state.high_status_online = max(0, min(100, numeric_value + random.randint(-10, 10)))

        # Ensure total percentages do not exceed 100
        st.session_state.low_status_offline = 100 - st.session_state.low_status_online
        st.session_state.high_status_offline = 100 - st.session_state.high_status_online

        # Calculate initial average decision
        st.session_state.initial_online_avg = (
            st.session_state.low_status_online + st.session_state.high_status_online
        ) // 2
        st.session_state.initial_offline_avg = 100 - st.session_state.initial_online_avg

        # Move to next step
        st.session_state.experiment_step = 2

elif st.session_state.experiment_step == 2:
    # Step 2: System Guidance and Review

    st.info("After submitting your answer, please wait for your collaborator to complete their response.")

    # Display individual results
    st.write(f"Low-status participant: I lean towards allocating {st.session_state.low_status_online}% for online advertising and {st.session_state.low_status_offline}% for offline advertising.")
    st.write(f"High-status participant: I believe the allocation should be {st.session_state.high_status_online}% for online advertising and {st.session_state.high_status_offline}% for offline advertising.")

    # Display initial system decision

    st.write(f"The average decision is {st.session_state.initial_online_avg}% for online advertising and {st.session_state.initial_offline_avg}% for offline advertising.")
    st.info("Would you like to revise your answer?")

    # Final decision adjustment
    final_value = st.slider(
        "Adjust your final value for online advertising (percentage):",
        min_value=0, max_value=100, value=st.session_state.initial_online_avg
    )

    if st.button("Submit Final Decision"):
        # Save the final decision
        st.session_state.final_online = final_value
        st.session_state.final_offline = 100 - final_value

        # Display final decision
        st.subheader("Final Decision")
        st.info(f"Your final decision average is: {st.session_state.final_online}% for online advertising and {st.session_state.final_offline}% for offline advertising.")

        # End experiment
        st.session_state.experiment_step = 3

elif st.session_state.experiment_step == 3:
    # Step 3: End of Experiment
    st.success("This is the end of our experiment. Thank you for participating!")
