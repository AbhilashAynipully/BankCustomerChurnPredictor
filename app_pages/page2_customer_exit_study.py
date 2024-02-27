""" Customer Exit Study """

import numpy as np
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_bank_data

import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
sns.set_style("whitegrid")


def page2_customer_exit_study_body():

    # load bank customer data
    df = load_bank_data()

    # important variables to study as per ExitedCustomerDataAnalysis notebook
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
        f"* We conducted a correlation study for a better understanding of "
        f"the variables that are correlated to Customer Exit. \n"
        f"Variables that were found to be most correlated are: \n\n **{imp_vars}**"
    )

    # Variable distribution Analysis
    df_imp = df.filter(imp_vars)

    # Individual plots per variable
    if st.checkbox("Variable Distribution"):
        variable_distribution(df_imp)

    # Exploratory Data Analysis (EDA) of most important variables
    df_eda = df.filter(imp_vars + ['Exited'])

    # Individual plots per variable
    if st.checkbox("Exit Levels per Variable"):
        variable_based_exit_level(df_eda)
    
    # Correlation and PPS Analysis
    if st.checkbox("Correlation and PPS Analysis"):
        cor(df)


    st.write("---")

    #  Conclusions based on customer exit study
    st.info(
        f"### Conclusions: \n"
        f"* The average age of customers who **exited is 45 years** and those who **didn't exit is 35 years**. \n"
        f"* Customers having **more than one product tend to exit less.** \n"
        f"* Customers belonging to **Germany tend to exit more** than France and Spain. \n"       
        f"* Customers who exited usually have credit scores in the range of 600 to 675."
        f" However, customers who didn't exit tend to have slightly"
        f" higher credit scores in the range of 625 to 700. \n"
        f"* Customers who exited **didn't belong to any specific salary range.** \n"
        f"* Customers with lower account balances tend to exit less compared \n"
        f" to customers with higher account balances. \n"
    )
    
    st.write("---")

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


# Variables Distribution
def variable_distribution(df_imp):

    for col in df_imp.columns.to_list():
        if df_imp[col].dtype == 'object':
                categorical_count(df_imp, col)
        else:
            numerical_count(df_imp, col)

def categorical_count(df,col):
    fig, axes = plt.subplots(figsize=(12,5))
    count = df.value_counts(col)
    plt.pie(x=count, labels=count.index,autopct='%1.1f%%')
    plt.title(f"{col}", fontsize=12, y=1.05)
    st.pyplot(fig)

def numerical_count(df,col):
    fig, axes = plt.subplots(figsize=(12, 5))
    plt.hist(df[col])
    plt.ylabel('Customers')
    plt.xlabel(col)
    plt.title(f"{col}", fontsize=15, y=1.05)
    st.pyplot(fig)   


# Correlation and PPS Analysis
def cor(df):
    state = '(Please wait...)'
    st.write("---")
    st.write('**Generating PPS score and Heatmaps:** *(Please wait...)*')
    st.write("---")

    def heatmap_corr(df, threshold, figsize=(20, 12), font_annot=8):
        if len(df.columns) > 1:
            mask = np.zeros_like(df, dtype=np.bool)
            mask[np.triu_indices_from(mask)] = True
            mask[abs(df) < threshold] = True

            fig, axes = plt.subplots(figsize=figsize)
            sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                        mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                        linewidth=0.5
                        )
            axes.set_yticklabels(df.columns, rotation=0)
            plt.ylim(len(df.columns), 0)
            st.pyplot(fig)


    def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
        if len(df.columns) > 1:
            mask = np.zeros_like(df, dtype=np.bool)
            mask[abs(df) < threshold] = True
            fig, ax = plt.subplots(figsize=figsize)
            ax = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                            mask=mask, cmap='rocket_r', annot_kws={"size": font_annot},
                            linewidth=0.05, linecolor='grey')
            plt.ylim(len(df.columns), 0)
            st.pyplot(fig)


    def CalculateCorrAndPPS(df):
        df_corr_spearman = df.corr(method="spearman")
        df_corr_pearson = df.corr(method="pearson")

        pps_matrix_raw = pps.matrix(df)
        pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

        pps_score_stats = pps_matrix_raw.query("ppscore < 1").filter(['ppscore']).describe().T
        st.write("PPS Score: \n")
        st.write(pps_score_stats.round(3))

        return df_corr_pearson, df_corr_spearman, pps_matrix


    def DisplayCorrAndPPS(df_corr_pearson, df_corr_spearman, pps_matrix, CorrThreshold, PPS_Threshold,
                        figsize=(20, 12), font_annot=8):

        st.write("\n")
        st.write("* Analyse how the target variable is correlated with other variables (features and target)")
        st.write("* Analyse multi-colinearity, that is, how the features are correlated among themselves")

        st.write("\n")
        st.write("*** Heatmap: Spearman Correlation (monotonic relationship) ***")
        heatmap_corr(df=df_corr_spearman, threshold=CorrThreshold, figsize=figsize, font_annot=font_annot)

        st.write("\n")
        st.write("*** Heatmap: Pearson Correlation (linear relationship between two continuous variables) ***")
        heatmap_corr(df=df_corr_pearson, threshold=CorrThreshold, figsize=figsize, font_annot=font_annot)

        st.write("\n")
        st.write("*** Heatmap: Power Predictive Score (PPS) ***")
        st.write("Linear or non-linear relationships between two columns")
        st.write("The score ranges from 0 (no predictive power) to 1 (perfect predictive power)")
        heatmap_pps(df=pps_matrix, threshold=PPS_Threshold, figsize=figsize, font_annot=font_annot)

    df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)

    DisplayCorrAndPPS(df_corr_pearson = df_corr_pearson,
                    df_corr_spearman = df_corr_spearman, 
                    pps_matrix = pps_matrix,
                    CorrThreshold = 0.3, PPS_Threshold =0.01,
                    figsize=(12,10), font_annot=10)


