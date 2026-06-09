import numpy as np
marks = np.array([45, 78, 92, 30, 67, 55, 88, 23, 99])
print(marks.mean())
print(marks[marks >= 40])
print(marks[marks < 40].size)
marks = marks + 5
marks[marks > 100] = 100
print(marks)