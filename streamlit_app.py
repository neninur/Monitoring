import streamlit as st
import requests

# URL API backend Anda
API_URL = 'https://marinafebiyol.pythonanywhere.com/api/endpoint'

# Mengambil data dari API backend
def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

st.title('Random Data Display')

# Ambil data dan tampilkan
data = fetch_data()
if data:
    st.write("Data from backend:", data['data'])
