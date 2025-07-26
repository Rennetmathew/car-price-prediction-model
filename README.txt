# 🚗 CarDekho Car Price Prediction

## 📝 Introduction
This project aims to predict the **selling price of used cars** using historical data. The model helps understand how factors like year of purchase, car age, fuel type, transmission, and ownership affect the resale value of a vehicle.

---

## 📊 Dataset Used
- **Source**: CarDekho dataset (typically sourced from Kaggle or GUVI platform)
- **Features**:
  - `Car_Name`: Brand/model of the car
  - `Year`: Year of purchase
  - `Selling_Price`: Target variable – price of the car (in lakhs)
  - `Present_Price`: Price of the car when bought
  - `Kms_Driven`: Distance the car has been driven
  - `Fuel_Type`: Type of fuel (Petrol/Diesel/CNG)
  - `Seller_Type`: Dealer or Individual
  - `Transmission`: Manual/Automatic
  - `Owner`: Number of previous owners
- **Preprocessing Techniques**:
  - Removed unnecessary columns (e.g., `Car_Name`)
  - Created `Car_Age = 2023 - Year` and dropped `Year`
  - Label encoding for categorical variables (`Fuel_Type`, `Seller_Type`, `Transmission`)
  - Checked and handled outliers and skewed distributions
  - Normalized features if needed

---

## 🤖 Machine Learning Model(s) Implemented
- **Primary Model**: `Random Forest Regressor`
- Other models tested (optional): Linear Regression, Decision Tree Regressor
- **Model Evaluation**:
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)

---

## ⚙️ How to Set Up and Run the Project

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-link>
   cd CarDekho-Car-Price-Prediction
2.Install Required Libraries:
   Use pip to install required Python libraries:
3.Open the Jupyter Notebook:
   jupyter notebook CarDekho_Price_Prediction_model.ipynb
4.Run All Cells:
  .Load dataset
  .Preprocess data
  .Train the model
  .Test predictions

5.Test Prediction:
  .Modify the input test values in the notebook to see predicted car prices.