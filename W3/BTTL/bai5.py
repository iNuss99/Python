
# 5. Bài 5 — Phân tích doanh thu
# Doanh thu trong 5 ngày là [100, 150, 120, 200, 180]. Tính tổng doanh thu, doanh thu lũy kế, và mức tăng hoặc giảm giữa hai ngày liên tiếp.

import numpy as np

arr = np.array([100, 150, 120, 200, 180])
print("Tong doanh thu:", np.sum(arr))
print("Doanh thu luy ke:", np.cumsum(arr))
print("Muc tang giam giua hai ngay lien tiep:", np.diff(arr))
