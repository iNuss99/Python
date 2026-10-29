import numpy as np

arr = np.array([31, 27, 34, 29, 26, 33, 30])

tang_dan = np.sort(arr)
giam_dan = np. sort(arr)[:: -1]

max_idx = np.argmax(arr)
min_idx = np.argmin(arr)

print("mang ban dau:", arr )
print("Mang tang dan:", tang_dan)
print("Mang giam dan:", giam_dan)
print("Cao nhat:", arr[max_idx],"tai vi tri:",max_idx)
print("Thap nhat:", arr[min_idx],"tai vi tri:",min_idx)