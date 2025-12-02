import streamlit as st
import numpy as np
import pickle
import datetime

# -----------------------------
# Load Model & Encoders
# -----------------------------
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="wide")

st.markdown("""
    <h1 style='text-align:center; color:#2E86C1;'>🚗 Car Price Prediction System</h1>
    <p style='text-align:center;'>Enter the car details below to estimate the selling price.</p>
""", unsafe_allow_html=True)

# Load model
try:
    model = pickle.load(open("car_price.pkl", "rb"))
except:
    st.error("❌ Error: Model file 'car_price.pkl' not found!")
    st.stop()

# -----------------------------
# Layout: Two Columns
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    car_name = st.text_input("🔤 Car Name", placeholder="Ex: Swift, Creta, Alto")

    year = st.number_input(
        "📅 Year of Purchase",
        min_value=1990,
        max_value=datetime.datetime.now().year,
        step=1
    )

    present_price = st.number_input(
        "💰 Present Price (in Lakhs)", 
        min_value=0.0, 
        format="%.2f"
    )

    kms_driven = st.number_input(
        "📍 Kilometers Driven", 
        min_value=0, 
        step=100
    )

with col2:
    fuel_type = st.selectbox(
        "⛽ Fuel Type",
        ["Petrol", "Diesel", "CNG"]
    )

    seller_type = st.selectbox(
        "🧑‍💼 Seller Type",
        ["Dealer", "Individual"]
    )

    transmission = st.selectbox(
        "⚙️ Transmission",
        ["Manual", "Automatic"]
    )

    owner = st.selectbox(
        "👤 Number of Previous Owners",
        [0, 1, 2, 3]
    )

# Auto compute Car Age
current_year = datetime.datetime.now().year
car_age = current_year - year

# Encoding
fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 0, "Automatic": 1}

# -----------------------------
# Predict Button
# -----------------------------
st.markdown("---")

if st.button("🔍 Predict Selling Price", use_container_width=True):
    
    # Prepare input data
    input_data = np.array([[
        year,
        present_price,
        kms_driven,
        fuel_map[fuel_type],
        seller_map[seller_type],
        trans_map[transmission],
        owner,
        car_age
    ]])

    # Predict
    prediction = model.predict(input_data)

    # Fix any ndarray formatting issues
    try:
        predicted_price = float(prediction[0])
    except:
        predicted_price = float(prediction[0][0])
    
    # Display Result
    st.success(f"### 💵 Estimated Selling Price: **₹ {predicted_price:.2f} Lakhs**")
    
    st.info("""
        ✔ Prediction is based on trained Machine Learning & ANN models.  
        ✔ Actual selling price may vary depending on condition, location & market demand.
    """)

# Footer
st.markdown("""
    <br><hr>
    <p style='text-align:center; font-size:14px; color:grey;'>
    🔧 Developed by Vikash Singh
    </p>
""", unsafe_allow_html=True)
