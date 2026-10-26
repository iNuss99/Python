from collections import Counter
# 3. Bài 3 — Thống kê phần tử
# Cho mảng [10, 20, 10, 30, 20, 10, 40]. Tìm các giá trị duy nhất và số lần xuất hiện của từng giá trị.

arr = [10, 20, 10, 30, 20, 10, 40]
counts = Counter(arr)

for value, count in counts.items():
    print(f"Giá trị {value}: xuất hiện {count} lần")