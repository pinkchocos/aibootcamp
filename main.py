import streamlit as st
from helper_functions.utility import check_password
# Main page content (About Us)
# Includes Project Overview, Objectives, Data Sources and Disclaimer
def main_page():

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

    st.title("About Us")

    st.markdown("""
    ## Project Overview
    Welcome to the GovAssist!
    The Eligibility Advisor aims to help Singaporeans easily navigate and understand their eligibility for various government assistance schemes and subsidies. 
    The GovBenefits ChatBot, on the other hand, answers Singaporeans' queries on the government schemes/benefits. This chatbot will serve as a user-friendly, conversational interface that simplifies the complex landscape of governemnt benefits by providing personalised guidance based on users' circumstances. 

    ## Objectives
    The goal of this project is to enhance accessibility, by:
    - Providing 24/7 automated assistance for users to explore government benefits
    - Reducing the need for users to manually search through multiple webpages
   
   It also aims to improve user experience by:
    - Simplifying complex eligibility criteria into conversational interactions 
    - Guiding users through a structured assessment process
    - Providing instant preliminary eligibility checks and estimated subsidy amounts
    
    At the same time, it aims to increase efficiency by reducing the workload on frontline service staffs handing enquiries as well as minimises the time users spent on researching different assistance schemes.

    ## Project Scope
    Our solution focuses on three core functionalities:
    - **Eligibility Advisor**: Allows users to check their eligibility for the respective government benefits.
    - **GovBenefits Chatbot**: Allows users to interact with the chatbot to know more about the government schemes/benefits out there.

    ## Data Sources
    Our insights and analysis are based on information found on https://www.govbenefits.gov.sg/. The dataset includes information on:

    **1.Eligibility Advisor**
    - Sub Scheme
    - Overview
    - Eligibility
    - When and how will I be paid

    **2.GovBenefits Chatbot**
    - Sub Scheme
    - FAQ
    """)

    with st.expander("**DISCLAIMER**", expanded=True):
        st.write("""

    **IMPORTANT NOTICE**: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decision making.

    **Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.**

    Always refer to https://www.govbenefits.gov.sg/ for the latest updates/news.

    """)

# Running the main function
if __name__ == '__main__':
    main_page()