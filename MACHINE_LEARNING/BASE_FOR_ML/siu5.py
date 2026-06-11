import numpy as np
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
r1 = arr[0,:].sum()
r2 = arr[1,:].sum()
r3 = arr[2,:].sum()
print(r1, r2, r3)
c1 = arr[:,0].sum()
c2 = arr[:,1].sum()
c3 = arr[:,2].sum()
print(c1, c2, c3)
