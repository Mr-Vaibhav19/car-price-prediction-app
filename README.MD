# 🚗 Car Price Prediction App

A **Machine Learning web app** built with **Streamlit** that predicts the selling price of cars based on their features.  
This is my B.Tech Final Year Project showcasing **ML model training, deployment, and interactive UI**.

---

## ✨ Features
- Predicts car price using **Random Forest Regressor**
- Accuracy: **84.6% R² Score**
- User-friendly interface built with **Streamlit**
- Takes 11 car attributes as input (brand, year, km driven, fuel, transmission, etc.)
- Displays price in **₹ (INR)** and **Lakhs**
- Shows **feature importance chart**

---

## 📂 Project Structure
car-price-prediction-app/
│── app.py # Streamlit app
│── make_model.py # Script to train model
│── requirements.txt # Dependencies
│── project_documentation.md # Detailed guide
│── .gitignore # Git ignore rules
│── README.md # This file

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Mr-Vaibhav19/car-price-prediction-app.git
cd car-price-prediction-app
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the app
bash
Copy
Edit
streamlit run app.py
➡️ Open in browser: http://localhost:8501

🎯 Usage
Enter details like Brand, Year, Km Driven, Fuel, Transmission, Engine, Power, etc.

Click Predict Price

Get the estimated resale value instantly

View car summary + feature importance chart

📊 Model Info
Algorithm: Random Forest Regressor

Dataset: 1000+ car records

Accuracy: 84.6% (R² Score)

Features: 11 (encoded + numerical)

📈 Example Predictions
Car Details	Predicted Price
Maruti Swift 2020, 50k km, Petrol, Manual	₹4.2 Lakhs
Honda City 2018, 30k km, Diesel, Automatic	₹8.5 Lakhs
BMW 3 Series 2019, 40k km, Petrol, Automatic	₹25.8 Lakhs

🚀 Deployment
This app can be deployed on:

Streamlit Cloud ✅ easiest

Heroku

Render / Railway / AWS

🔮 Future Enhancements
Location-based pricing

Historical price trend analysis

Deep learning models

Car image recognition

👤 Author
Vaibhav
🔗 GitHub: Mr-Vaibhav19

💡 Built with ❤️ using Python, Streamlit, and Machine Learning.
