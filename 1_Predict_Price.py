import streamlit as st
import pandas as pd
import joblib

st.title("💰 Car Price Prediction")

# Load trained model
model = joblib.load("car_price_model.pkl")

# Inputs
price = st.number_input("Present Price (in lakhs)", min_value=0.0)
kms = st.number_input("Kilometers Driven", min_value=0)
owner = st.selectbox("Number of Owners", [0, 1, 2, 3])

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller = st.selectbox("Dealer or Owner", ["Dealer", "Individual"])
trans = st.selectbox("Transmission", ["Manual", "Automatic"])

car_age = st.slider("Car Age (years)", 0, 20, 5)

# Prediction
if st.button("🔮 Predict Price"):

    fuel_map = {"Petrol": 2, "Diesel": 1, "CNG": 0}
    seller_map = {"Dealer": 0, "Individual": 1}
    trans_map = {"Manual": 1, "Automatic": 0}

    input_data = pd.DataFrame({
        "Present_Price": [price],
        "Kms_Driven": [kms],
        "Fuel_Type": [fuel_map[fuel]],
        "Seller_Type": [seller_map[seller]],
        "Transmission": [trans_map[trans]],
        "Owner": [owner],
        "Car_Age": [car_age]
    })

    pred = model.predict(input_data)

    st.success(f"💰 Estimated Selling Price: ₹ {round(pred[0], 2)} lakh")
