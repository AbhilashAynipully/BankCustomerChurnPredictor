""" Hypothesis and Validation """

import streamlit as st


def page3_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # Conclusions are based on customer exit Study notebook
    st.success(
        f"* The management team believes, customers who use only one product tend to exit"
        f"The correlation study at Churned Customer Study supports that. \n\n"
    )

    st.warning(
        f"* As per customer service team, customer's account balance has no impact on exit. "
        f"The correlation study doesn't support that. Customers with lower salary tend to exit less. "
        f"Basis this finding further discussions and investigations will be conducted with customer service team. \n\n"

        f"* Sales team believes customer's salary is the most important factor in deciding exit."
        f"The correlation study doesn't support that. Customer salary has no major impact on exit."
        f"Basis this finding further discussions and investigations will be conducted with sales team. \n\n"
    )