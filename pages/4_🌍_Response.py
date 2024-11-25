import streamlit as st 
import time 

st.set_page_config(page_title="response", page_icon="🌍")

def set_query_params(page):
    if page == "Home":
        st.experimental_set_query_params(page="home")
    elif page == "Questionaire":
        st.experimental_set_query_params(page="questionaire")

def main():
    st.title("Q&A Interactive Interface")
    
    # Set up the UI header
    st.subheader("Interact with the options below to submit your response.")

    # Add a dropdown (select box) for choosing options
    st.markdown("**In the context of rapid globalization, with technological advancements and deepening cultural exchanges, how can organizations balance the need for localization while ensuring accuracy and effectiveness in cross-cultural communication, particularly in the areas of language translation and semantic understanding, to avoid misunderstandings or biases arising from cultural differences?**")

    # Add a slider to adjust a numeric value
    numeric_value = st.slider(
        "Set a numeric value:",
        min_value=0, max_value=100, value=50
    )
    # Add a submit button
    if st.button("Submit Response"):
        st.write(f"Submitted value: {numeric_value}")
# Dictionary to store button click times
button_click_times = {}

def on_button_click(button_name):
    """處理按鈕點擊事件"""
    button_click_times = {}
    current_time = time.time()  # 獲取當前秒級時間戳
    if button_name not in button_click_times:
        # 如果是第一次點擊該按鈕
        button_click_times[button_name] = current_time
        print(f"按鈕 '{button_name}' 的第一次點擊記錄，等待第二次點擊...")
    else:
        # 如果已經記錄過第一次點擊，計算時間差
        time_difference = current_time - button_click_times[button_name]
        print(f"按鈕 '{button_name}' 的兩次點擊間隔: {time_difference:.3f} 秒")
        # 重置該按鈕的時間戳


def submitted_page():
    st.title("Thank You!")
    conn = sqlite3.connect(db_file_path)  # File-based database connection
    st.write("You can go back to the main page or close this window.")
    main()
    # on_button_click("Submit Response")
    print("Connected to the SQLite database from 'Database/main.sql'")



main()

if "task_completed" not in st.session_state:
    st.session_state["task_completed"] = False

# 模擬任務完成的檢查
task = st.checkbox("完成任務")  # 用任務邏輯替換此處
if task:
    st.session_state["task_completed"] = True
    st.success("任務已完成！您現在可以進入下一頁。")

# 提供下一頁的按鈕（條件性顯示）
if st.session_state["task_completed"]:
    st.markdown("[進入下一頁](guide)")
else:
    st.warning("請先完成任務才能解鎖下一頁！")