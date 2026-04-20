import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==================================
# PAGE CONFIG
# ==================================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# ==================================
# LOAD DATA
# ==================================
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "main_data.csv")

df = pd.read_csv(file_path)
df["dteday"] = pd.to_datetime(df["dteday"])

# ==================================
# CLEANING DATA
# ==================================
bins = [0, 0.25, 0.5, 0.75, 1]
labels = ["Dingin", "Sedang", "Hangat", "Panas"]

df["temp_group"] = pd.cut(df["temp"], bins=bins, labels=labels)

# ==================================
# SIDEBAR FILTER
# ==================================
st.sidebar.title("🚲 Filter Dashboard")

start_date = st.sidebar.date_input(
    "Tanggal Awal",
    value=df["dteday"].min()
)

end_date = st.sidebar.date_input(
    "Tanggal Akhir",
    value=df["dteday"].max()
)

selected_temp = st.sidebar.multiselect(
    "Kategori Suhu",
    options=df["temp_group"].dropna().unique(),
    default=df["temp_group"].dropna().unique()
)

# ==================================
# FILTER DATA
# ==================================
filtered_df = df[
    (df["dteday"] >= pd.to_datetime(start_date)) &
    (df["dteday"] <= pd.to_datetime(end_date)) &
    (df["temp_group"].isin(selected_temp))
]

# ==================================
# HEADER
# ==================================
st.title("🚲 Bike Sharing Dashboard")
st.write("Dashboard interaktif berdasarkan hasil analisis Bike Sharing Dataset")

# ==================================
# METRICS
# ==================================
col1, col2, col3 = st.columns(3)

if filtered_df.empty:
    total_cnt = 0
    avg_cnt = 0
    max_cnt = 0
else:
    total_cnt = int(filtered_df["cnt"].sum())
    avg_cnt = round(filtered_df["cnt"].mean(), 2)
    max_cnt = int(filtered_df["cnt"].max())

col1.metric("Total Penyewaan", total_cnt)
col2.metric("Rata-rata Penyewaan", avg_cnt)
col3.metric("Penyewaan Maksimum", max_cnt)

if filtered_df.empty:
    st.warning("Tidak ada data sesuai filter yang dipilih.")

st.markdown("---")

# ==================================
# VISUALISASI 1
# ==================================
st.subheader("1️⃣ Pengaruh Kategori Suhu terhadap Rata-rata Penyewaan")

if not filtered_df.empty:
    temp_df = filtered_df.groupby("temp_group")["cnt"].mean().reset_index()

    fig1, ax1 = plt.subplots(figsize=(8,5))
    sns.barplot(
        data=temp_df,
        x="temp_group",
        y="cnt",
        palette="coolwarm",
        ax=ax1
    )

    ax1.set_xlabel("Kategori Suhu")
    ax1.set_ylabel("Rata-rata Penyewaan")

    st.pyplot(fig1)

# ==================================
# VISUALISASI 2
# ==================================
st.subheader("2️⃣ Jam Puncak Penyewaan Sepeda")

if not filtered_df.empty:
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
    ax2.set_xticks(range(0,24))

    st.pyplot(fig2)

# ==================================
# KESIMPULAN
# ==================================
with st.expander("📌 Lihat Kesimpulan & Rekomendasi"):

    st.markdown("""
    ### Insight:
    - Penyewaan tertinggi terjadi pada kategori suhu **Panas**.
    - Jam puncak penyewaan terjadi sekitar **17.00**.
    - Penyewaan ramai pada pagi dan sore hari.

    ### Rekomendasi:
    - Tambahkan stok sepeda pada jam sibuk.
    - Fokus promosi saat cuaca hangat.
    - Tingkatkan layanan di area kerja dan transportasi umum.
    """)

# ==================================
# FOOTER
# ==================================
st.markdown("---")
st.caption("© 2026 Wahyu Dwi Wicaksono | Dicoding Submission")