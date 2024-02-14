import streamlit as st
from app_pages.multipage import MultiPage

# load pages 
from app_pages.page1_summary import page1_summary_body
from app_pages.page2_customer_exit_study import page2_customer_exit_study_body
from app_pages.page3_hypothesis import page3_hypothesis_body
from app_pages.page4_predict import page4_predict_body
from app_pages.page5_exit_ml import page5_exit_ml_body
from app_pages.page6_tenure_ml import page6_tenure_ml_body

# Create an instance of the app
app = MultiPage(app_name= "Bank Customer Exit Predictor")  

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page1_summary_body)
app.add_page("Customer Exit Study", page2_customer_exit_study_body)
app.add_page("Project Hypothesis and Validation", page3_hypothesis_body)
app.add_page("Exit Predictor", page4_predict_body)
app.add_page("ML: Customer Exit", page5_exit_ml_body)
app.add_page("ML: Customer Tenure", page6_tenure_ml_body)

# Run the  app
app.run() 