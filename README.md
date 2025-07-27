# 🚗 AutoValuator - Smart Car Price Estimator

A modern, professional car price prediction web application built with Flask and machine learning. Features a beautiful glassmorphic UI design with real-time AJAX predictions.

![AutoValuator Screenshot](https://via.placeholder.com/800x400/667eea/ffffff?text=AutoValuator+-+Smart+Car+Price+Estimator)

## ✨ Features

- **Modern UI Design**: Glassmorphic design with gradient backgrounds and smooth animations
- **Real-time Predictions**: AJAX-powered predictions without page reload
- **Responsive Layout**: Mobile-first design that works on all devices
- **Input Validation**: Client-side and server-side validation with helpful tooltips
- **Professional UX**: Floating labels, loading states, and error handling
- **Machine Learning**: Powered by trained ML models for accurate price predictions

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **Machine Learning**: scikit-learn, pandas, numpy
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd car-price-prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

### 🌐 Deployment

#### Deploy to Render.com

1. **Create a new Web Service** on [Render.com](https://render.com)
2. **Connect your GitHub repository**
3. **Configure the service**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: `Python 3`

#### Deploy to Railway.app

1. **Visit** [Railway.app](https://railway.app)
2. **Deploy from GitHub** by connecting your repository
3. **Railway will automatically detect** the Python app and deploy it

#### Deploy to Heroku

1. **Install Heroku CLI** and login
2. **Create a new Heroku app**:
   ```bash
   heroku create your-app-name
   ```
3. **Deploy**:
   ```bash
   git push heroku main
   ```

## 📋 API Endpoints

### GET /
Returns the main HTML page with the prediction form.

### POST /predict
Accepts car details and returns price prediction.

**Request Body** (JSON):
```json
{
  "vehicle_age": 5,
  "km_driven": 50000,
  "mileage": 15.5,
  "engine": 1500,
  "max_power": 120.5,
  "seats": 5,
  "seller_type": "Individual",
  "fuel_type": "Petrol",
  "transmission_type": "Manual"
}
```

**Response** (JSON):
```json
{
  "success": true,
  "predicted_price": "₹8,50,000.00",
  "raw_price": 850000.0
}
```

## 🎨 UI Features

- **Glassmorphic Design**: Semi-transparent cards with backdrop blur
- **Floating Labels**: Smooth label animations on focus
- **Tooltips**: Helpful hints for each input field
- **Loading States**: Visual feedback during prediction
- **Error Handling**: User-friendly error messages
- **Responsive Grid**: Adapts to different screen sizes
- **Smooth Animations**: CSS animations for better UX

## 📱 Mobile Responsiveness

The application is fully responsive and optimized for:
- 📱 Mobile phones (320px+)
- 📱 Tablets (768px+)
- 💻 Desktops (1024px+)
- 🖥️ Large screens (1200px+)

## 🔧 Customization

### Styling
- Modify the gradient background in the `gradient-bg` class
- Adjust glassmorphism opacity in the `.glassmorphism` class
- Change colors using Tailwind CSS classes

### Model
- Replace `best_model.pkl` with your trained model
- Update `columns.pkl` with your feature columns
- Modify validation ranges in both frontend and backend

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Built with ❤️ by AI Assistant | Powered by ML & Flask

---

### 🎯 Future Enhancements

- [ ] Dark/Light theme toggle
- [ ] Price history charts
- [ ] Car image upload and analysis
- [ ] Comparison with similar cars
- [ ] Export prediction results
- [ ] User accounts and saved searches