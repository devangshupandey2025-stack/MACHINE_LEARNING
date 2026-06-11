from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Dataset
X = np.array([
    [1],
    [2],
    [3],
    [5],
    [7],
    [8],
    [10],
    [12],
    [15],
    [18]
])

y = np.array([
    25,
    30,
    38,
    50,
    65,
    72,
    90,
    105,
    130,
    160
])

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Test Predictions
predictions = model.predict(X_test)

print("===== TEST RESULTS =====")

for exp, actual, pred in zip(X_test, y_test, predictions):
    print(f"Experience: {exp[0]} years")
    print(f"Actual Salary: {actual}")
    print(f"Predicted Salary: {pred:.2f}")
    print(f"Error: {abs(actual - pred):.2f}")
    print("-" * 30)

# Future Predictions
print("\n===== FUTURE PREDICTIONS =====")

for years in [6, 20]:
    salary_pred = model.predict(np.array([[years]]))[0]
    print(f"{years} years experience -> Salary = {salary_pred:.2f}")