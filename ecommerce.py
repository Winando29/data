import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data dari CSV
@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

file_path = "ecommerce.csv"  # Ganti dengan path file CSV Anda
df = load_data(file_path)

# Menghitung jumlah pesanan per bulan
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['month'] = df['order_purchase_timestamp'].dt.month
monthly_orders = df.groupby('month')['order_id'].count()

# Menghitung jumlah pelanggan pembelian berulang
repeat_customers = df[df['customer_id'].duplicated()]['customer_id'].nunique()
total_customers = df['customer_id'].nunique()
repeat_customer_percentage = (repeat_customers / total_customers) * 100

# Streamlit App
st.title('Analisis Data E-Commerce')

# Plot jumlah pesanan per bulan
st.write('## Jumlah Pesanan per Bulan')
fig_orders, ax_orders = plt.subplots()
ax_orders.bar(monthly_orders.index, monthly_orders.values)
ax_orders.set_xlabel('Bulan')
ax_orders.set_ylabel('Jumlah Pesanan')
st.pyplot(fig_orders)

# Kesimpulan pertanyaan pertama
st.write("""
### Kesimpulan Jumlah Pesanan per Bulan:
Grafik di atas menunjukkan jumlah pesanan per bulan dalam dataset e-commerce ini. Terlihat bahwa jumlah pesanan cenderung fluktuatif selama setahun, dengan puncak tertinggi pada bulan-bulan tertentu.

""")

st.write('---')

# Menampilkan informasi jumlah pelanggan pembelian berulang
st.write('## Informasi Pelanggan Pembelian Berulang')
st.write(f"Jumlah Pelanggan Pembelian Berulang: {repeat_customers}")
st.write(f"Total Jumlah Pelanggan: {total_customers}")
st.write(f"Persentase Pelanggan Pembelian Berulang: {repeat_customer_percentage:.2f}%")

# Plot persentase pelanggan pembelian berulang
fig_percentage, ax_percentage = plt.subplots()
labels = ['Pelanggan Pembelian Berulang', 'Pelanggan Non-Berulang']
sizes = [repeat_customers, total_customers - repeat_customers]
colors = ['#ff9999','#66b3ff']
ax_percentage.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax_percentage.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax_percentage.set_title('Persentase Pelanggan Pembelian Berulang')
st.pyplot(fig_percentage)

# Kesimpulan pertanyaan kedua
st.write("""
### Kesimpulan Informasi Pelanggan Pembelian Berulang:
Dari data e-commerce yang diberikan, terdapat informasi bahwa ada sejumlah pelanggan yang melakukan pembelian berulang. Jumlah pelanggan pembelian berulang adalah {repeat_customers}, dari total {total_customers} pelanggan yang tercatat dalam dataset. Hal ini menunjukkan bahwa sebagian pelanggan cenderung lebih loyal dan berkontribusi terhadap transaksi berulang di platform e-commerce ini.
""")

