import os
import streamlit as st
import numpy as np
import pandas as pd

st.title("CaNaWa Logistics")

class Item:
    def __init__(self, item_id, unit_price):
        self.item_id = item_id
        self.unit_price = float(unit_price)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.unit_price + other.unit_price
        return self.unit_price + float(other)

    def __str__(self):
        return f"Item ID: {self.item_id} | Unit Price: RM{self.unit_price:.2f}"


class PerishableItem(Item):
    def __init__(self, item_id, unit_price, expiry_date):
        super().__init__(item_id, unit_price)
        self.expiry_date = expiry_date

    def __str__(self):
        return f"{super().__str__()} | Expiry: {self.expiry_date}"


st.subheader("Item Registration")

col1, col2 = st.columns(2)
with col1:
    price1 = st.text_input("Price Item 1 (RM):", "67.00")
with col2:
    price2 = st.text_input("Price Item 2 (RM):", "11.00")

if st.button("Register"):
    try:
        item1 = Item("A001", price1)
        item2 = PerishableItem("B002", price2, "2026-04-17")
        total = item1 + item2

        st.write(str(item1))
        st.write(str(item2))
        st.success(f"Total Price: RM{total:.2f}")
    except ValueError:
        st.error("Sila masukkan nombor sahaja")

st.subheader("Warehouse Stock")

stock = np.array([
    [43, 68, 32, 57, 9],
    [65, 66, 22, 90, 12],
    [88, 10, 21, 40, 30],
    [31, 45, 29, 67, 83],
    [49, 11, 8, 78, 63]
])

st.write("Matriks Stock")
st.write(stock)

total_stock = np.sum(stock)
st.write(f"Total Stock: {total_stock} units")

section_sum = np.sum(stock, axis=1)
for i in range(5):
    if section_sum[i] < 200:
        st.warning(f"Section {chr(65 + i)} has low stock ({section_sum[i]} units).")

trucks = st.number_input("Number of trucks to divide stock:", min_value=0, value=0)
if st.button("Calculate Stock Per Truck"):
    try:
        result = int(total_stock) / int(trucks)
        st.success(f"Stock per truck: {result:.2f} units")
    except ZeroDivisionError:
        st.error("Error: Bilangan lori tidak boleh 0.")

st.subheader("Sales Data Pre-processing")

uploaded_file = st.file_uploader("Upload sales CSV file:", type=["csv"])

df = None
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as err:
        st.error(f"Error membaca fail CSV: {err}")
else:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, "sales_records.csv")
        if os.path.exists(csv_path):
            with open(csv_path, "r", encoding="utf-8") as f:
                df = pd.read_csv(f)
            st.info("Using default file: sales_records.csv")
    except Exception as err:
        st.error(f"Error memuatkan fail lalai: {err}")

if df is not None:
    st.write("Raw Data from CSV:", df)

    df_clean = df.drop_duplicates(keep="first").copy()

    if "Price" in df_clean.columns:
        df_clean["Price"] = df_clean["Price"].fillna(df_clean["Price"].mean())
    if "Units_Sold" in df_clean.columns:
        df_clean["Units_Sold"] = df_clean["Units_Sold"].fillna(df_clean["Units_Sold"].mean())

    st.write("Cleaned Data (Duplicates removed & NaN filled with mean):", df_clean)

    if "Units_Sold" in df_clean.columns:
        high_sales = df_clean[df_clean["Units_Sold"] >= 20]
        st.write("High Sales Volume (Units Sold >= 20):", high_sales)

    st.download_button(
        label="Download Cleaned CSV",
        data=df_clean.to_csv(index=False).encode("utf-8"),
        file_name="cleaned_sales.csv",
        mime="text/csv"
    )