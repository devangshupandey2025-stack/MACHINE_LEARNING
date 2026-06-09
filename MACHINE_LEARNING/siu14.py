import pandas as pd

df = pd.read_csv("employees.csv")

print(df.head(5))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df["Salary"].mean())
print(df[df["Department"] == "IT"])
print(df[df["Salary"] > 55000])
df["Bonus"] = df["Salary"]*0.1
print(df)
df.to_csv("employees_updated.csv", index=False)