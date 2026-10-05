import pandas as pd
import numpy as np

# Messy sales dataset
raw_sales = {
 'Order_ID': [101, 102, 103, 102, 104, 105, 106],
 'Category': ['Electronics', 'Clothing', np.nan, 'Clothing', 'Home', 'Electronics', np.nan],
 'Price': [299.99, 45.00, 150.00, 45.00, np.nan, 89.99, 12.50],
 'Units_Sold': [2, 1, 0, 1, 3, -1, 4] # Note: contains invalid/zero sales counts
}

df = pd.DataFrame(raw_sales)

df = df.drop_duplicates(subset=['Order_ID'], keep='first')

df['Category'] = df['Category'].fillna('Uncategorized')

median_price = df['Price'].median()
df['Price'] = df['Price'].fillna(median_price)

df_clean = df[df['Units_Sold'] >= 1].copy()

df_clean['Total_Sales'] = df_clean["Price"] * df_clean['Units_Sold']

category_revenue = df_clean.groupby('Category')['Total_Sales'].sum().reset_index()

print("-----Cleaned Data Frame-----")
print(df_clean)

print("-----Revenue-----")
print(category_revenue)