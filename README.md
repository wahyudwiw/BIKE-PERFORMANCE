# 📊 Bike Sharing Dashboard

## Deskripsi Proyek

Dashboard ini dibuat untuk menganalisis pola penyewaan sepeda menggunakan **Bike Sharing Dataset**. Visualisasi disusun berdasarkan hasil analisis data pada notebook.



## 📁 Struktur Folder

submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── README.md
└── requirements.txt



## ▶️ Cara Menjalankan Dashboard

### 1. Install Library

pip install -r requirements.txt

### 2. Masuk ke Folder Dashboard

cd dashboard

### 3. Jalankan Streamlit

py -m streamlit run dashboard/dashboard.py



## 🌐 Dashboard Online

https://bike-performance.streamlit.app/



## 📌 Insight Utama

* Penyewaan tertinggi terjadi pada kategori suhu panas.
* Jam puncak penyewaan terjadi pukul 17.00.
* Sepeda banyak digunakan pada jam berangkat dan pulang kerja.



## 🚀 Teknologi yang Digunakan

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit
