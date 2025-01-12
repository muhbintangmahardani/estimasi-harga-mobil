import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Universitas Bina Sarana Informatika')
st.title('PROJECT MACHINE LEARNING : ESTIMASI HARGA MOBIL BEKAS MENGGUNAKAN ALGORITMA MODEL LINEAR REGRESSION, DECISION TREE REGRESSOR & DEPLOYMENT DI STREAMLIT.')
st.title('Muh Bintang Mahardani (17225123)')
st.title('Taufiq Ismail (17215032)')
st.title('Estimasi Harga Mobil Bekas')

# Input data dari pengguna
year = st.number_input('Input Tahun Mobil', min_value=0, step=1)
mileage = st.number_input('Input Km Mobil', min_value=0.0, step=1.0)
tax = st.number_input('Input Pajak Mobil', min_value=0.0, step=1.0)
mpg = st.number_input('Input Konsumsi BBM Mobil', min_value=0.0, step=0.1)
engineSize = st.number_input('Input Engine Size', min_value=0.0, step=0.1)

predict = ''

# Validasi apakah semua input telah terisi
if st.button('Estimasi Harga', disabled=(year == 0 or mileage == 0.0 or tax == 0.0 or mpg == 0.0 or engineSize == 0.0)):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('Estimasi harga mobil bekas dalam Ponds : ', predict)
    st.write('Estimasi harga mobil bekas dalam IDR (Juta) :', predict * 19000)
