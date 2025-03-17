import pandas as pd
import numpy as np
import joblib
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the saved model
model = joblib.load("XGBoost_best_model.pkl")

# Streamlit UI
st.title("Wind Turbine Power Prediction")
st.write("This app predicts the active power based on wind parameters.")

# Load dataset for statistics & visualization
data = pd.read_csv("T1.csv", delimiter=',')
data.columns = ['DateTime', 'LV_ActivePower', 'Wind_Speed', 'Theoretical_Power_Curve', 'Wind_Direction']
data['DateTime'] = pd.to_datetime(data['DateTime'], format='%d %m %Y %H:%M')
data['Hour'] = data['DateTime'].dt.hour
data['Day'] = data['DateTime'].dt.day
data['Month'] = data['DateTime'].dt.month

# Sidebar inputs
st.sidebar.header("User Input Features")
wind_speed = st.sidebar.slider("Wind Speed (m/s)", float(data['Wind_Speed'].min()), float(data['Wind_Speed'].max()), float(data['Wind_Speed'].mean()))
theoretical_power = st.sidebar.slider("Theoretical Power Curve (KWh)", float(data['Theoretical_Power_Curve'].min()), float(data['Theoretical_Power_Curve'].max()), float(data['Theoretical_Power_Curve'].mean()))
wind_direction = st.sidebar.slider("Wind Direction (°)", float(data['Wind_Direction'].min()), float(data['Wind_Direction'].max()), float(data['Wind_Direction'].mean()))
hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
day = st.sidebar.slider("Day of Month", 1, 31, 15)
month = st.sidebar.slider("Month", 1, 12, 6)

# Predict button
if st.sidebar.button("Predict Active Power"):
    input_data = np.array([[wind_speed, theoretical_power, wind_direction, hour, day, month]])
    prediction = model.predict(input_data)[0]
    st.write(f"### Predicted Active Power: {prediction:.2f} kW")

# Data Statistics & Visualizations
st.subheader("Data Statistics")
st.write(data.describe())

st.subheader("Visualizations")
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Histogram of Wind Speed
sns.histplot(data['Wind_Speed'], bins=30, kde=True, ax=ax[0])
ax[0].set_title("Wind Speed Distribution")
ax[0].set_xlabel("Wind Speed (m/s)")
ax[0].set_ylabel("Frequency")

# Scatter plot of Wind Speed vs. Active Power
sns.scatterplot(x=data['Wind_Speed'], y=data['LV_ActivePower'], alpha=0.5, ax=ax[1])
ax[1].set_title("Wind Speed vs Active Power")
ax[1].set_xlabel("Wind Speed (m/s)")
ax[1].set_ylabel("Active Power (kW)")

st.pyplot(fig)
