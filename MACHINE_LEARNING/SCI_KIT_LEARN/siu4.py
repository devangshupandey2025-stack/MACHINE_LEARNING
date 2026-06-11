from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

X = np.array([
    [2],
    [4],
    [6],
    [8],
    [10]
])

y = np.array([20, 35, 55, 70, 95])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Test Inputs:")
print(X_test)

print("Actual:")
print(y_test)

print("Predicted:")
print(predictions)