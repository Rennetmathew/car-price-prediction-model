from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd
import os

# Load the trained model
try:
    # Try to load the best_model.pkl first
    if os.path.exists('best_model.pkl'):
        model = pickle.load(open('best_model.pkl', 'rb'))
    else:
        # Fallback to other available models
        model = pickle.load(open('RandomForestRegressor_model.pkl', 'rb'))
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Load the column names used during training
try:
    with open('columns.pkl', 'rb') as f:
        columns = pickle.load(f)
except Exception as e:
    print(f"Error loading columns: {e}")
    columns = None

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if request is JSON (AJAX) or form data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        # Extract and validate inputs
        data_dict = {
            'vehicle_age': int(data['vehicle_age']),
            'km_driven': int(data['km_driven']),
            'mileage': float(data['mileage']),
            'engine': int(data['engine']),
            'max_power': float(data['max_power']),
            'seats': int(data['seats']),
            'seller_type': data['seller_type'],
            'fuel_type': data['fuel_type'],
            'transmission_type': data['transmission_type']
        }

        # Basic validation
        if data_dict['vehicle_age'] < 0 or data_dict['km_driven'] < 0:
            raise ValueError("Age and KM driven cannot be negative")
        
        if data_dict['mileage'] <= 0 or data_dict['max_power'] <= 0:
            raise ValueError("Mileage and Max Power must be positive")
        
        if data_dict['seats'] < 1:
            raise ValueError("Seats must be at least 1")

        # Convert to DataFrame
        df = pd.DataFrame([data_dict])

        # One-hot encode with correct column structure
        df_encoded = pd.get_dummies(df)
        df_encoded = df_encoded.reindex(columns=columns, fill_value=0)

        # Predict using the model
        predicted_price = model.predict(df_encoded)[0]
        
        # Format the price
        formatted_price = f"₹{predicted_price:,.2f}"

        # Return JSON response for AJAX requests
        if request.is_json:
            return jsonify({
                'success': True,
                'predicted_price': formatted_price,
                'raw_price': float(predicted_price)
            })
        else:
            # Fallback for non-AJAX requests
            return render_template('index.html', prediction_text=f'Predicted Selling Price: {formatted_price}')

    except ValueError as ve:
        error_msg = str(ve)
        if request.is_json:
            return jsonify({'success': False, 'error': error_msg}), 400
        else:
            return render_template('index.html', error_message=error_msg)
    
    except Exception as e:
        error_msg = "An error occurred while processing your request. Please try again."
        if request.is_json:
            return jsonify({'success': False, 'error': error_msg}), 500
        else:
            return render_template('index.html', error_message=error_msg)

if __name__ == '__main__':
    import sys
    print(f"Python version: {sys.version}")
    print("Starting AutoValuator - Car Price Prediction App...")
    print("Open your browser and go to http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
