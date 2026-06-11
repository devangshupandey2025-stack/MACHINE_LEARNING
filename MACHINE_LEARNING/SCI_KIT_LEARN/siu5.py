from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

sizes = np.array([
    [800],
    [1000],
    [1200],
    [1500],
    [1800],
    [2000],
    [2200],
    [2500]
])

prices = np.array([
    40,
    50,
    58,
    72,
    85,
    95,
    105,
    120
])

X_train, X_test, y_train, y_test = train_test_split(
    sizes,
    prices,
    test_size = 0.25,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

test = model.predict(X_test)


print("Test Inputs:")
print(X_test)

print("Actual:")
print(y_test)

print("Predicted:")
print(test)