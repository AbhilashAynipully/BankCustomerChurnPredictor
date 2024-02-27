""" Hypothesis and Validation """

import streamlit as st


def page3_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # Conclusions are based on customer exit Study notebook
    st.success(
        f"**1. The management team believes: 'if customers use only one product, then they tend to exit more.'**\n\n" 
        f"- The correlation study supports that. As per the study report, "
        f"customers using only one product tend to exit more. \n\n"
    )

    st.error(
        f"**2. According to customer service team: 'if customer's account balance is high, then they tend to exit less.'** \n\n"
        f"- The correlation study doesn't support that. As per the study report, customers with higher account balances tend to exit more. "
        f"Based on this, discussions and planning will be done with the customer service team. \n\n"
    )
    st.error(
        f"**3. The sales team believes: 'if customer's salary is low, then they tend to exit more.'**\n\n"
        f"- The correlation study doesn't support that. As per the study report, the customer's salary has no major influence on exit. "
        f"Based on this, discussions and planning will be done with the sales team. \n\n"
    )