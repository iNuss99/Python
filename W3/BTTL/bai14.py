import numpy as np
arr = np.array([12, 25, 37, 48, 59, 72, 85])
idx_50 = np.argmin(np.abs(arr - 50))
idx_70 = np.argmin(np.abs(arr - 70))
print("14.1:", arr[idx_50], "vi tri:", idx_50)
print("14.2:", arr[idx_70], "vi tri:", idx_70)