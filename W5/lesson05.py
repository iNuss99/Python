import pandas as pd
import numpy as np

# BÀI 1. KHÁM PHÁ DỮ LIỆU
df = pd.read_csv("sales_practice_dataset.csv", encoding="utf-8-sig")

print("5 dòng đầu")
print(df.head(5))
print("\n5 dòng cuối")
print(df.tail(5)) 

print("\n 2. Kích thước & Kiểu dữ liệu")
print("Kích thước (Shape):", df.shape)
print("Tên các cột:", df.columns.tolist())
print("Kiểu dữ liệu:\n", df.dtypes)

print("\n3. Số giá trị thiếu theo từng cột")
print(df.isna().sum())

for col in ["Product", "Category", "City"]:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

print("\n4. Danh sách các giá trị khác nhau")
print("Sản phẩm (Product):", df["Product"].unique())
print("Nhóm hàng (Category):", df["Category"].unique()) 
print("Thành phố (City):", df["City"].unique())


# BÀI 2. LÀM SẠCH DỮ LIỆU

print("\n6. Dòng thiếu Quantity hoặc UnitPrice")
missing_rows = df[df["Quantity"].isna() | df["UnitPrice"].isna()]
print(missing_rows)

print("\n7. Dòng có Quantity <= 0 hoặc UnitPrice <= 0")
invalid_rows = df[(df["Quantity"] <= 0) | (df["UnitPrice"] <= 0)]
print(invalid_rows)

clean_df = df.dropna(subset=["Quantity", "UnitPrice"]).copy()
clean_df = clean_df[(clean_df["Quantity"] > 0) & (clean_df["UnitPrice"] > 0)].copy()
print("\n--- 9. Kích thước clean_df ---", clean_df.shape)


# BÀI 3. PHÂN TÍCH NGOẠI LAI (OUTLIERS)
quantity = df["Quantity"].dropna()
Q1 = quantity.quantile(0.25)
Q3 = quantity.quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print(f"\n10. IQR Quantity ")
print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Ngưỡng dưới: {lower}, Ngưỡng trên: {upper}")

outlier_mask = (df["Quantity"] < lower) | (df["Quantity"] > upper)
print("\n11. Danh sách OrderID ngoại lai ")
print(df.loc[outlier_mask, ["OrderID", "Product", "Quantity"]])

mean_keep = clean_df["Quantity"].mean()
mean_remove = clean_df[clean_df["Quantity"] <= upper]["Quantity"].mean()
print(f"\n12. So sánh Quantity Trung Bình")
print(f"Giữ ngoại lai: {mean_keep:.2f}")
print(f"Loại ngoại lai: {mean_remove:.2f}")


encoded_df = pd.get_dummies(clean_df, columns=["Category", "City"], dtype=int)

print("\n--- 16. 5 dòng sau khi mã hóa ---")
print(encoded_df.head(5))


# BÀI 5. PHÂN TÍCH DOANH THU
clean_df["Revenue"] = clean_df["Quantity"] * clean_df["UnitPrice"]

print(f"\n19. Tổng doanh thu sạch: {clean_df['Revenue'].sum():,.0f} VNĐ ")

by_product = clean_df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\n 20. Doanh thu theo Sản phẩm \n", by_product)

by_city = clean_df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
print("\n21. Doanh thu theo Thành phố \n", by_city)

print(f"\n 22. Cao nhất ")
print(f"Sản phẩm cao nhất: {by_product.index[0]} ({by_product.iloc[0]:,.0f} VNĐ)")
print(f"Thành phố cao nhất: {by_city.index[0]} ({by_city.iloc[0]:,.0f} VNĐ)")

with pd.ExcelWriter("sales_report.xlsx", engine="openpyxl") as writer:
    clean_df.to_excel(writer, sheet_name="CleanData", index=False)
    by_product.to_frame("Revenue").to_excel(writer, sheet_name="ByProduct")
    by_city.to_frame("Revenue").to_excel(writer, sheet_name="ByCity")