""" Predict Exit """

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page5_exit_ml_body():

    version = 'v1'
    # All saved files(Train and Test Datasets, Feature Importance Plots, Pipelines)
    exit_preprocessing = load_pkl_file(
        f'outputs/ml_pipeline/predict_exit/{version}/clf_pipeline_preprocessed.pkl')
    exit_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_exit/{version}/clf_pipeline_model.pkl")
    exit_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_exit/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_exit/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_exit/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_exit/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_exit/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Customer Exit")
    # display pipeline summary
    st.info(
        f"The pipeline was aimed at producing at least **0.70 Recall on the 'Will Exit' class**, "
        f"as we are interested in identifying customers who would exit. Also, "
        f"the pipeline was expected to deliver **0.70 Precision on the 'No Exit' class**. \n\n"
        f"* The pipeline's **Recall performance** on the 'Will Exit' class for the "
        f"**train and test set is 0.83 and 0.71**, respectively. \n\n"
        f"* The pipeline's **Precision performance** on the 'No Exit' class for the "
        f"**train and test set is 0.80 and 0.89**, respectively. \n\n "
    )
    st.warning(
        f"The model was not refitted using the important features identified as the **Recall performance "
        f"was 0.69** post-refitting which **didn't meet the business requirement of 0.70**."
    )

    # display pipelines
    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")
    st.write("\n\n")

    st.write(" * The first is responsible for data cleaning and feature engineering.")
    st.write(exit_preprocessing)

    st.write("* The second is for feature scaling and modelling.")
    st.write(exit_model)

    # displayfeature importance plot
    st.write("---")
    st.write("#### The important features identified")
    st.write("\n\n")
    st.write("1. Age \n\n" 
             "2. IsActiveMember \n\n "
             "3. HasCrCard "
    )
    st.image(exit_feat_importance)
    st.write("\n\n")
    st.write("Note : The model was not refitted using these features as the performance was slighlty low.")

    # display performance on train and test set
    st.write("---")
    st.write("## Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=exit_model,
                    label_map=["No-Exit", "Will-Exit"])