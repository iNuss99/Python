
import numpy as np
# 2. Bài 2 — Lọc và đếm
# Cho mảng [35, 60, 75, 45, 90, 80, 50]. In ra các số từ 50 đến dưới 80, sau đó đếm số phần tử thỏa mãn điều kiện.
scores = np.array([35, 60, 75, 45, 90, 80, 50])

print(scores[(scores >= 50) & (scores < 80)])
print("So phan tu thoa man dieu kien:", np.sum((scores >= 50) & (scores < 80)))


