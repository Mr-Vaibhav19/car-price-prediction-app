# 🚗 Car Price Prediction App

A Machine Learning web application built with **Streamlit** that predicts the selling price of a car based on its features.  
This project was developed as a **B.Tech Final Year Project** to demonstrate ML model training, deployment, and interactive visualization.

---

## 📌 Features
- Predicts car prices using **Random Forest Regressor**  
- Input fields for 11 car attributes (brand, year, fuel, transmission, etc.)  
- Accuracy: **84.6% R² Score**  
- Interactive UI built with **Streamlit**  
- Displays results in both **₹ (INR)** and **Lakhs** format  
- Provides feature importance analysis  

---

## 🏗️ Project Structure
car-price-prediction-app/
│
├── app.py # Streamlit app for predictions
├── make_model.py # Script to train and save ML model
├── car_price_model.pkl # Trained model (ignored in gitignore if large)
├── sample_car_data.csv # Sample dataset (optional)
├── requirements.txt # Dependencies
├── project_documentation.md # Detailed project report
└── README.md # This file


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/car-price-prediction-app.git
cd car-price-prediction-app

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the App
streamlit run app.py

4️⃣ Open in Browser

Go to: http://localhost:8501

🎯 Usage

Select Car Brand, Year, Fuel Type, Transmission, etc.

Enter numerical details like Km Driven, Engine Capacity, Mileage, Max Power

Click Predict Price

View estimated selling price instantly

📊 Model Information

Algorithm: Random Forest Regressor

Training Data: 1000+ car records

Accuracy: 84.6% (R² Score)

Features Used: 11 encoded attributes

📈 Sample Predictions
Car Details	Predicted Price
Maruti Swift 2020, 50k km, Petrol, Manual	₹4.2 Lakhs
Honda City 2018, 30k km, Diesel, Automatic	₹8.5 Lakhs
BMW 3 Series 2019, 40k km, Petrol, Automatic	₹25.8 Lakhs
Toyota Innova 2017, 80k km, Diesel, Manual	₹12.3 Lakhs
🚀 Deployment

This app can be deployed on:

Streamlit Cloud (free, easiest)

Heroku

Render / Railway / AWS / Azure

📚 Future Enhancements

📉 Add historical price trend analysis

🌍 Location-based pricing

🖼️ Image recognition (car condition from photos)

🤖 Deep learning models

📝 License

This project is open-source and available under the MIT License.

💬 Contact

👤 Vaibhav
📧 [vaibhavbhutta@gmail.com
]
🔗 GitHub: Mr-Vaibhav19


