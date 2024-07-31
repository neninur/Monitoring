import streamlit as st
import requests

st.title("Streamlit dengan Backend Flask")

if st.button("Dapatkan Data Acak"):
    response = requests.get("https://twenty-eels-dress.loca.lt/random-data")
    data = response.json()
    st.write(f"Data Acak: {data['data']}")
