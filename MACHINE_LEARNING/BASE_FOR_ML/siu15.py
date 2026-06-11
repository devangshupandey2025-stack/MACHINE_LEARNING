import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["John", "Emma", "Mike", "Sara", "Alex"],
    "Age": [25, np.nan, 28, 35, np.nan],
    "Salary": [50000, 65000, np.nan, 70000, 60000]
})

print(df)
print(df.isna())
print(df.isna().sum())
print(df.dropna())
print(df["Age"].fillna(df["Age"].mean()))
print(df["Salary"].fillna(df["Salary"].mean()))
print(df)