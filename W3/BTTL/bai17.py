import numpy as np
arr = np.array([20, 40, 60, 80, 100])
xmin, xmax = np.min(arr), np.max(arr)
normalized = (arr - xmin) / (xmax - xmin)
print("17.1:", xmin, xmax)
print("17.3:", normalized)