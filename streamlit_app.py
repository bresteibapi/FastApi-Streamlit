import streamlit as st
import requests

st.title('Приложение для предсказаний')

feature1 = st.number_input('Feature 1')
feature2 = st.number_input('Feature 2')

if st.button('Предсказать'):
    response = requests.post("http://127.0.0.1:8000/predict/", json={"feature1": feature1, "feature2": feature2})
    prediction = response.json()["prediction"]
    st.write(f'Предсказание: {prediction}')
