import numpy as np
from sklearn.linear_model import LogisticRegression

hours = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
])

result = np.array([
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    1
])

model = LogisticRegression()

model.fit(hours, result)

prediction = model.predict([[4.5]])

probability = model.predict_proba([[4.5]])

print("Prediction:", prediction)
print("Probability:", probability)