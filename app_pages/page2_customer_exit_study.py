""" Customer Exit Study """

import plotly.express as px
import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_bank_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page2_customer_exit_study_body():

    # load bank customer data
    df = load_bank_data()

    # important variable to study as per ExitedCustomerDataAnalysis notebook
    imp_vars = ['Age','Balance','CreditScore','EstimatedSalary','Gender','Geography','NumOfProducts']

    st.write("### Customer Exit Study")
    st.info(
        f"* The bank is interested in identifying from the available data, the "
        f"most relevant customer attributes which are correlated to customer exit.")

    # inspect bank customer data
    if st.checkbox("Inspect Customer Base"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"please find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* We conducted a correlation study for better understanding of "
        f"the variables which are correlated to Customer Exit. \n"
        f"Variables which were found to be most correlated are: \n\n **{imp_vars}**"
    )

    #  Conclusions and Next steps based on customer exit study
    st.info(
        f"* The average age of customers who **exited is 45 years** and who **didn't exit is 35 years**. \n"
        f"* Customers having **more than one product tend to exit less.** \n"
        f"* Customers belonging to **Germany tend to exit more** than France and Spain. \n"       
        f"* Customers who exited usually have credit scores in the range of 600 to 675."
        f" However, customers who didn't exit tend to have slightly"
        f" higher credit scores in the range of 625 to 700. \n"
        f"* Customers who exited **didn't belong to any specific salary range.** \n"
        f"* Customers with lower account balances tend to exit less compared \n"
        f" to customers with higher account balances. \n"
    )

    # Exploratory Data Analysis (EDA) of most important variables
    df_eda = df.filter(imp_vars + ['Exited'])

    # Individual plots per variable
    if st.checkbox("Exit Levels per Variable"):
        variable_based_exit_level(df_eda)


# Variables Distribution basis customer exit
def variable_based_exit_level(df_eda):
    target_var = 'Exited'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)


def plot_categorical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df, x=col, hue=target_var,
                  order=df[col].value_counts().index)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  


def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig) 