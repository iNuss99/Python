# Bài 13. Tìm các giá trị duy nhất
# Cho mảng mã sản phẩm:
# products = np.array([101, 102, 101, 103, 102, 104, 101, 103])
# 1. Liệt kê các mã sản phẩm không trùng lặp.
# 2. Đếm số lần xuất hiện của từng mã.
# 3. Tìm mã xuất hiện nhiều lần nhất.
# 4. Gợi ý: np.unique(..., return_counts=True).

import numpy as np

products = np.array([101, 102, 101, 103, 102, 104, 101, 103])

unique, counts = np.unique(products, return_counts=True)

print("1. Ma duy nhat:", unique)
print("2. So lan xuat hien:", dict(zip(unique, counts)))

print("3. Ma nhieu nhat:", unique[np.argmax(counts)])