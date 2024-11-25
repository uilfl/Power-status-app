import streamlit as st
st.title("Task Instructions")
    
# Create two columns for the layout
col1, col2 = st.columns(2)
    
with col1:
        st.subheader("Robot Performance")
        robot_progress = st.slider("Robot Progress", 0, 100, 30)
        st.progress(robot_progress/100)
        st.write(f"Current: {robot_progress}%")
        
with col2:
        st.subheader("Human Performance")
        human_progress = st.slider("Human Progress", 0, 100, 80)
        st.progress(human_progress/100)
        st.write(f"Current: {human_progress}%")
    
    # Add two sample images side by side
image_col1, image_col2 = st.columns(2)
with image_col1:
        st.image("https://via.placeholder.com/200x200", caption="Sample Image 1")
with image_col2:
        st.image("https://via.placeholder.com/200x200", caption="Sample Image 2")
        
    # Add a slider between images
comparison_slider = st.slider("Compare Images", 0, 100, 50)
    
if st.button("Confirm"):
        st.session_state.current_page = 'waiting'
        st.experimental_rerun()
