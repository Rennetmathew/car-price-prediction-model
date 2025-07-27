from flask import Flask, render_template, request, jsonify
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
    try:
        # Check if it's an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = request.get_json()
            
            # Extract form inputs
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
        else:
            # Handle regular form submission
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
        
        # Format the price with commas for better readability
        formatted_price = "{:,.2f}".format(predicted_price)
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({
                'success': True,
                'predicted_price': formatted_price,
                'message': f'Predicted Selling Price: ₹{formatted_price}'
            })
        else:
            return render_template('index.html', prediction_text=f'Predicted Selling Price: ₹{formatted_price}')
            
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({
                'success': False,
                'error': str(e)
            }), 400
        else:
            return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
