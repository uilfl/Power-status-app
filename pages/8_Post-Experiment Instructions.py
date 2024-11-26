import streamlit as st
import sqlite3
import os

def post_experiment_page():
    st.title("Post-Experiment Instructions")

    # Provide experiment details
    st.markdown("""
    Thank you for completing this experiment!\n  
    As a token of our appreciation, we will provide you with a small candy gift.\n  
    Additionally, we would like to clarify that the **group bonus** mentioned during the experiment is purely a part of the experimental design and **does not** have any actual impact based on the evaluation results with the robot.  
    \n Thank you again for your participation! Do you have any questions?
    """)

# Main entry point
if __name__ == "__main__":
    post_experiment_page()
