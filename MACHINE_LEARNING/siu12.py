import pandas as pd
company = pd.DataFrame({
    "Name" : ["Alice", "Bob", "Charlie","David", "Eva"],
    "Department" : ["HR", "IT", "Finance", "IT", "HR"],
    "Salary" : [40000, 60000, 55000, 70000, 45000]
})
print("<--The DataFrame-->")
print(company)
print("<--Show first 3 rows-->")
print(company.head(3))
print("<--Show last 2 rows-->")
print(company.tail(2))
print("<--Print shape-->")
print(company.shape)
print("<--The column names-->")
print(company.columns)
print("<--The datatypes-->")
print(company.dtypes)
print("<--Calculate average salary-->")
print(company["Salary"].mean())
print("<--Find highest salary-->")
print(company["Salary"].max())
print("<--Find employees with salary > 50000-->")
print(company[company["Salary"] > 50000])
company["Bonus"] = company["Salary"] * 0.1
print("<--Add column: Bonus = Salary * 0.1-->")
print(company)
print(company.describe())