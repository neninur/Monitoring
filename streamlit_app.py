import streamlit as st
import random
import time

# Pengaturan tampilan
st.set_page_config(layout="wide")

# Judul Aplikasi
st.title("Monitoring")
st.subheader("Data Receive")

# Fungsi untuk menghasilkan data random
def generate_random_data():
    return random.randint(1, 10)

# Placeholder untuk update konten
placeholder = st.empty()

# Loop untuk update data secara dinamis
iteration = 0
while True:
    data = generate_random_data()
    unique_key = f"data_receive_{iteration}"  # Membuat kunci unik berdasarkan iterasi
    
    # Update konten dalam placeholder
    with placeholder.container():
        
        st.text_area("Data Receive", value=str(data), height=100, disabled=True, key=unique_key)
       
    
    iteration += 1
    time.sleep(1)  # Interval update dalam detik
