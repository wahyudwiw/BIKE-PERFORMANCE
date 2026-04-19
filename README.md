# 📊 Proyek Analisis Data: Bike Sharing Dataset


---

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda menggunakan **Bike Sharing Dataset**. Analisis dilakukan untuk mengetahui pengaruh faktor lingkungan dan waktu terhadap jumlah penyewaan sepeda.

Hasil analisis kemudian divisualisasikan melalui dashboard interaktif menggunakan **Streamlit**.

---

## 🎯 Pertanyaan Bisnis

1. Bagaimana pengaruh kategori suhu terhadap rata-rata jumlah penyewaan sepeda pada periode 2011–2012?

2. Pada jam berapa rata-rata jumlah penyewaan sepeda mencapai puncaknya dalam satu hari berdasarkan data tahun 2011–2012?

---

## 📊 Insight Hasil Analisis

* Kategori suhu yang lebih hangat cenderung memiliki rata-rata jumlah penyewaan lebih tinggi.
* Puncak penyewaan sepeda terjadi pada pagi hari dan sore hari.
* Sepeda banyak digunakan sebagai sarana mobilitas harian.

---

## 💡 Rekomendasi Bisnis

* Menambah ketersediaan sepeda pada jam sibuk, terutama pagi dan sore hari.
* Mengoptimalkan operasional pada kondisi cuaca hangat.
* Menyediakan promosi khusus pada periode permintaan rendah.

---

## ▶️ Cara Menjalankan Dashboard

### 1. Install dependencies

pip install -r requirements.txt

### 2. Jalankan dashboard Streamlit

streamlit run dashboard.py

---

## 📁 Struktur Folder

submission/
├── dashboard.py
├── main_data.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt

---

## 🌐 Dashboard Online

https://bike-performance.streamlit.app/

---

## 🚀 Teknologi yang Digunakan

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit
