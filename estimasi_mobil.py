import pickle
import streamlit as st

# Load model
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# Judul Aplikasi
st.title('Universitas Bina Sarana Informatika')
st.header('Project Machine Learning')
st.subheader('Estimasi Harga Mobil Bekas')
st.text('Menggunakan Algoritma:')
st.text('- Linear Regression')
st.text('- Decision Tree Regressor')
st.text('- Deployment di Streamlit')
st.text('Oleh:')
st.text('Muh Bintang Mahardani (17225123)')
st.text('Taufiq Ismail (17215032)')

# Input data dari pengguna
st.write("### Masukkan Data Mobil")
year = st.number_input('Tahun Mobil', min_value=0, step=1, format="%d")
mileage = st.number_input('Kilometer Mobil (Km)', min_value=0, step=1, format="%d")
tax = st.number_input('Pajak Mobil (Pounds)', min_value=0, step=1, format="%d")
mpg = st.number_input('Konsumsi BBM Mobil (MPG)', min_value=0, step=1, format="%d")
engineSize = st.number_input('Ukuran Mesin (L)', min_value=0, step=1, format="%d")

# Prediksi Harga
predict = ''
if st.button('Estimasi Harga', disabled=(year == 0 or mileage == 0 or tax == 0 or mpg == 0 or engineSize == 0)):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('### Hasil Estimasi')
    st.write(f'Estimasi harga mobil bekas dalam Pounds: **£{int(predict[0]):,}**')
    st.write(f'Estimasi harga mobil bekas dalam IDR (Juta): **Rp{int(predict[0] * 19000) / 1_000_000:,} Juta**')

