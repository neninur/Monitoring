import streamlit as st
import random
import time

# Pengaturan tampilan
st.set_page_config(layout="wide")

# Judul Aplikasi
st.title("MONITORING SYSTEM")

# Menampilkan subheader di sudut kiri atas dan sudut kanan atas
col1, col2 = st.columns(2)
with col1:
    st.subheader("BARELANG MARINE ROBOTICS TEAM")
with col2:
    st.subheader("POLITEKNIK NEGERI BATAM")

# Fungsi untuk menghasilkan data random
def generate_random_data():
    return {
        "DAY": "SUNDAY",  # Anda dapat mengganti ini dengan data dinamis sesuai kebutuhan
        "DATE": random.randint(1, 10),
        "TIME": random.randint(1, 10),
        "COORDINATE": random.randint(1, 10),
        "SOG": random.randint(1, 10),
        "COG": random.randint(1, 10)
    }

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
while True:
    data = generate_random_data()
    
    # Update konten dalam placeholder
    with placeholder:
        st.markdown('<div class="border-box">', unsafe_allow_html=True)
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            st.text("DAY")
            st.text(data["DAY"])
        with col2:
            st.text("DATE")
            st.text(str(data["DATE"]))
        with col3:
            st.text("TIME")
            st.text(str(data["TIME"]))
        with col4:
            st.text("COORDINATE")
            st.text(str(data["COORDINATE"]))
        with col5:
            st.text("SOG")
            st.text(str(data["SOG"]))
        with col6:
            st.text("COG")
            st.text(str(data["COG"]))
        st.markdown('</div>', unsafe_allow_html=True)
    
    time.sleep(1)  # Interval update dalam detik
