import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score
)

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

X_train, X_test, y_train, y_test = train_test_split(
    hours,
    result,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)

print("Predictions:", predictions)
print("Actual:", y_test)
print("Accuracy:", accuracy)
print("Confusion Matrix: ")
print(cm)

precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)