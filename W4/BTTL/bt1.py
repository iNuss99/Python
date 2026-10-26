# pyrefly: ignore[missing-import]
import numpy as np
import pandas as pd

# 1. Doc file CSV bằng pd.read_csv()
df = pd.read_csv("data.csv", encoding="utf-8")

# 2. Hien thi 5 dong dau, kiem tra so dong, so cot va kieu du lieu
print("=== YEU CAU 2 ===")
print("--- 5 dong dau ---")
print(df.head())

print(f"\nSo dong: {df.shape[0]}, So cot: {df.shape[1]}")

print("\n--- Kieu du lieu cua tung cot ---")
print(df.dtypes)

# 3. Kiem tra du lieu thieu trong tung cot
print("\n=== YEU CAU 3 ===")
print("--- So luong gia tri thieu (NaN) trong tung cot ---")
print(df.isna().sum())

# 4. Chuan hoa ten san pham va thanh pho bang str.strip()
df["Product"] = df["Product"].astype(str).str.strip()
df["City"] = df["City"].astype(str).str.strip()
print("\n=== YEU CAU 4 ===")
print("Da chuan hoa khoang trang thua o cot Product va City.")

# 5. Phat hien so luong ban khong hop le (am hoac > 100)
print("\n=== YEU CAU 5 ===")
invalid_quantity = df[(df["Quantity"] < 0) | (df["Quantity"] > 100)]
print("--- Danh sach dong co Quantity khong hop le ---")
print(invalid_quantity)

# 6. Xu ly du lieu thieu trong Quantity va UnitPrice
# Giai thich:
# - Chuyen cac gia tri bat thuong (Quantity < 0, Quantity > 100, UnitPrice <= 0) ve NaN.
# - Dien NaN bang trung vi (median) cua tung san pham de tranh bi anh huong boi outlier.
# ---------------------------------------------------------
df.loc[(df["Quantity"] < 0) | (df["Quantity"] > 100), "Quantity"] = np.nan
df.loc[df["UnitPrice"] <= 0, "UnitPrice"] = np.nan

df["Quantity"] = df.groupby("Product")["Quantity"].transform(
    lambda x: x.fillna(x.median())
)
df["UnitPrice"] = df.groupby("Product")["UnitPrice"].transform(
    lambda x: x.fillna(x.median())
)

# Gan lai df thay vi dung inplace=True de tranh Pandas Warning
df = df.dropna(subset=["Quantity", "UnitPrice"])

print("\n=== YEU CAU 6 ===")
print("--- Kiem tra lai gia tri thieu sau khi xu ly ---")
print(df.isna().sum())

# 7. Tao cot Revenue = Quantity * UnitPrice
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
print("\n=== YEU CAU 7 ===")
print("--- 5 dong dau sau khi them cot Revenue ---")
print(df.head())

# 8. Tinh tong doanh thu theo tung san pham
df_product_revenue = (
    df.groupby("Product")["Revenue"].sum().reset_index(name="Total_Revenue")
)
print("\n=== YEU CAU 8 ===")
print("--- Tong doanh thu theo san pham ---")
print(df_product_revenue)

# 9. Thong ke doanh thu theo tung thanh pho
df_city_revenue = (
    df.groupby("City")["Revenue"].sum().reset_index(name="Total_Revenue")
)
print("\n=== YEU CAU 9 ===")
print("--- Thong ke doanh thu theo thanh pho ---")
print(df_city_revenue)

# 10. Sap xep san pham theo doanh thu giam dan
df_product_sorted = df_product_revenue.sort_values(
    by="Total_Revenue", ascending=False
)
print("\n=== YEU CAU 10 ===")
print("--- Danh sach san pham sap xep theo doanh thu giam dan ---")
print(df_product_sorted)

# 11. Xuat du lieu da xu ly ra file sales_clean.csv
df.to_csv("sales_clean.csv", index=False, encoding="utf-8")
print("\n=== YEU CAU 11 ===")
print("Da xuat file sales_clean.csv thanh cong!")