import streamlit as st
import pandas as pd
from src.data_management import load_bank_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (
    predict_exit,
    predict_tenure)


def page4_predict_body():

    # Files for predicting exit
    version = 'v1'
    exit_preprocessing = load_pkl_file(
        f'outputs/ml_pipeline/predict_exit/{version}/clf_pipeline_preprocessed.pkl')
    exit_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_exit/{version}/clf_pipeline_model.pkl")
    exit_features = (pd.read_csv(f"outputs/ml_pipeline/predict_exit/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )

    # Files for predicting tenure
    version = 'v1'
    tenure_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/clf_pipeline.pkl")
    tenure_labels_map = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/label_map.pkl")
    tenure_features = (pd.read_csv(f"outputs/ml_pipeline/predict_tenure/{version}/X_train.csv")
                       .columns
                       .to_list()
                       )

    st.write("### Exit Predictor Interface")
    st.info(
        f"* The bank is interested in determining whether or newly onboarded customer will exit. "
        f"If yes, the bank is interested in knowing if the customer will exit withinin a year."
    )
    st.write("---")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # prediction on live data
    if st.button("Run Analysis"):
        exit_prediction = predict_exit(
            X_live, exit_features, exit_preprocessing, exit_model)

        if exit_prediction == 1:
            predict_tenure(X_live, tenure_features,
                           tenure_model, tenure_labels_map)


def DrawInputsWidgets():

    # load dataset
    df = load_bank_data()

# we create input widgets only for all 9 features
    col1, col2, col3 = st.beta_columns(3)
    col4, col5, col6 = st.beta_columns(3)
    col7, col8, col9 = st.beta_columns(3)
    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "CreditScore"
        st_widget = st.number_input(
            label=feature,
            min_value=300,
            max_value=900,
            value=300
        )
    X_live[feature] = st_widget

    with col2:
        feature = "Geography"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "Gender"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "Age"
        st_widget = st.number_input(
            label=feature,
            min_value=18,
            max_value=100,
            value=18
        )
    X_live[feature] = st_widget

    with col5:
        feature = "Balance"
        st_widget = st.number_input(
            label=feature,
            min_value=0.00,
            max_value=300000.00,
            value=0.00
        )
    X_live[feature] = st_widget

    with col6:
        feature = "NumOfProducts"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col7:
        feature = "HasCrCard"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col8:
        feature = "IsActiveMember"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col9:
        feature = "EstimatedSalary"
        st_widget = st.number_input(
            label=feature,
            min_value=0.00,
            max_value=300000.00,
            value=0.00
        )
    X_live[feature] = st_widget

    return X_live