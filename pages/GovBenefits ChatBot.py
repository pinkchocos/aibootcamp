import streamlit as st
from helper_functions.utility import check_password
from helper_functions import func

# Page settings
st.set_page_config(
    page_title="Government Subsidies Guru",
    page_icon="💰",
    layout="centered"
)

# Do not continue if check_password is not True.
if not check_password():
    st.stop()

# Sidebar navigation
with st.sidebar:
    st.page_link('main.py', label='About GovAssist', icon='💰')
    st.page_link('pages/Methodology.py', label='Methodology', icon='⚙️')
    st.page_link('pages/Eligibility Advisor.py', label='Eligibility Advisor', icon='🤵')
    st.page_link('pages/GovBenefits ChatBot.py', label='GovBenefits ChatBot', icon='💬')

# Page title
st.title("GovBenefits ChatBot")
st.write("Curious about details of each government scheme? Ask me before contacting service/call officers.")

# Example prompts
st.markdown("### Examples you can try:")
st.markdown("- Why is Annual Value (AV) used for Assurance Package (AP) Seniors' Bonus but not for AP Cash?")
st.markdown("- If I own more than one property, will I be eligible for Assurance Package (AP) benefits?")
st.markdown("- Can I withdraw my GSTV – MediSave?")

# User input
user_input = st.text_area(
    "Ask your question about Singapore government benefits:",
    placeholder="E.g., How will I know if the GSTV – Cash and/or GSTV – MediSave has been credited to my bank/CPF account?"
)

# Submit
if st.button("Get Answer"):
    if user_input.strip():
        with st.spinner("Finding the most relevant answer from FAQ..."):
            response = func.get_faq_answer(user_input)  # Uses RAG FAQ bot
            st.subheader("Answer")
            st.write(response)
    else:
        st.warning("Please enter a question to get an answer.")
