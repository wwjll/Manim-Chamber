import numpy as np
a = np.array([0,0,0])
b = np.array([1, 1, 0])
c = np.array([0, -1, 0])
d = np.array([1, 0, 0])
ab = b-a
cd = d-c
print(ab, cd[1], ab*cd)