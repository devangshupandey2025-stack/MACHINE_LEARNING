from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np

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

X_test, X_train, y_test, y_train = train_test_split(
    X,
    y,
    test_size = 0.3,
    random_state = 42
)

model = LinearRegression()

test = model.fit(X_train,y_train)

predict = test.predict(X_test)
actual = y_test

mae = mean_absolute_error(actual, predict)
mse = mean_squared_error(actual, predict)
rmse = mse ** 0.5
R2score = r2_score(actual, predict)

print("Mean absolute error: ",mae)
print("Mean squared error: ", mse)
print("Root mean squared error: ",rmse)
print("R2score: ",R2score)