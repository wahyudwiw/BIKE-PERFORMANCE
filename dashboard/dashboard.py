import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# konfirmasi halaman
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)


# load data
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "main_data.csv")

df = pd.read_csv(file_path)
df["dteday"] = pd.to_datetime(df["dteday"])


# sidebar
st.sidebar.title("🚲 Bike Analysis")
st.sidebar.write("Dashboard Analisis Penyewaan Sepeda")

# Filter tanggal
start_date = st.sidebar.date_input(
    "Tanggal Awal",
    df["dteday"].min()
)

end_date = st.sidebar.date_input(
    "Tanggal Akhir",
    df["dteday"].max()
)

# Filter data
filtered_df = df[
    (df["dteday"] >= pd.to_datetime(start_date)) &
    (df["dteday"] <= pd.to_datetime(end_date))
]


# header
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Visualisasi dibuat sesuai hasil analisis pada notebook")


# metric
col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", int(filtered_df["cnt"].sum()))
col2.metric("Rata-rata", round(filtered_df["cnt"].mean(), 2))
col3.metric("Maksimum", int(filtered_df["cnt"].max()))

st.markdown("---")


# visualisasi pertanyaan 1
st.subheader("1️⃣ Pengaruh Kategori Suhu terhadap Rata-rata Penyewaan")

temp_df = filtered_df.groupby("temp_category")["cnt"].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(8,5))
sns.barplot(
    data=temp_df,
    x="temp_category",
    y="cnt",
    palette="coolwarm",
    ax=ax1
)

ax1.set_xlabel("Kategori Suhu")
ax1.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig1)

st.info("Kategori suhu Panas memiliki rata-rata penyewaan tertinggi.")


# visualisasi pertanyaan 2
st.subheader("2️⃣ Jam Puncak Penyewaan Sepeda")

hour_df = filtered_df.groupby("hr")["cnt"].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10,5))
sns.lineplot(
    data=hour_df,
    x="hr",
    y="cnt",
    marker="o",
    ax=ax2
)

ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig2)

st.info("Puncak penyewaan terjadi sekitar pukul 17.00.")


# kesimpulan
with st.expander("📌 Lihat Detail Kesimpulan & Rekomendasi Bisnis"):

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Kesimpulan")
        st.write("""
        - Suhu hangat meningkatkan jumlah penyewaan.
        - Penyewaan tertinggi terjadi sore hari.
        - Sepeda banyak digunakan untuk mobilitas harian.
        """)

    with col2:
        st.subheader("Rekomendasi")
        st.write("""
        - Tambah stok sepeda di jam sibuk.
        - Fokus promosi saat cuaca hangat.
        - Tingkatkan layanan pada sore hari.
        """)


# footer
st.markdown("---")
st.caption("© 2026 Wahyu Dwi Wicaksono | Dicoding Submission")
