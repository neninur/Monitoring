import streamlit as st
import requests

# Ganti <ZeroTier_IP> dengan IP virtual ZeroTier dari perangkat yang menjalankan Flask
backend_url = 'http://172.50.116.118:5000/data'

def fetch_data():
    response = requests.get(backend_url)
    return response.json()

data = fetch_data()
st.write('Data from Flask:', data['message'])
