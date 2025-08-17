import streamlit as st
from helper_functions.utility import check_password

# Methodology
# Depicts image illustrating the workflow for this application

st.set_page_config(
page_title="Government Subsidies Guru",
page_icon="💰",
layout="centered")

# Do not continue if check_password is not True.
if not check_password():
   st.stop()


st.image("data/methodology.png", caption="Methodology", use_container_width=True)

with st.sidebar:
    st.page_link('main.py', label='About GovAssist', icon='💰')
    st.page_link('pages/Methodology.py', label='Methodology', icon='⚙️')
    st.page_link('pages/Eligibility Advisor.py', label='Eligibility Advisor', icon='🤵')
    st.page_link('pages/GovBenefits ChatBot.py', label='GovBenefits ChatBot', icon='💬')