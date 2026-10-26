# Bài 7. Đảo ngược mảng
# Cho mảng:
# arr = np.array([12, 25, 38, 41, 56, 69])
# 1. In mảng theo thứ tự ngược lại.
# 2. In 3 phần tử cuối theo thứ tự ban đầu.
# 3. In các phần tử ở vị trí chẵn (index chẵn).

import numpy as np
scores = np.array([12, 25, 38, 41, 56, 69])
print("Mang dao nguoc:", scores[::-1])
print("3 phan tu cuoi theo thu tu ban dau:", scores[-3:])
print("Cac phan tu o vi tri chan:", scores[::2])