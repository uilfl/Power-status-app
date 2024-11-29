import streamlit as st
import random

import importlib.util


# Initialize session state for robot and human progress if not set
if 'robot_progress' not in st.session_state:
    st.session_state.robot_progress = random.randint(0, 100)

if 'human_progress' not in st.session_state:
    st.session_state.human_progress = 50  # Default value, can be set by another page



if 'changed_human_progress' not in st.session_state:
    st.session_state.changed_human_progress = None

# Title
st.title("Task Instructions")

# Create two columns for the layout
col1, col2 = st.columns(2)

# Robot Performance (Randomly Decided)
with col1:
    st.subheader("Robot Performance")
    st.progress(st.session_state.robot_progress / 100)
    st.write(f"Current: {st.session_state.robot_progress}%")

# Human Performance (From Another Page)
with col2:
    st.subheader("Human Performance")
    st.write(f"Initial: {st.session_state.human_progress}%")
    
    # Option to change the value
    if st.button("Change Human Progress"):
        st.session_state.human_progress = st.slider(
            "Adjust Human Progress", 0, 100, st.session_state.human_progress
        )
        st.session_state.changed_human_progress = st.session_state.human_progress
    else:
        st.write(f"Current (unchanged): {st.session_state.human_progress}%")

# Final Confirmation Button
if st.button("Confirm"):
    st.session_state.current_page = 'waiting'
    st.experimental_rerun()