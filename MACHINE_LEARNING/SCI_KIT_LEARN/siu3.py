from sklearn.linear_model import LinearRegression
import numpy as np

hours = np.array([
    [2],
    [4],
    [6],
    [8],
    [10]
])

marks = np.array([20, 35, 55, 70, 95])

model = LinearRegression()

model.fit(hours, marks)

prediction1 = model.predict(np.array([[5]]))
prediction2 = model.predict(np.array([[12]]))

print(prediction1)
print(prediction2)