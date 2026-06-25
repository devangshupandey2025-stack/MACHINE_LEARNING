import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
import numpy as np

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

plt.figure(figsize=(8,6))

plot_tree(
    model,
    feature_names=["Hours"],
    class_names=["Fail", "Pass"],
    filled=True
)

plt.show()