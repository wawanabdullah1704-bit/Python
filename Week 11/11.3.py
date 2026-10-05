import pandas as pd
import numpy as np

raw_data = {
    'ProductID': ['P101', 'P102', 'P103', 'P104', 'P105', 'P106', 'P107'],
    'Department': ['Electronics', 'Furniture', 'Electronics', 'Clothing', 'Furniture', 'Clothing', 'Electronics'],
    'Unit_Cost': [120.50, 45.00, np.nan, 25.00, 210.00, 15.50, 80.00],
    'Stock_Qty': [60, 30, 85, np.nan, 40, 110, 15]
}

inventory_df = pd.DataFrame(raw_data)
print(inventory_df)

inventory_df.info()
print(inventory_df.dtypes)

print("Median Unit Cost:", inventory_df['Unit_Cost'].median())
print("Total Stock Qty:", inventory_df['Stock_Qty'].sum())

print(inventory_df[inventory_df['Stock_Qty'] > 50])

inventory_df['Inventory_Value'] = inventory_df['Unit_Cost'] * inventory_df['Stock_Qty']
inventory_df = inventory_df.fillna(0)
print(inventory_df)
