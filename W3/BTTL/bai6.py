
# 6. Bài 6 — Xử lý điểm
# Cho mảng [45, 120, -5, 75, 95, 60]. Giới hạn điểm trong khoảng 0–100, làm tròn đến số nguyên nếu cần, rồi phân loại điểm từ 50 trở lên là Đạt, còn lại là Không đạt.
import numpy as np
scores = np.array([45, 120, -5, 75, 95, 60])
scores = np.clip(scores, 0, 100)
scores = np.round(scores).astype(int)

print("Mang sau khi xu ly:", scores)
print("Phan Loai Diem:")
for score in scores:
    if score >= 50:
        print(f"- {score}: dat")
    else:
        print(f"- {score}: Khong dat")