import pandas as pd
employees = pd.DataFrame({
    "Name": ["John", "Emma", "Mike", "Sara"],
    "Age": [25, 30, 28, 35],
    "Salary": [50000, 65000, 55000, 70000]
})
print(employees.iloc[0])
print(employees.iloc[2])
print(employees.iloc[1, 2])
print(employees.iloc[:,1])
print(employees.iloc[1:3])

employees.index = ["E1", "E2", "E3", "E4"]

print(employees.loc["E1"])
print(employees.loc["E3"])
print(employees.loc["E2", "Salary"])
print(employees.loc[:, "Name"])
print(employees.loc["E2":"E4"])