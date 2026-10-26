import numpy as np  
revenue = np.array([100, 120, 90, 150, 180, 160, 200])
print("16.1:", np.sum(revenue))
print("16.2:", np.cumsum(revenue))
print("16.3:", np.diff(revenue))
print("16.4:", np.argmax(revenue) + 1)