# Fuzzy Logic-Based Air Quality Prediction System

This project calculates AQI using fuzzy logic, compares it with actual values, and predicts future AQI using ARIMA. It includes a Streamlit UI for visualization.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AQ1_prediction.git

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt


## Usage

1. Place air_quality_data.csv in the data/ directory.
2. Run the Jupyter Notebook for analysis:
   ```bash
   jupyter notebook main.ipynb

3. Launch the Streamlit UI:
   ```bash
   streamlit run streamlit_app.py

## Features

Fuzzy logic AQI calculation based on PM2.5 and NO2.
Error analysis (MAE) and AQI classification.
ARIMA-based time series forecasting.
Interactive Streamlit dashboard for city-wise AQI visualization (2016-2020).