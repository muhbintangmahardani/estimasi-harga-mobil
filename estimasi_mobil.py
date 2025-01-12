import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

# Input data dari pengguna
year = st.number_input('Input Tahun Mobil', min_value=1900, max_value=2025, step=1)
mileage = st.number_input('Input Km Mobil', min_value=0.0, step=1.0)
tax = st.number_input('Input Pajak Mobil', min_value=0.0, step=1.0)
mpg = st.number_input('Input Konsumsi BBM Mobil', min_value=0.0, step=0.1)
engineSize = st.number_input('Input Engine Size', min_value=0.0, step=0.1)

predict = ''

if st.button('Estimasi Harga'):
    if year > 0 and mileage >= 0 and tax >= 0 and mpg >= 0 and engineSize >= 0:
        predict = model.predict(
            [[year, mileage, tax, mpg, engineSize]]
        )
        st.write('Estimasi harga mobil bekas dalam Ponds : ', predict)
        st.write('Estimasi harga mobil bekas dalam IDR (Juta) :', predict * 19000)
    else:
        st.error('Input tidak valid! Pastikan semua nilai tidak negatif.')

