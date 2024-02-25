import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def predict_exit(X_live, exit_features, exit_preprocessing, exit_model):

    # Selecting all features from live data for exit prediction
    X_live_exit = X_live.filter(exit_features)

    # Data cleaning and feature engineering pipeline
    X_live_preprocessing = exit_preprocessing.transform(X_live_exit)

    # Predicting Exit
    exit_prediction = exit_model.predict(X_live_preprocessing)
    exit_proba = exit_model.predict_proba(X_live_preprocessing)
    
    # Calculate and display results 
    exit_prob = exit_proba[0, exit_prediction][0]*100
    if exit_prediction == 1:
        exit_result = 'will'
        pie_result = 'Will Exit'
        neg_result = 'Will Not Exit'
    else:
        exit_result = 'will not'
        pie_result = 'Will Not Exit'
        neg_result = 'Will Exit'

    display = (
        f'### There is {exit_prob.round(1)}% probability '
        f'that this prospect **{exit_result} exit**.')
    
    st.write("---")
    st.write("## Exit Prediction")
    st.write(display)
    
    # Probability Plot
    fig, axes = plt.subplots(figsize=(12, 6))
    result_value = exit_prob
    remaining_value = 100 - exit_prob 
    sizes = [result_value,remaining_value]
    labels = [pie_result,neg_result]
    axes.pie(sizes, labels=labels,explode=(0,0.1),autopct='%1.1f%%',wedgeprops={'alpha':0.5})
    plt.title('Customer Exit Probability', fontsize=15, y=1)
    st.pyplot(fig)

    return exit_prediction


def predict_tenure(X_live, tenure_features, tenure_model, tenure_labels_map):

    # from live data, subset features related to this pipeline
    X_live_tenure = X_live.filter(tenure_features)

    # prediction
    tenure_prediction = tenure_model.predict(X_live_tenure)
    tenure_prediction_proba = tenure_model.predict_proba(X_live_tenure)
  
    # display results based on prediction
    proba = tenure_prediction_proba[0, tenure_prediction][0]*100
    tenure_levels = tenure_labels_map[tenure_prediction[0]]

    if tenure_prediction == 0:
        st.write("---")
        statement = (
            f"* We also expect that there is a {proba.round(2)}% probability that this customer "
            f"will exit withinin a period of **{tenure_levels} year**. "
        )
    else:
        st.write("---")
        statement = (
            f"* We also expect that the customer would exit between **{tenure_levels} years**, "
            f"**Kindly note that the recall and precision levels for {tenure_levels} years is not "
            f"strong.** "
        )
    
    st.write("## Tenure Prediction")
    st.write(statement)




