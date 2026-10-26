# Bài 11. Lọc số chẵn và số lẻ
# Cho mảng:
# arr = np.array([12, 7, 24, 31, 46, 53, 60, 75])
# 1. Tạo mảng chỉ chứa số chẵn.
# 2. Tạo mảng chỉ chứa số lẻ.
# 3. Đếm số lượng số chẵn và số lượng số lẻ.

import numpy as np
arr = np.array([12, 7, 24, 31, 46, 53, 60, 75]) 
print("Mang chi chua so chan:", arr[arr % 2 == 0])
print("Mang chi chua so le:", arr[arr % 2 != 0])
print("So luong so chan:", np.sum(arr % 2 == 0))
print("So luong so le:", np.sum(arr % 2 != 0))
