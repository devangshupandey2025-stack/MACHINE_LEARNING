import numpy as np

marks = np.array([
    [78, 85, 90, 67, 88],
    [45, 56, 62, 48, 51],
    [92, 88, 95, 91, 89],
    [34, 40, 29, 45, 38],
    [67, 72, 70, 68, 74],
    [81, 79, 85, 88, 90],
    [55, 60, 58, 62, 57],
    [99, 97, 100, 98, 96],
    [23, 35, 30, 28, 25],
    [73, 75, 78, 80, 77],
    [64, 66, 68, 70, 72],
    [87, 89, 85, 90, 92],
    [41, 38, 45, 42, 40],
    [58, 62, 60, 64, 59],
    [95, 94, 96, 98, 97]
])

print(marks.shape)
print(marks.size)
print(marks.ndim)
print(marks.max())
print(marks.min())
print(marks.mean())

print(marks.sum(axis = 1))
print(marks.mean(axis = 1))
print(marks.max(axis = 1))
