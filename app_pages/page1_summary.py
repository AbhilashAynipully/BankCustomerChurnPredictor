""" Project Summary """

import streamlit as st 

def page1_summary_body():
    
    # Heading
    st.write("### Quick Project Summary")

    # Project Terms and Jargons
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* A **customer** is a individual who uses banking services(bank account, credit card etc).\n"
        f"* An **exited customer** is a user who has stopped using banking services.\n"
        f"* A **credit score** talks about the credit worthiness of the individual.\n "
        f"* This customer has a **tenure** level, the number of months this person " 
        f"has used our product/service.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset contains information on **bank customers** who either left the bank or"
        f"continue to be a customer. There are details regarding:"
        f"* Customer profile, like age, gender, surname, salary, credit score and geography."
        f"* Customer information, like how many products they hold with bank,"
        f"the number of years they have been wih bank,customer's account balance, whether customer is active")
   

    # Link to README file
    st.write(
        f"* For additional information, please **read** the "
        f"[Project README file](https://github.com/AbhilashAynipully/BankCustomerExitPredictor/blob/main/README.md)."
        )
    

    # Business Requirements
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The bank is interested in identyfying from the available data most"
        f"relevant customer attributes which are correlated to customer exit.\n"
        f"* 2 - The bank is also interested in predicting if a newly onboarded customer" 
        f"would exit. If yes, will it be within a year or later"
        )