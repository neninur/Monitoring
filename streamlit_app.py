import streamlit as st
import requests
import time

# Pengaturan tampilan
st.set_page_config(layout="wide")

# Judul Aplikasi
st.title("Data Monitoring")

# Placeholder untuk update konten
placeholder = st.empty()

# URL backend Flask (gunakan alamat IP publik atau domain)
backend_url = "http://103.20.185.106:5000/random"

# Loop untuk update data secara dinamis
while True:
    response = requests.get(backend_url)
    data = response.json()["data"]
    
    # Update konten dalam placeholder
    with placeholder.container():
        st.text_area("Data Receive", value=str(data), height=100, disabled=True, key="data_receive")
    
    time.sleep(1)  # Interval update dalam detik
