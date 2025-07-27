# AutoValuator - Smart Car Price Estimator

A modern, responsive web application that predicts car prices using machine learning. Built with Flask, featuring a beautiful glassmorphic UI with Tailwind CSS.

## 🚀 Features

- **Modern UI**: Glassmorphic design with smooth animations
- **Responsive**: Works perfectly on desktop and mobile devices
- **Real-time Validation**: Form validation with helpful tooltips
- **AJAX Integration**: Smooth predictions without page reload
- **Professional Design**: Beautiful gradients and modern typography
- **User-Friendly**: Intuitive interface with floating labels

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Machine Learning**: Scikit-learn
- **Icons**: Font Awesome
- **Deployment**: Gunicorn

## 📋 Prerequisites

- Python 3.9+
- pip (Python package installer)

## 🚀 Quick Start

### Local Development

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd car-price-prediction-model
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

### Deployment

#### Option 1: Render.com

1. **Create a new Web Service** on Render
2. **Connect your GitHub repository**
3. **Configure the service**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3.9

#### Option 2: Railway.app

1. **Create a new project** on Railway
2. **Connect your GitHub repository**
3. **Deploy automatically** - Railway will detect the Python app

#### Option 3: Heroku

1. **Install Heroku CLI**
2. **Login to Heroku**

   ```bash
   heroku login
   ```

3. **Create a new Heroku app**

   ```bash
   heroku create your-app-name
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

## 📁 Project Structure

```
car-price-prediction-model/
├── app.py                 # Flask application
├── best_model.pkl        # Trained ML model
├── columns.pkl           # Feature columns
├── requirements.txt      # Python dependencies
├── Procfile             # Deployment configuration
├── runtime.txt          # Python version
├── README.md            # Project documentation
├── templates/
│   └── index.html       # Main HTML template
└── data/
    └── Cardekho Dataset (3).xlsx  # Training dataset
```

## 🎨 UI Features

- **Glassmorphic Design**: Modern glass-like card effect
- **Gradient Background**: Beautiful purple-blue gradient
- **Floating Labels**: Animated form labels
- **Tooltips**: Helpful information on hover
- **Responsive Grid**: Adapts to different screen sizes
- **Smooth Animations**: CSS transitions and keyframes
- **Loading States**: Spinner during prediction
- **Error Handling**: User-friendly error messages

## 🔧 Configuration

### Environment Variables

No environment variables are required for basic functionality.

### Model Files

Ensure these files are present in the root directory:

- `best_model.pkl` - Your trained machine learning model
- `columns.pkl` - Feature column names used during training

## 📊 Model Information

The application uses a machine learning model trained on the CarDekho dataset to predict car prices based on:

- Vehicle Age
- Kilometers Driven
- Mileage (kmpl)
- Engine (CC)
- Max Power (bhp)
- Number of Seats
- Seller Type
- Fuel Type
- Transmission Type

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- CarDekho for the dataset
- Flask community for the excellent framework
- Tailwind CSS for the beautiful styling utilities
- Font Awesome for the icons

---

⭐ If you found this project helpful, please give it a star!
