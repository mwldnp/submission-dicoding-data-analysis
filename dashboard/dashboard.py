import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

hour_df = pd.read_csv('data.csv')

st.title('Bike Sharing Dashboard :sparkles:')

# Sidebar Navigation
st.sidebar.title('Select data visualization')
selected_page = st.sidebar.radio("", ["Weather Analysis", "Season Analysis"])

# Weather Analysis
if selected_page == "Weather Analysis":
    st.header("Weather Analysis 🌤️")

    cnt_by_weather_df = hour_df.groupby(by='weathersit').cnt.sum().reset_index()

    colors = ["#FF8819", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.barplot(
    y="cnt",
    x="weathersit",
    data=cnt_by_weather_df,
    palette=colors,
    ax=ax
)

    ax.set_title('Number of Bike Renters Based on Season')
    ax.set_xticklabels(['Clear', 'Mist', 'Light Snow/Rain', 'Heavy Rain/Snow'], rotation=0)
    ax.set_ylabel(None)
    ax.set_xlabel('Weather')
    ax.tick_params(axis='x', labelsize=12)
    st.pyplot(fig)
    
    st.subheader("Conclution")

    st.markdown("""
                #### Pelanggan paling sering menyewa sepeda pada saat cuaca Cerah.

                Berdasarkan data jumlah penyewa sepeda berdasarkan cuaca :
                - Clear : **2.338.173**
                - Mist : **795.952**
                - Light Snow/Rain : **158.331**
                - Heavy Rain/Snow : **223**

                **Rekomendasi**:
                1. Menyediakan lebih banyak unit sepeda pada saat cuaca diprediksi cerah.
                2. Mengoptimalkan pelayanan pada saat cuaca diprediksi cerah.
                3. Menyusun strategi promosi pada kondisi cuaca cerah untuk menarik lebih banyak pelanggan.
            """)

# Season Analysis
elif selected_page == "Season Analysis":
    st.header("Season Analysis 🍂")

    cnt_by_season_df = hour_df.groupby(by='season').cnt.sum().reset_index()

    colors = ["#D3D3D3", "#D3D3D3", "#FF8819", "#D3D3D3"]

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.barplot(
    y="cnt",
    x="season",
    data=cnt_by_season_df,
    palette=colors,
    ax=ax
)

    ax.set_title('Number of Bike Renters Based on Season')
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'], rotation=0)
    ax.set_ylabel(None)
    ax.set_xlabel('Season')
    ax.tick_params(axis='x', labelsize=12)
    st.pyplot(fig)

    st.subheader("Conclution")

    st.markdown("""
                #### Pelanggan paling sering menyewa sepeda pada saat musim Cerah.

                Berdasarkan data jumlah penyewa sepeda berdasarkan cuaca :
                - Spring : **471.348**
                - Summer : **918.589**
                - Fall : **1.061.129**
                - Winter : **841.613**

                **Rekomendasi**:
                1. Menambahkan unit sepeda pada saat musim-musim dengan permintaan tinggi (seperti musim gugur dan semi)
                2. Melakukan strategi promosi dan diskon pada saat musim dengan pengguna sepeda tertinggi
                3. Mempersiapkan strategi dalam menghadapi musim yann memiliki pengguna sepeda terendah (seperti musim salju)
            """)

st.caption('Copyright © Wildan 2024')
