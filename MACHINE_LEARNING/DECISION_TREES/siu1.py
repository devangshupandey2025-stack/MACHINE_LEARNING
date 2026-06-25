import numpy as np
from sklearn.tree import DecisionTreeClassifier
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
    0,
    0,
    0,
    1,
    1,
    1,
    1
])
model = DecisionTreeClassifier()
model.fit(hours, result)
prediction = model.predict(np.array([[2.5]]))

print(prediction)