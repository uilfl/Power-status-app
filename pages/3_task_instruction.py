import streamlit as st
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


def get_power_status():
    # Placeholder implementation
    return 'ON'

def main():
    st.title("Power Status Checker")
    status = get_power_status()
    st.write(f"The current power status is: {status}")

if __name__ == "__main__":
    main()