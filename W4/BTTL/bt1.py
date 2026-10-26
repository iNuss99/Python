# Bài tập: Phân tích dữ liệu bán hàng bằng Pandas
# Yêu cầu sinh viên sử dụng file CSV trên để thực hiện:
# 1. Đọc file CSV bằng pd.read_csv().
# 2. Hiển thị 5 dòng đầu, kiểm tra số dòng, số cột và kiểu dữ liệu.
# 3. Kiểm tra dữ liệu thiếu trong từng cột.
# 4. Chuẩn hóa tên sản phẩm và thành phố bằng str.strip().
# 5. Phát hiện số lượng bán không hợp lệ, chẳng hạn số lượng âm hoặc bất thường.
# 6. Xử lý dữ liệu thiếu trong Quantity và UnitPrice, giải thích cách lựa chọn.
# 7. Tạo cột Revenue = Quantity * UnitPrice.
# 8. Tính tổng doanh thu theo từng sản phẩm.
# 9. Thống kê doanh thu theo từng thành phố.
# 10. Sắp xếp sản phẩm theo doanh thu giảm dần.
# 11. Xuất dữ liệu đã xử lý ra file sales_clean.csv.

import pandas as pd
# pyrefly: ignore[missing-import]
import numpy as np
# 1
df = pd.read_csv("data.csv", encoding = "utf-8")
# 2
print(df.head())
print(df.tail())
print(df.columns)
print(df.dtypes)
#3
print("So dong bi thieu: ",df.isna().sum().sum())

#4
df["Product"] = df["Product"].str.strip()
df["City"] = df["City"].str.strip()
print(df)

#5
invalid_quanity = df[(df["Quantity"] < 0)|(df["Quantity"] > 100)]
print(invalid_quanity)

#6
df.loc[(df["Quantity"] < 0)|(df["Quantity"] > 100), "Quantity"] = np.nan
df.loc[(df["UnitPrice"] < 0)|(df["UnitPrice"] > 100), "UnitPrice"] = np.nan
print(df.isna().sum())

#7
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
print(df)

#8
df_product = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print(df_product)

#9
df_city = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
print(df_city)

#10
df_sorted = df.sort_values(by="Revenue", ascending=False)
print(df_sorted)

#11
df.to_csv("sales_clean.csv", index=False, encoding="utf-8")
