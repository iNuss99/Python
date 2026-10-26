# Bài 9. Tìm vị trí phần tử
# Cho mảng:
# arr = np.array([15, 30, 45, 30, 60, 30, 75])
# 1. Tìm vị trí xuất hiện đầu tiên của giá trị 30.
# 2. Tìm tất cả vị trí xuất hiện của giá trị 30.
# 3. Đếm số lần xuất hiện của giá trị 30.

import numpy as np
arr = np.array([15, 30, 45, 30, 60, 30, 75])
print("Vi tri xuat hien dau tien cua gia tri 30:", np.where(arr == 30)[0][0])
print("Tat ca vi tri xuat hien cua gia tri 30:", np.where(arr == 30)[0])
print("So lan xuat hien cua gia tri 30:", np.sum(arr == 30))
