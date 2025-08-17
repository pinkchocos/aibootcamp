import streamlit as st
from helper_functions import func
from helper_functions.utility import check_password

## Create a LLM-assisted bot to help provide scripts or strategies for better negotation deals

st.set_page_config(
    page_title="Government Subsidies Guru",
    page_icon="💰",
    layout="centered")

# Do not continue if check_password is not True.
if not check_password():
   st.stop()

with st.sidebar:
    st.page_link('main.py', label='About GovAssist', icon='💰')
    st.page_link('pages/Methodology.py', label='Methodology', icon='⚙️')
    st.page_link('pages/Eligibility Advisor.py', label='Eligibility Advisor', icon='🤵')
    st.page_link('pages/GovBenefits ChatBot.py', label='GovBenefits ChatBot', icon='💬')

## Guide for the user on what to include in his/her inputs
st.title("Eligibility Advisor")
st.write("Wondering what support you're eligible for? Just chat with me! I’ll help you discover the right government subsidies, explain the amounts, and guide you on what to do next.")
st.write("Do indicate as many information as possible in order for me to provide a more comprehensive advice. Below are some examples:")
citizenship = st.selectbox("- Citizenship:", ["Singapore Citizen","Singapore PR", "Foreigner"])
age = st.slider("- Age as of this year:", 1,99,1)
properties = st.slider("- How many properties you own:", 0,10,1)
ppty_type = st.selectbox("- Do you own any HDB flat?:", ["Yes","No"])
#flat_type = st.selectbox("- Flat type:", ["None", "1-2 room","3-room","4-room","5-room","Executive/Multi-Generation"])
#income = st.selectbox("- Assessable Income (in a year) range:", ["Less than $22,000","$22,000 to $34,000","$34,000 to $39,000","$39,000 to $100,000","More than $100,000"])
income = st.slider("- Assessable Income (in a year):", 0,1000000,1)
#annual_val = st.selectbox("- Annual Value (AV) of home:", ["Less than $13,000","$13,000 to $21,000","$21,000-$25,000","$25,000 to $31,000","More than $31,000"])
annual_val = st.slider("- Annual Value (AV) of home:", 0,600000,1)
question = st.text_area("State your question here:")
print(f"User question: {question}")

# Submit of user inputs to the LLM
if st.button("Get Advice"):
    if question:
        if func.check_for_malicious_intent(question) == 'Y':
            st.write("Sorry, we cannot process this request.")
        else:
            with st.spinner("Getting advice..."):
                user_input = func.eligiblity_user_input(ppty_type,citizenship,age, properties,income,annual_val,question)
                print(f"User info: {user_input}")
                response = func.eligibility_model(user_input)["result"]
                st.subheader("Eligibility Advice")
                st.write(response)
    else:
        st.warning("Please enter your information to get advice.")