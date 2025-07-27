#!/bin/bash

echo "🚗 AutoValuator - Smart Car Price Estimator"
echo "==========================================="
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    echo "✓ Python 3 found"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    echo "✓ Python found"
    PYTHON_CMD="python"
else
    echo "❌ Python not found. Please install Python 3.7+."
    exit 1
fi

# Check if required packages are installed
echo "📦 Checking dependencies..."
$PYTHON_CMD -c "
try:
    import flask, pandas, numpy, sklearn, pickle
    print('✓ All required packages are installed')
except ImportError as e:
    print(f'❌ Missing package: {e}')
    print('Please install the required packages:')
    print('pip install -r requirements.txt')
    exit(1)
"

if [ $? -ne 0 ]; then
    exit 1
fi

# Check if model files exist
if [ ! -f "best_model.pkl" ] && [ ! -f "RandomForestRegressor_model.pkl" ]; then
    echo "⚠️  No model files found. Creating demo model..."
    $PYTHON_CMD -c "
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Create a demo model
model = RandomForestRegressor(n_estimators=10, random_state=42)
X_dummy = np.random.rand(100, 30)
y_dummy = np.random.rand(100) * 1000000
model.fit(X_dummy, y_dummy)

# Save model
with open('best_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save columns
columns = [
    'vehicle_age', 'km_driven', 'mileage', 'engine', 'max_power', 'seats',
    'seller_type_Dealer', 'seller_type_Individual', 'seller_type_Trustmark Dealer',
    'fuel_type_CNG', 'fuel_type_Diesel', 'fuel_type_Electric', 'fuel_type_LPG', 'fuel_type_Petrol',
    'transmission_type_Automatic', 'transmission_type_Manual'
] + [f'feature_{i}' for i in range(14)]

with open('columns.pkl', 'wb') as f:
    pickle.dump(columns, f)

print('✓ Demo model created successfully')
"
fi

echo ""
echo "🚀 Starting AutoValuator..."
echo "📱 Open your browser and visit: http://localhost:5000"
echo "⏹️  Press Ctrl+C to stop the server"
echo ""

# Start the Flask application
$PYTHON_CMD app.py