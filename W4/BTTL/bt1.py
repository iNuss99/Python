# pyrefly: ignore[missing-import]
import numpy as np

import pandas as pd

# 1. Đọc file CSV
df = pd.read_csv("data.csv")
print("\ncau1\n")
print(df)

# 2. Hiển thị 5 dòng đầu, số dòng, số cột và kiểu dữ liệu
print("\ncau2\n")
print(df.head(5))
print(df.shape)
print(df.dtypes)

# 3. Kiểm tra dữ liệu thiếu
print("\ncau3\n")
print(df.isna().sum())

# 4. Chuẩn hóa tên sản phẩm và thành phố
print("\ncau4\n")
df["Product"] = df["Product"].str.strip()
df["City"] = df["City"].str.strip()
print(df["Product"])
print(df["City"])

# 5. Phát hiện số lượng không hợp lệ
print("\ncau5\n")
print(df[df["Quantity"] < 0])
print(df[df["Quantity"] > 100])
# Chuyen gia tri khong hop le ve NaN
df.loc[(df["Quantity"] < 0) | (df["Quantity"] > 100), "Quantity"] = np.nan

# 6. Xử lý dữ liệu thiếu
print("\ncau6\n")
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["UnitPrice"] = df["UnitPrice"].fillna(df["UnitPrice"].median())
print(df[["Quantity", "UnitPrice"]])

# 7. Tạo cột Revenue
print("\ncau7\n")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
print(df[["OrderID", "Product", "Quantity", "UnitPrice", "Revenue"]])

# 8. Tổng doanh thu theo sản phẩm
print("\ncau8\n")
total_revenue_by_product = df.groupby("Product")["Revenue"].sum()
print(total_revenue_by_product)

# 9. Doanh thu theo thành phố
print("\ncau9\n")
total_revenue_by_city = df.groupby("City")["Revenue"].sum()
print(total_revenue_by_city)

# 10. Sắp xếp doanh thu giảm dần
print("\ncau10\n")
print(total_revenue_by_product.sort_values(ascending=False))

# 11. Xuất dữ liệu đã xử lý
print("\ncau11\n")
df.to_csv(
    "sales_clean.csv",
    index=False,
    encoding="utf-8-sig"
)
print("Da xuat file sales_clean.csv thanh cong!")