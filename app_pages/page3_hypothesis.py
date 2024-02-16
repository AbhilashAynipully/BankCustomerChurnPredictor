""" Hypothesis and Validation """

import streamlit as st


def page3_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # Conclusions are based on customer exit Study notebook
    st.success(
        f"**1. The management team believes, customers who use only one product tend to exit.\n\n"
        f"The correlation study at Customer Exit Study supports that. \n\n"
    )

    st.error(
        f"2 As per customer service team, customer's account balance has no impact on exit. "
        f"The correlation study doesn't support that. Customers with lower salary tend to exit less. "
        f"Basis this finding further discussions and investigations will be conducted with customer service team. \n\n"
    )
    st.error(
        f"3 Sales team believes customer's salary is the most important factor in deciding exit."
        f"The correlation study doesn't support that. Customer salary has no major impact on exit."
        f"Basis this finding further discussions and investigations will be conducted with sales team. \n\n"
    )