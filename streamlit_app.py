import streamlit as st
import random
import time

# Pengaturan tampilan
st.set_page_config(layout="wide")

# Judul Aplikasi
st.title("Data Monitoring")

# Fungsi untuk menghasilkan data random
def generate_random_data():
    return random.randint(1, 10)

# Kotak dengan border biru tua dan text box
st.markdown("""
    <style>
    .border-box {
        border: 4px solid darkblue;
        padding: 10px;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Placeholder untuk update konten
placeholder = st.empty()

# Loop untuk update data secara dinamis
iteration = 0
while True:
    data = generate_random_data()
    unique_key = f"data_receive_{iteration}"  # Membuat kunci unik berdasarkan iterasi
    
    # Update konten dalam placeholder
    with placeholder.container():
        st.markdown('<div class="border-box">', unsafe_allow_html=True)
        st.text_area("Data Receive", value=str(data), height=100, disabled=True, key=unique_key)
        st.markdown('</div>', unsafe_allow_html=True)
    
    iteration += 1
    time.sleep(1)  # Interval update dalam detik
