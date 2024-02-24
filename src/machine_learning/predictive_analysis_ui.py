import streamlit as st

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
    else:
        exit_result = 'will not'

    display = (
        f'### There is {exit_prob.round(1)}% probability '
        f'that this prospect **{exit_result} exit**.')

    st.write(display)

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
        statement = (
            f"* We also expect that there is a {proba.round(2)}% probability that this customer "
            f"will exit withinin a period of **{tenure_levels} year**. "
        )
    else:
        statement = (
            f"* We also expect that the customer would exit between **{tenure_levels} years**, "
            f"**Kindly note that the recall and precision levels for {tenure_levels} years is not "
            f"strong.** "
        )

    st.write(statement)

