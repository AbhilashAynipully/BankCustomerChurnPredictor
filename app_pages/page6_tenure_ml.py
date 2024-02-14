""" Predict Tenure """

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page6_tenure_ml_body():

    # load tenure pipeline files
    version = 'v1'
    tenure_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/clf_pipeline.pkl")
    tenure_labels_map = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/label_map.pkl")
    tenure_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_tenure/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_tenure/{version}/y_test.csv")

    st.write("### ML Pipeline: Predict Tenure")
    # display pipeline summary
    st.info(
        f"* **Regression model** was chosen initially for predicting the tenure, however the"
        f"model performance was poor and **didn't meet the requirement** : "
        f"0.7 of R2 Score on train and test sets. \n"
        f"* It was decided to switch to a **Classification Model** by converting the target variable"
        f"* 'Tenure' into classes. The aim was to obtain at least 0.7 Recall on 'Upto 1' class, on train and test sets,"
        f"since the primary objective was to identify customers who are expected to quit within a year."
        f"The classifer performance was higher than 0.9 on both train and test sets.\n"
        f"*The model has decent performance in predicting exit within a year, however predictions"
        f"for the remaining classes are poor and this is the limitation of this model.")
    st.write("---")

    # display pipeline steps
    st.write("* ML pipeline to predict tenure when customer is expected to exit.")
    st.write(tenure_model)
    st.write("---")

    # display best features
    st.write("* The important features identified")
    st.write(X_train.columns.to_list())
    st.image(tenure_feat_importance)
    st.write("---")

    # display performance on train and test set
    st.write("### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=tenure_model,
                    label_map=tenure_labels_map)