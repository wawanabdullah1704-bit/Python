import pandas as pd
import numpy as np

data = {
    'Employee_ID': ['E201', 'E202', 'E203', 'E204', 'E205', 'E206'],
    'Department': ['Sales', 'Support', 'Sales', 'Sales', 'Support', 'Sales'],
    'Sales_Target': [50000, 20000, 60000, 45000, 20000, 50000],
    'Sales_Achieved': [55000, np.nan, 48000, 50000, 18000, np.nan],
    'Rating': [4.5, 3.8, 3.2, 4.0, np.nan, 4.2]
}

emp_df = pd.DataFrame(data)

print("----- Non-Null Values Per Column -----")
print(emp_df.count())

median_sales = emp_df['Sales_Achieved'].median()
print(f"\nSales Achieved Median (Used for Imputation): ${median_sales:,.2f}")

emp_df['Sales_Achieved'] = emp_df['Sales_Achieved'].fillna(median_sales)
emp_df['Rating'] = emp_df['Rating'].fillna(3.0)

sales_high_performers = emp_df[(emp_df['Department'] == 'Sales') & (emp_df['Sales_Achieved'] >= 50000)]
print("\n----- Subsetting Output: Sales High Performers -----")
print(sales_high_performers)

emp_df['Bonus'] = np.where(emp_df['Sales_Achieved'] >= emp_df['Sales_Target'], emp_df['Sales_Achieved'] * 0.10, 0.0)

total_bonus = emp_df['Bonus'].sum()
print(f"\nTotal Company Bonus Payout: ${total_bonus:,.2f}")

print("\n----- Final Manipulated DataFrame Output -----")
print(emp_df)