""" Project Summary """

import streamlit as st 

def page1_summary_body():
    
    # Heading
    st.write("### Quick Project Summary")

    # Project Terms and Jargons
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* A **customer** is an individual who uses banking services(bank account, credit card, etc).\n"
        f"* An **exited customer** is a user who has stopped using banking services.\n"
        f"* A **credit score** talks about the creditworthiness of the individual.\n "
        f"* Each customer has a **tenure** level, that is the number of years this person " 
        f"has used a service.\n\n")
    
    # Project Dataset
    st.info(
        f"**Project Dataset**\n"
        f"* The dataset contains information on **bank customers** who either left or "
        f"continue to be a customer. \n"
        f"* It has details related to customer profiles like age, gender, surname, salary, credit score, and geography. \n"
        f"* Customer relationship information, like how many products they hold with the bank,"
        f" the number of years they have been with the bank, customer's account balance, " 
        f" whether the customer is active, etc.")
   

    # Link to README file
    st.write(
        f"* For additional information, please **read** the project "
        f"[README file](https://github.com/AbhilashAynipully/BankCustomerExitPredictor/blob/main/README.md)"
        )
    

    # Business Requirements
    st.success(
        f"The project has **2 business requirements:**\n"
        f"* 1 - The bank is interested in identifying from the available data, the most "
        f"relevant customer attributes which are correlated to customer exit.\n\n"
        f"* 2 - The bank is also interested in predicting if a newly onboarded customer " 
        f"would exit. If yes, when will it be?"
        )