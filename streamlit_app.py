import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('data/processed_air_quality_data.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    return data

data = load_data()

# Streamlit UI
st.title("Air Quality Index (AQI) Dashboard")

# Sidebar for city selection
cities = data['City'].unique()
selected_city = st.sidebar.selectbox("Select City", cities)

# Filter data by city and year (2016-2020)
city_data = data[(data['City'] == selected_city) & (data['Date'].dt.year >= 2016) & (data['Date'].dt.year <= 2020)]

# Display data
st.subheader(f"AQI Data for {selected_city} (2016-2020)")
st.dataframe(city_data[['Date', 'PM2.5', 'NO2', 'AQI', 'Predicted_AQI', 'AQI_Category']])

# Plot AQI over time
st.subheader("AQI Trend")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(city_data['Date'], city_data['AQI'], label='Actual AQI', color='blue')
ax.plot(city_data['Date'], city_data['Predicted_AQI'], label='Predicted AQI', color='orange')
ax.set_xlabel('Date')
ax.set_ylabel('AQI')
ax.set_title(f'AQI Trend for {selected_city}')
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)

# Display error statistics
st.subheader("Prediction Error")
mae = city_data['Error'].mean()
st.write(f"Mean Absolute Error (MAE): {mae:.2f}")

# Display AQI category distribution
st.subheader("AQI Category Distribution")
category_counts = city_data['AQI_Category'].value_counts()
st.bar_chart(category_counts)

# Load and display forecasted AQI (for Ahmedabad as an example)
if selected_city == 'Ahmedabad':
    forecast_data = pd.read_csv('data/forecasted_aqi_ahmedabad.csv')
    forecast_data['Date'] = pd.to_datetime(forecast_data['Date'])
    st.subheader("30-Day AQI Forecast for Ahmedabad")
    st.dataframe(forecast_data)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(city_data['Date'], city_data['AQI'], label='Historical AQI', color='blue')
    ax.plot(forecast_data['Date'], forecast_data['Forecasted_AQI'], label='Forecasted AQI', color='red')
    ax.set_xlabel('Date')
    ax.set_ylabel('AQI')
    ax.set_title('AQI Forecast for Ahmedabad')
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)