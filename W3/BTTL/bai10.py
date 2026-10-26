# Bài 10. Kiểm tra điều kiện
# Cho mảng:
# arr = np.array([12, 18, 25, 30, 42, 55])
# 1. Kiểm tra tất cả phần tử có lớn hơn 10 hay không.
# 2. Kiểm tra có phần tử nào lớn hơn 50 hay không.
# 3. Kiểm tra tất cả phần tử có nằm trong khoảng từ 10 đến 60 hay không.
# 4. Gợi ý: np.all(), np.any()

import numpy as np
arr = np.array([12, 18, 25, 30, 42, 55])
print("Tat ca phan tu lon hon 10:", np.all(arr > 10))
print("Co phan tu nao lon hon 50:", np.any(arr > 50))
print("Tat ca phan tu nam trong khoang tu 10 den 60:", np.all((arr >= 10) & (arr <= 60)))

                