import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
import matplotlib.pyplot as plt

# ✅ Page config must be first Streamlit command
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="wide")

# -----------------------------
# Load the trained model safely
# -----------------------------
@st.cache_data
def load_model():
    with open('car_price_model.pkl', 'rb') as f:
        model_data = pickle.load(f)
    return model_data

model_data = load_model()
model = model_data['model']
le_name = model_data['le_name']
le_fuel = model_data['le_fuel']
le_seller = model_data['le_seller']
le_transmission = model_data['le_transmission']

# Safe transform function to avoid errors on unseen categories
def safe_transform(le, value):
    if value in le.classes_:
        return le.transform([value])[0]
    else:
        return -1  # Unknown category placeholder

# -----------------------------
# Layout
# -----------------------------
st.title("🚗 Car Price Prediction App")
st.markdown("### Predict the selling price of your car using Machine Learning")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("Enter Car Details")

    # Dynamic Car Brands
    car_brands = sorted(list(le_name.classes_))
    selected_brand = st.selectbox("🏷️ Car Brand", car_brands)

    # Year
    current_year = datetime.now().year
    year = st.selectbox("📅 Year of Purchase", list(range(2005, current_year + 1))[::-1])

    # Kilometers Driven
    km_driven = st.number_input("🛣️ Kilometers Driven", min_value=0, max_value=500000, value=50000, step=1000)

    # Fuel Type
    fuel_types = sorted(list(le_fuel.classes_))
    fuel_type = st.selectbox("⛽ Fuel Type", fuel_types)

    # Seller Type
    seller_types = sorted(list(le_seller.classes_))
    seller_type = st.selectbox("👤 Seller Type", seller_types)

    # Transmission
    transmissions = sorted(list(le_transmission.classes_))
    transmission = st.selectbox("⚙️ Transmission", transmissions)

    # Number of Owners
    owner = st.selectbox("👥 Number of Previous Owners", [0, 1, 2, 3, 4])

    # Mileage
    mileage = st.number_input("📊 Mileage (km/l)", min_value=5.0, max_value=40.0, value=15.0, step=0.1)

    # Engine Capacity
    engine = st.number_input("🔧 Engine Capacity (cc)", min_value=500, max_value=5000, value=1500, step=50)

    # Max Power
    max_power = st.number_input("⚡ Max Power (bhp)", min_value=30.0, max_value=500.0, value=100.0, step=1.0)

    # Seats
    seats = st.selectbox("💺 Number of Seats", [4, 5, 7, 8])

with col2:
    st.header("Prediction")

    if st.button("🔮 Predict Price", type="primary", use_container_width=True):
        try:
            input_data = pd.DataFrame({
                'year': [year],
                'km_driven': [km_driven],
                'name_encoded': [safe_transform(le_name, selected_brand)],
                'fuel_encoded': [safe_transform(le_fuel, fuel_type)],
                'seller_type_encoded': [safe_transform(le_seller, seller_type)],
                'transmission_encoded': [safe_transform(le_transmission, transmission)],
                'owner': [owner],
                'mileage': [mileage],
                'engine': [engine],
                'max_power': [max_power],
                'seats': [seats]
            })

            predicted_price = model.predict(input_data)[0]

            st.subheader("💰 Predicted Price")
            st.metric(label="Estimated Price", value=f"₹ {predicted_price:,.0f}")

            price_in_lakhs = predicted_price / 100000
            st.info(f"💵 **Price in Lakhs:** ₹ {price_in_lakhs:.2f} Lakhs")

            st.markdown("---")
            st.markdown("### 📋 Car Summary")
            st.write(f"**Brand:** {selected_brand}")
            st.write(f"**Year:** {year}")
            st.write(f"**Fuel Type:** {fuel_type}")
            st.write(f"**Transmission:** {transmission}")
            st.write(f"**Kilometers Driven:** {km_driven:,} km")

        except Exception as e:
            st.error(f"⚠️ An error occurred: {str(e)}")

    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("""
    - **Lower kilometers** → higher resale value  
    - **Newer cars** usually sell for more  
    - **Automatic cars** often have higher resale value  
    - **Diesel cars** may have better resale in some markets  
    - **Premium brands** (BMW, Audi) retain value longer  
    """)

# -----------------------------
# Sidebar Information
# -----------------------------
with st.sidebar:
    st.header("📊 Model Information")
    st.write("**Algorithm:** Random Forest Regressor")
    st.write("**Training Data:** 1000+ car records")
    st.write("**Model Accuracy:** 84.6% R² Score")
    st.write("**Features Used:** 11 car attributes")

    st.markdown("---")
    st.header("🎯 How it Works")
    st.write("""
    1. Enter your car details  
    2. Click 'Predict Price'  
    3. Get instant price prediction  
    4. Use the estimate for selling/buying decisions  
    """)

    st.markdown("---")
    st.header("📈 Feature Importance")
    try:
        feature_importance = model.feature_importances_
        features = ['year', 'km_driven', 'name_encoded', 'fuel_encoded', 'seller_type_encoded',
                    'transmission_encoded', 'owner', 'mileage', 'engine', 'max_power', 'seats']

        fig, ax = plt.subplots()
        ax.barh(features, feature_importance, color='skyblue')
        ax.set_xlabel("Importance Score")
        ax.set_ylabel("Features")
        ax.invert_yaxis()
        st.pyplot(fig)
    except:
        st.warning("Feature importance not available for this model.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>🚗 Car Price Prediction App | Built with Streamlit & Machine Learning</p>
        <p>Model Accuracy: 84.6% (R² Score) | Algorithm: Random Forest</p>
    </div>
    """, 
    unsafe_allow_html=True
)
