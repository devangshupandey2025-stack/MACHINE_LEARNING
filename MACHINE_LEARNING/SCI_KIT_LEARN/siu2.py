from sklearn.linear_model import LinearRegression
import numpy as np
hours = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

marks = np.array([15, 30, 45, 60, 75])

model = LinearRegression()

model.fit(hours, marks)

prediction = model.predict(np.array([[6]]))
print(prediction)