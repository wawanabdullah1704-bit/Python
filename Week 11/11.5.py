import pandas as pd
import numpy as np

# Provide DataFrame
data = {
    'Ticket_ID': ['T101', 'T102', 'T103', 'T104', 'T105', 'T106'],
    'Region': ['North', 'South', 'North', 'West', 'South', 'West'],
    'Priority': ['High', 'Low', 'Medium', 'High', np.nan, 'Low'],
    'Resolution_Time_Hrs': [4.5, np.nan, 2.0, 6.0, 1.5, np.nan],
    'Satisfaction_Score': [5, 3, np.nan, 4, 2, 4]
}

tickets_df = pd.DataFrame(data)

# DataFrame dimensions
print(tickets_df.shape)

# Fill missing values
mean_rst = tickets_df['Resolution_Time_Hrs'].mean()
tickets_df['Resolution_Time_Hrs'] = tickets_df['Resolution_Time_Hrs'].fillna(mean_rst)
tickets_df['Priority'] = tickets_df['Priority'].fillna('Medium')

print(tickets_df)