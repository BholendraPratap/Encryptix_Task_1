import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier  # Example model; replace with your model
import pickle

# Load your trained model (assuming it's saved as 'fraud_model.pkl')
model = pickle.load(open('fraud_model.pkl', 'rb'))

# Function to make predictions
def predict_fraud(data):
    # Preprocessing data (adjust based on your model's requirements)
    # Example: Transforming the input into a format suitable for prediction
    input_data = np.array(data).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction[0]

# Web app UI
st.title("Credit Card Fraud Detection")

# Collect user input
st.header("Enter transaction details")

# Collect input features (Example inputs, modify based on your dataset)
amt = st.number_input("Transaction Amount", min_value=0.0)
trans_hour = st.number_input("Transaction Hour", min_value=0, max_value=23)
trans_year = st.number_input("Transaction Year", min_value=2020, max_value=2025)
category = st.selectbox("Transaction Category", ["Groceries", "Electronics", "Clothing", "Others"])
trans_month = st.number_input("Transaction Month", min_value=1, max_value=12)
age = st.number_input("Age of Cardholder", min_value=18, max_value=100)
city_pop = st.number_input("City Population", min_value=1000, max_value=1000000)
trans_day = st.number_input("Transaction Day", min_value=1, max_value=31)

# Combine all inputs into a list (to be used for prediction)
input_data = [amt, trans_hour, trans_year, category, trans_month, age, city_pop, trans_day]

# Button to trigger prediction
if st.button("Predict Fraud"):
    # Get the prediction
    prediction = predict_fraud(input_data)

    # Display the result
    if prediction == 1:
        st.error("This transaction is predicted as Fraud!")
    else:
        st.success("This transaction is predicted as Non-Fraud.")
