import numpy as np
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([30, 40, 50, 60])
merged = np.concatenate((arr1, arr2))
intersect = np.intersect1d(arr1, arr2)
union_sorted = np.sort(np.union1d(arr1, arr2))
print("15.1:", merged)
print("15.2:", intersect)
print("15.3 & 15.4:", union_sorted)