import streamlit as st
import requests

# URL LocalTunnel yang didapatkan dari langkah sebelumnya
LOCAL_TUNNEL_URL = "https://quick-views-smash.loca.lt"  # Ganti dengan URL yang diberikan oleh LocalTunnel

st.title("Monitoring System")

# Buat permintaan ke backend Flask untuk mendapatkan data sensor
response = requests.get(f"{LOCAL_TUNNEL_URL}/sensor_data")
sensor_data = response.json()

with st.expander("Sensor Data"):
    st.write(f"Sensor 1: {sensor_data['sensor1']}")
    st.write(f"Sensor 2: {sensor_data['sensor2']}")
    st.write(f"Sensor 3: {sensor_data['sensor3']}")
    st.write(f"Sensor 4: {sensor_data['sensor4']}")
