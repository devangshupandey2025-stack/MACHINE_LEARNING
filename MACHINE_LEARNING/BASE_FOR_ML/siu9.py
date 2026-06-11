import numpy as np

marks = np.array([
    [78, 85, 90, 67, 88],
    [45, 56, 62, 48, 51],
    [92, 88, 95, 91, 89],
    [34, 40, 29, 45, 38],
    [67, 72, 70, 75, 80]
])
print(marks.mean(axis = 1))
print(marks.mean(axis = 0))
print(marks.max())
print(marks[marks.mean(axis = 1) > 75])
print((marks[marks.mean(axis = 1) >= 50].size / marks.size) * 100)