import pandas as pd

students = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(students)

print(df)
print(df.shape)
print(df.columns)
print(df.head())
print(df.info())
print(df.describe())
