import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Car Recommender", page_icon="🚗")

st.title("🤖 Smart Car Recommendation System")

# Load dataset
data = pd.read_csv("car_data.csv")

# Remove bikes strongly
bike_keywords = [
    "Royal", "Pulsar", "Hero", "Bajaj", "KTM",
    "Activa", "Shine", "FZ", "R15", "Access",
    "Dio", "Gixxer", "TVS", "Scooty", "Apache"
]

for word in bike_keywords:
    data = data[~data["Car_Name"].str.contains(word, case=False)]

st.write("### Select your preferences")

# ✅ Budget 10 lakh → 4 crore (400 lakh)
budget = st.slider(
    "Budget (in lakhs)",
    min_value=10.0,
    max_value=400.0,
    value=50.0,
    step=5.0
)

st.write(f"💰 Selected Budget: ₹ {budget/100:.2f} crore")

fuel = st.selectbox(
    "Fuel Type",
    ["Any", "Petrol", "Diesel", "CNG"]
)

trans = st.selectbox(
    "Transmission",
    ["Any", "Manual", "Automatic"]
)

# Apply filters
filtered = data[data["Selling_Price"] <= budget]

if fuel != "Any":
    filtered = filtered[filtered["Fuel_Type"] == fuel]

if trans != "Any":
    filtered = filtered[filtered["Transmission"] == trans]

# Sort best cars
filtered = filtered.sort_values(
    by=["Year", "Selling_Price"],
    ascending=[False, True]
)

# Show results
st.subheader(f"🔥 Found {len(filtered)} matching cars")

if filtered.empty:
    st.warning("❌ No cars found. Try increasing budget.")
else:

    # Limit to top 10 (app fast rahe)
    for _, row in filtered.head(10).iterrows():

        car_name = row["Car_Name"]

        # Auto car image
        image_url = f"https://source.unsplash.com/600x300/?{car_name},car"

        st.image(image_url)

        st.markdown(f"""
        ### 🚗 {car_name}

        • Year: {row['Year']}  
        • Price: ₹ {row['Selling_Price']} lakh  
        • Fuel: {row['Fuel_Type']}  
        • Transmission: {row['Transmission']}

        ---
        """)
