# Cho mảng điểm:
# scores = np.array([45, 78, 90, 55, 62, 88, 35, 95, 70, 48])
# 1. Tính điểm trung bình.
# 2. Đếm số sinh viên đạt điểm từ 50 trở lên.
# 3. Lọc các điểm từ 80 trở lên.
# 4. Tìm điểm cao nhất và thấp nhất.
# 5. Tính tỷ lệ phần trăm sinh viên đạt điểm từ 50 trở lên

import numpy as np
scores = np.array([45, 78, 90, 55, 62, 88, 35, 95, 70, 48])
print("Diem trung binh:", np.mean(scores))
print("So sinh vien dat diem tu 50 tro len:", np.sum(scores >= 50))
print("Cac diem tu 80 tro len:", scores[scores >= 80])  
print("Diem cao nhat:", np.max(scores))
print("Diem thap nhat:", np.min(scores))
print("Ty le phan tram sinh vien dat diem tu 50 tro len:", (np.sum(scores >= 50) / len(scores)) * 100, "%")
