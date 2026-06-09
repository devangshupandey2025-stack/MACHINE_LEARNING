import pandas as pd

df = pd.DataFrame({
    "Name": ["John","Emma","Mike","Sara","Alex","Tom"],
    "Department": ["IT","HR","Finance","IT","HR","Finance"],
    "Salary": [50000,65000,55000,70000,60000,52000]
})

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department").size())