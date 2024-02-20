""" Hypothesis and Validation """

import streamlit as st


def page3_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # Conclusions are based on customer exit Study notebook
    st.success(
        f"**1. The management team believes, customers who use only one product tend to exit.**\n\n" 
        f"The correlation study at Customer Exit Study supports that. As per the study report, "
        f"customers with more than one product tend to exit less. \n\n"
    )

    st.error(
        f"**2. As per the customer service team, the customer's account balance has no impact on exit.** \n\n"
        f"The correlation study doesn't support that. As per the study report, customers with lower salaries tend to exit less. "
        f"Basis this finding further discussions and investigations will be conducted with the customer service team. \n\n"
    )
    st.error(
        f"**3. The sales team believes that the customer's salary is the most important factor in deciding on exit.**\n\n"
        f"The correlation study doesn't support that. As per study report, customer's salary has no major impact on exit. "
        f"Based on this finding further discussions and investigations will be conducted with the sales team. \n\n"
    )