import numpy as np
scores = np.array([35, 72, 48, 90, 65, 20, 88])
print(scores[scores > 60])
print(scores[scores > 60].size)
scores[scores < 40] = 40
print(scores)