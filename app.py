import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('rf_model.pkl', 'rb'))

st.title("Dynamic Pricing Prediction System")

price = st.number_input("Enter Price (UnitPrice)")
month = st.slider("Month", 1, 12)
day = st.slider("Day", 1, 31)
hour = st.slider("Hour", 0, 23)

if st.button("Predict Demand"):
    input_data = np.array([[price, month, day, hour]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Demand: {int(prediction[0])}")
