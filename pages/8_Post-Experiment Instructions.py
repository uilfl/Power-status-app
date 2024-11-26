import streamlit as st
import sqlite3
import os

def main():
    st.title("Post-Experiment Instructions")

    # Provide experiment details
    st.markdown("""
    Thank you for completing this experiment!  
    As a token of our appreciation, we will provide you with a small candy gift.  
    Additionally, we would like to clarify that the "group bonus" mentioned during the experiment is purely a part of the experimental design and does not have any actual impact based on the evaluation results with the robot.  
    Thank you again for your participation! Do you have any questions?
    """)
