import streamlit as st
import numpy as np
import pandas as pd

st.title("Apex Logistics Management System")

# Base class
class Item:
    def __init__(self, item_id, unit_price):
        self.item_id = item_id
        self.unit_price = float(unit_price)

    # Operator overloading untuk tambah harga dua barang
    def __add__(self, other):
        return self.unit_price + other.unit_price

    def __str__(self):
        return f"Item ID: {self.item_id} | Unit Price: RM{self.unit_price:.2f}"


# Subclass yang inherit dari Item
class PerishableItem(Item):
    def __init__(self, item_id, unit_price, expiry_date):
        super().__init__(item_id, unit_price)
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{super().__str__()} | Expiry Date: {self.expiry_date}"


# --- Bahagian 1: Pendaftaran Item & OOP ---
st.subheader("1. Pendaftaran Produk")

col1, col2 = st.columns(2)
with col1:
    id1 = st.text_input("ID Item 1:", "ITM01")
    price1 = st.text_input("Harga Item 1 (RM):", "40.00")

with col2:
    id2 = st.text_input("ID Item 2 (Perishable):", "PRSH02")
    price2 = st.text_input("Harga Item 2 (RM):", "15.50")
    expiry = st.text_input("Tarikh Luput:", "2026-12-31")

if st.button("Daftar Item"):
    try:
        # Cuba convert harga kepada float
        p1 = float(price1)
        p2 = float(price2)

        item1 = Item(id1, p1)
        item2 = PerishableItem(id2, p2, expiry)

        # Guna operator __add__
        total = item1 + item2

        st.success("Item berjaya didaftarkan.")
        st.write(str(item1))
        st.write(str(item2))
        st.write(f"Jumlah Harga (Operator Overloading): RM{total:.2f}")

    except ValueError:
        st.error("Error: Sila masukkan nombor sahaja untuk harga.")


# --- Bahagian 2: Stok Gudang (NumPy Matrix 5x5) ---
st.subheader("2. Paras Stok Gudang (NumPy 5x5)")

# Matriks stok 5 seksyen x 5 rak
stock = np.array([
    [50, 20, 60, 30, 15],  # Seksyen A
    [10, 5, 8, 12, 4],     # Seksyen B
    [80, 90, 75, 85, 70],  # Seksyen C
    [25, 30, 40, 35, 20],  # Seksyen D
    [5, 8, 12, 6, 9]       # Seksyen E
])

st.write("Matriks Stok Gudang:")
st.write(stock)

total_stock = np.sum(stock)
section_totals = np.sum(stock, axis=1)

st.write(f"Jumlah Keseluruhan Stok: {total_stock} unit")

# Check seksyen stok rendah (< 50 unit)
for i in range(len(section_totals)):
    if section_totals[i] < 50:
        seksyen = chr(65 + i)
        st.warning(f"Amaran: Seksyen {seksyen} mempunyai stok rendah ({section_totals[i]} unit).")

# Kira agihan stok guna try-except
trucks = st.number_input("Bilangan lori untuk agihan stok:", min_value=0, value=0)
if st.button("Kira Stok Setiap Lori"):
    try:
        per_truck = total_stock / trucks
        st.success(f"Stok untuk setiap lori: {per_truck:.2f} unit")
    except ZeroDivisionError:
        st.error("Error: Bilangan lori tidak boleh 0.")


# --- Bahagian 3: Analisis Jualan (Pandas) ---
st.subheader("3. Analisis dan Pembersihan Data Jualan (Pandas)")

# Dataset jualan
raw_sales = {
    'Order_ID': [101, 102, 103, 102, 104, 105, 106, 107],
    'Category': ['Electronics', 'Clothing', 'Perishable', 'Clothing', 'Home', 'Electronics', 'Perishable', 'Clothing'],
    'Price': [299.99, 45.00, 15.50, 45.00, np.nan, 89.99, 12.50, 35.00],
    'Units_Sold': [12, 25, 50, 25, 8, np.nan, 4, 30]
}

df = pd.DataFrame(raw_sales)

st.write("Data Asal:")
st.dataframe(df)

# 1. Buang duplicate
df_clean = df.drop_duplicates(keep='first').copy()

# 2. Ganti NaN dengan nilai purata (mean)
df_clean['Price'] = df_clean['Price'].fillna(df_clean['Price'].mean())
df_clean['Units_Sold'] = df_clean['Units_Sold'].fillna(df_clean['Units_Sold'].mean())

st.write("Data Selepas Dibersihkan (Tiada Duplicate & NaN diganti Mean):")
st.dataframe(df_clean)

# 3. Filter jualan tinggi (Units_Sold >= 20)
high_sales = df_clean[df_clean['Units_Sold'] >= 20]

st.write("Item Jualan Tinggi (Units Sold >= 20):")
st.dataframe(high_sales)