import streamlit as st

# Judul besar
st.title('Monitoring System')

# Group box untuk menampilkan data sensor
with st.beta_expander('Sensor Data', expanded=True):
    # Membuat 4 textbox untuk menampilkan data sensor
    sensor1 = st.text_input('Sensor 1 Data', value='0', key='sensor1')
    sensor2 = st.text_input('Sensor 2 Data', value='0', key='sensor2')
    sensor3 = st.text_input('Sensor 3 Data', value='0', key='sensor3')
    sensor4 = st.text_input('Sensor 4 Data', value='0', key='sensor4')

    # Tombol untuk memperbarui data sensor (opsional)
    if st.button('Update Data'):
        st.write('Data updated')
        # Anda bisa menambahkan kode di sini untuk mengambil data terbaru dari backend

# Menambahkan informasi tambahan atau fitur lain di bawah group box
st.write('Additional features can be added here')
