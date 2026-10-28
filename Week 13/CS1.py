import os
import streamlit as st
import numpy as np
import pandas as pd

st.title("Diana Logistics")

class Item:
    def __init__(self, itemID, unitPrice):
        self.itemID = itemID
        self.unitPrice = float(unitPrice)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.unitPrice + other.unitPrice
        return self.unitPrice + float(other)

    def __str__(self):
        return f"Item ID: {self.itemID} | Unit Price: RM{self.unitPrice:.2f}"

class perishableItem(Item):
    def __init__(self, itemID, unitPrice, expiryDate):
        super().__init__(itemID, unitPrice)
        self.expiryDate = expiryDate

    def __str__(self):
        return f"{super().__str__()}, Expiry: {self.expiryDate}"

st.subheader("Item Registration")
price1 = st.text_input("Price Item 1:", "30.00")
price2 = st.text_input("Price Item 2:", "15.00")

if st.button("Register"):
    try:
        item1 = Item("A001", price1)
        item2 = perishableItem("B002", price2, "2026-04-17")
        total = item1 + item2

        st.write(str(item1))
        st.write(str(item2))
        st.success(f"Total Price: RM{total:.2f}")

    except ValueError:
        st.error("Sila masukkan nombor sahaja untuk harga")

st.subheader("Warehouse Stock")
stock = np.array([
    [43, 68, 32, 57, 9],
    [65, 66, 22, 90, 12],
    [88, 10, 21, 40, 30],
    [31, 45, 29, 67, 83],
    [49, 11, 8, 78, 63]
])

st.write(stock)
totalStock = np.sum(stock)
st.write(f"Total Stock: {totalStock}")

sectionSum = np.sum(stock, axis=1)
for i in range(5):
    if sectionSum[i] < 200:
        st.warning(f"Section {chr(65 + i)} has low stock ({sectionSum[i]} units).")

trucks = st.number_input("Number of trucks to divide stock:", min_value=0, value=0)
if st.button("Calculate Stock Per Truck"):
    try:
        result = int(totalStock) / int(trucks)
        st.success(f"Stock per truck: {result:.2f} units")
    except ZeroDivisionError:
        st.error("Error: Bilangan lori tidak boleh 0.")

st.subheader("Sales Data Pre-processing")

uploadedFile = st.file_uploader("Upload sales CSV file:", type=["csv"])

df = None
if uploadedFile is not None:
    try:
        df = pd.read_csv(uploadedFile)
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
        else:
            raw_data = {
                'Order_ID': [101, 102, 103, 102, 104, 105, 106, 107],
                'Category': ['Electronics', 'Clothing', 'Perishable', 'Clothing', 'Home', 'Electronics', 'Perishable', 'Clothing'],
                'Price': [299.99, 45.00, 15.50, 45.00, np.nan, 89.99, 12.50, 35.00],
                'Units_Sold': [12, 25, 50, 25, 8, np.nan, 4, 30]
            }
            df = pd.DataFrame(raw_data)
    except Exception as err:
        st.error(f"Error memuatkan data: {err}")

if df is not None:
    st.write("Raw Data from CSV", df)

    df_clean = df.drop_duplicates(keep="first").copy()
    if "Price" in df_clean.columns:
        df_clean["Price"] = df_clean["Price"].fillna(df_clean["Price"].mean())
    if "Units_Sold" in df_clean.columns:
        df_clean["Units_Sold"] = df_clean["Units_Sold"].fillna(df_clean["Units_Sold"].mean())

    st.write("Cleaned Data", df_clean)

    if "Units_Sold" in df_clean.columns:
        high_sales = df_clean[df_clean["Units_Sold"] >= 20]
        st.write("High Sales Volume (Units Sold >= 20)", high_sales)