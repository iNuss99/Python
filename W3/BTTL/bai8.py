# Bài 8. Thay thế các phần tử
# Cho mảng:
# arr = np.array([10, 25, 30, 45, 50, 65, 70])
# 1. Thay các phần tử nhỏ hơn 30 bằng 0.
# 2. Thay các phần tử lớn hơn 60 bằng 100.
# # 3. In mảng sau khi cập nhật.

import numpy as np
arr = np.array([10, 25, 30, 45, 50, 65, 70])
arr[arr < 30] = 0
arr[arr > 60] = 100
print("Mang sau khi cap nhat:", arr)
