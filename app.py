from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

# Load the trained model
model = pickle.load(open('best_model.pkl', 'rb'))

# Load the column names used during training
with open('columns.pkl', 'rb') as f:
    columns = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form

    # Extract form inputs
    data_dict = {
        'vehicle_age': int(form_data['vehicle_age']),
        'km_driven': int(form_data['km_driven']),
        'mileage': float(form_data['mileage']),
        'engine': int(form_data['engine']),
        'max_power': float(form_data['max_power']),
        'seats': int(form_data['seats']),
        'seller_type': form_data['seller_type'],
        'fuel_type': form_data['fuel_type'],
        'transmission_type': form_data['transmission_type']
    }

    # Convert to DataFrame
    df = pd.DataFrame([data_dict])

    # One-hot encode with correct column structure
    df_encoded = pd.get_dummies(df)
    df_encoded = df_encoded.reindex(columns=columns, fill_value=0)

    # Predict using the model
    predicted_price = model.predict(df_encoded)[0]

    return render_template('index.html', prediction_text=f'Predicted Selling Price: ₹{round(predicted_price, 2)}')

if __name__ == '__main__':
    app.run(debug=True)
