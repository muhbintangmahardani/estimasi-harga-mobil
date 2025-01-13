import pickle
import streamlit as st

# Load model
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# Menambahkan background gambar
def add_bg_from_local(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = image_file.read()
    bg_style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image.hex()}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

# Panggil fungsi untuk menambahkan background
add_bg_from_local("/mnt/data/mobil.png")

# Judul Aplikasi
st.markdown(
    """
    <div style="text-align: center;">
        <h1>Universitas Bina Sarana Informatika</h1>
        <h2>Project Machine Learning</h2>
        <h3>Estimasi Harga Mobil Bekas</h3>
        <p><b>Menggunakan Algoritma:</b></p>
        <ul style="list-style: none; padding: 0;">
            <li>- Linear Regression</li>
            <li>- Decision Tree Regressor</li>
            <li>- Deployment di Streamlit</li>
        </ul>
        <p><b>Oleh:</b></p>
        <p>Muh Bintang Mahardani (17225123)</p>
        <p>Taufiq Ismail (17215032)</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Input data dari pengguna
st.write("### Masukkan Data Mobil")
year = st.number_input('Tahun Mobil', step=1, format="%d", value=None)
mileage = st.number_input('Kilometer Mobil (Km)', min_value=0, step=1, format="%d", value=None)
tax = st.number_input('Pajak Mobil (Pounds)', min_value=0, step=1, format="%d", value=None)
mpg = st.number_input('Konsumsi BBM Mobil (MPG)', min_value=0, step=1, format="%d", value=None)
engineSize = st.number_input('Ukuran Mesin (L)', min_value=0, step=1, format="%d", value=None)

# Cek apakah semua input telah diisi
inputs_filled = all(value is not None for value in [year, mileage, tax, mpg, engineSize])

# Tampilkan peringatan jika tombol ditekan tanpa semua input terisi
if st.button('Estimasi Harga') and not inputs_filled:
    st.warning("Harap isi semua input terlebih dahulu!")

# Prediksi Harga
if inputs_filled:
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write('### Hasil Estimasi')
    st.write(f'Estimasi harga mobil bekas dalam Pounds: **£{int(predict[0]):,}**')
    st.write(f'Estimasi harga mobil bekas dalam IDR (Juta): **Rp{int(predict[0] * 19000) / 1_000_000:,} Juta**')
