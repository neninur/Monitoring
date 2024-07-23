import streamlit as st
import random
import time

# Pengaturan tampilan
st.set_page_config(layout="wide")

# Judul Aplikasi
st.title("Data Monitoring")

# Placeholder untuk update konten
placeholder = st.empty()

# Loop untuk update data secara dinamis
while True:
    try:
        # Generate data random 1-5
        data = random.randint(1, 5)

        # Update konten dalam placeholder
        with placeholder.container():
            st.text_area("Data Receive", value=str(data), height=100, disabled=True, key="data_receive")

        time.sleep(1)  # Interval update dalam detik

    except Exception as e:
        st.error(f"Error: {e}")
        break
