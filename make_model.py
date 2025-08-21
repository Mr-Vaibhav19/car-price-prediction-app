import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Create a sample dataset
np.random.seed(42)
n_samples = 500

brands = ['Maruti', 'Hyundai', 'Honda', 'Toyota', 'BMW', 'Audi', 'Ford', 'Volkswagen', 'Nissan', 'Kia']
fuel_types = ['Petrol', 'Diesel', 'CNG', 'Electric']
seller_types = ['Individual', 'Dealer', 'Trustmark Dealer']
transmissions = ['Manual', 'Automatic']

data = pd.DataFrame({
    'name': np.random.choice(brands, n_samples),
    'year': np.random.randint(2005, 2024, n_samples),
    'km_driven': np.random.randint(5000, 200000, n_samples),
    'fuel': np.random.choice(fuel_types, n_samples),
    'seller_type': np.random.choice(seller_types, n_samples),
    'transmission': np.random.choice(transmissions, n_samples),
    'owner': np.random.randint(0, 5, n_samples),
    'mileage': np.random.uniform(10, 25, n_samples),
    'engine': np.random.randint(800, 3000, n_samples),
    'max_power': np.random.uniform(40, 200, n_samples),
    'seats': np.random.choice([4, 5, 7, 8], n_samples),
    'selling_price': np.random.uniform(200000, 2000000, n_samples)
})

# Encode categorical variables
le_name = LabelEncoder()
le_fuel = LabelEncoder()
le_seller = LabelEncoder()
le_transmission = LabelEncoder()

data['name_encoded'] = le_name.fit_transform(data['name'])
data['fuel_encoded'] = le_fuel.fit_transform(data['fuel'])
data['seller_type_encoded'] = le_seller.fit_transform(data['seller_type'])
data['transmission_encoded'] = le_transmission.fit_transform(data['transmission'])

# Features & Target
features = ['year', 'km_driven', 'name_encoded', 'fuel_encoded',
            'seller_type_encoded', 'transmission_encoded', 'owner',
            'mileage', 'engine', 'max_power', 'seats']
X = data[features]
y = data['selling_price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders into pickle file
model_data = {
    "model": model,
    "le_name": le_name,
    "le_fuel": le_fuel,
    "le_seller": le_seller,
    "le_transmission": le_transmission
}

with open("car_price_model.pkl", "wb") as f:
    pickle.dump(model_data, f)

print("✅ Model file 'car_price_model.pkl' created successfully!")
