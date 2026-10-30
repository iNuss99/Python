import os
import sys
import numpy as np
import pandas as pd

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = "sales_practice_dataset.csv"
if not os.path.exists(csv_file):
    csv_file = os.path.join(base_dir, "sales_practice_dataset.csv")

# Bài 1. Khám phá dữ liệu

df = pd.read_csv(csv_file, encoding="utf-8-sig")
print("=== Câu 10 ===")
print("5 dòng đầu:")
print(df.head(5))
print("\n5 dòng cuối:")
print(df.tail(5))

print("\n=== Câu 11 ===")
print("Kích thước (Shape):", df.shape)
print("Số dòng:", df.shape[0])
print("Số cột:", df.shape[1])
print("Tên các cột:", df.columns.tolist())
print("Kiểu dữ liệu:")
print(df.dtypes)

print("\n=== Câu 12 ===")
print("Số giá trị thiếu theo từng cột:")
print(df.isna().sum())

print("\n=== Câu 13 ===")
print("Sản phẩm (Product):", df["Product"].dropna().unique().tolist())
print("Nhóm hàng (Category):", df["Category"].dropna().unique().tolist())
print("Thành phố (City):", df["City"].dropna().unique().tolist())


# Bài 2. Làm sạch dữ liệu

for col in ["Product", "Category", "City"]:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()
print("\n=== Câu 14 ===")
print("Đã chuẩn hóa str.strip() cho Product, Category, City.")

print("\n=== Câu 15 ===")
missing_rows = df[df["Quantity"].isna() | df["UnitPrice"].isna()]
print("Các dòng thiếu Quantity hoặc UnitPrice:")
print(missing_rows)

print("\n=== Câu 16 ===")
invalid_rows = df[(df["Quantity"] <= 0) | (df["UnitPrice"] <= 0)]
print("Các dòng có Quantity <= 0 hoặc UnitPrice <= 0:")
print(invalid_rows)

print("\n=== Câu 17 ===")
print("""Đề xuất xử lý:
- Dòng thiếu Quantity (O011) hoặc thiếu UnitPrice (O012): Loại bỏ (drop) khỏi tập phân tích doanh thu.
  Giải thích: Doanh thu = Quantity * UnitPrice, thiếu 1 trong 2 thông tin cốt lõi này sẽ không thể tính chính xác doanh thu.
  Việc tự ý điền trung bình/trung vị có thể làm sai lệch dữ liệu tài chính.
- Dòng có Quantity <= 0 (O013 có Quantity = -1.0) hoặc UnitPrice <= 0: Loại bỏ (drop).
  Giải thích: Trong giao dịch bán hàng thương mại, số lượng và đơn giá phải là số dương (> 0).
  Giá trị <= 0 là dữ liệu bất thường hoặc nhập sai.""")

clean_df = df.dropna(subset=["Quantity", "UnitPrice"]).copy()
clean_df = clean_df[(clean_df["Quantity"] > 0) & (clean_df["UnitPrice"] > 0)].copy()
print("\n=== Câu 18 ===")
print(f"Kích thước clean_df: {clean_df.shape} (Dữ liệu gốc df vẫn giữ nguyên: {df.shape})")


# Bài 3. Phân tích ngoại lai

quantity = df["Quantity"].dropna()
Q1 = quantity.quantile(0.25)
Q3 = quantity.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print("\n=== Câu 19 ===")
print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Ngưỡng dưới: {lower_bound}, Ngưỡng trên: {upper_bound}")

outlier_mask = (df["Quantity"] < lower_bound) | (df["Quantity"] > upper_bound)
print("\n=== Câu 20 ===")
print("Các đơn hàng bị đánh dấu ngoại lai:")
print(df.loc[outlier_mask, ["OrderID", "Product", "Category", "Quantity", "UnitPrice", "City"]])

mean_keep = clean_df["Quantity"].mean()
mean_remove = clean_df[clean_df["Quantity"] <= upper_bound]["Quantity"].mean()
print("\n=== Câu 21 ===")
print(f"Số lượng bán trung bình khi GIỮ ngoại lai:     {mean_keep:.2f}")
print(f"Số lượng bán trung bình khi LOẠI BỎ ngoại lai: {mean_remove:.2f}")

print("\n=== Câu 22 ===")
print("""Giải thích:
- Ngoại lai (Outlier) là giá trị cách biệt rất xa so với số đông, nhưng vẫn có thể là giao dịch thực tế
  (ví dụ đơn hàng O016 mua 150 chiếc Webcam là đơn mua buôn/sỉ của khách hàng doanh nghiệp).
- Dữ liệu sai là dữ liệu vi phạm logic hoặc lỗi nhập liệu (ví dụ số lượng âm, sai định dạng).
- Vì vậy, ngoại lai phản ánh hành vi mua hàng quy mô lớn thực tế, không đồng nghĩa với dữ liệu sai.""")


# Bài 4. Mã hóa dữ liệu

encoded_category = pd.get_dummies(clean_df["Category"], prefix="Category", dtype=int)
print("\n=== Câu 23 ===")
print("Mã hóa Category:")
print(encoded_category.head())

encoded_city = pd.get_dummies(clean_df["City"], prefix="City", dtype=int)
print("\n=== Câu 24 ===")
print("Mã hóa City:")
print(encoded_city.head())

encoded_df = pd.get_dummies(clean_df, columns=["Category", "City"], dtype=int)
print("\n=== Câu 25 ===")
print("5 dòng sau mã hóa:")
print(encoded_df.head(5))
print("""Giải thích các cột 0/1:
- Giá trị 1: Dòng dữ liệu thuộc về danh mục đó.
- Giá trị 0: Dòng dữ liệu không thuộc về danh mục đó.
- Ví dụ: Dòng đầu tiên (O001) có City là 'Ho Chi Minh City' nên cột City_Ho Chi Minh City mang giá trị 1,
  các cột thành phố khác mang giá trị 0.""")

print("\n=== Câu 26 ===")
print("""Giải thích:
- Category là biến định danh danh nghĩa (Nominal), các nhóm bình đẳng, không có thứ bậc hơn kém tự nhiên.
- Nếu gán số tùy ý (ví dụ Accessories = 1, Electronics = 2), các mô hình học máy và thuật toán tính toán
  sẽ hiểu nhầm rằng Electronics lớn gấp đôi Accessories (2 > 1), tạo ra mối quan hệ thứ bậc giả mạo.
- Do đó, phương pháp One-Hot Encoding (pd.get_dummies) là chuẩn xác nhất.""")


# Bài 5. Phân tích doanh thu

clean_df["Revenue"] = clean_df["Quantity"] * clean_df["UnitPrice"]
print("\n=== Câu 27 ===")
print("Đã tạo cột Revenue (5 dòng đầu):")
print(clean_df[["OrderID", "Product", "Quantity", "UnitPrice", "Revenue"]].head(5))

total_revenue = clean_df["Revenue"].sum()
print("\n=== Câu 28 ===")
print(f"Tổng doanh thu trên dữ liệu đã làm sạch: {total_revenue:,.0f} VNĐ")

by_product = clean_df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\n=== Câu 29 ===")
print("Doanh thu theo Sản phẩm (giảm dần):")
print(by_product.apply(lambda x: f"{x:,.0f} VNĐ"))

by_city = clean_df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
print("\n=== Câu 30 ===")
print("Doanh thu theo Thành phố (giảm dần):")
print(by_city.apply(lambda x: f"{x:,.0f} VNĐ"))

print("\n=== Câu 31 ===")
print(f"Sản phẩm cao nhất: {by_product.index[0]} ({by_product.iloc[0]:,.0f} VNĐ)")
print(f"Thành phố cao nhất: {by_city.index[0]} ({by_city.iloc[0]:,.0f} VNĐ)")

print("\n=== Câu 32 ===")
print("""3-5 Nhận xét dựa trên kết quả:
1. Webcam dẫn đầu doanh thu (136,170,000 VNĐ, chiếm hơn 50% tổng doanh thu), chủ yếu nhờ vào đơn hàng sỉ O016 (150 chiếc).
2. Laptop đứng thứ 2 về doanh thu (74,700,000 VNĐ) nhờ đơn giá cao nhất trong các sản phẩm.
3. Hanoi là thị trường đóng góp doanh thu lớn nhất (172,850,000 VNĐ, chiếm ~64%), theo sau là TP. Hồ Chí Minh (56,720,000 VNĐ).
4. Dữ liệu ban đầu có 3/20 đơn lỗi (15%), cần bổ sung kiểm tra hợp lệ dữ liệu (validation) khi nhập liệu hệ thống.
5. Đơn hàng ngoại lai O016 có ảnh hưởng rất lớn đến trung bình và tổng doanh thu, doanh nghiệp nên phân loại đơn bán lẻ và bán buôn.""")

clean_csv_path = os.path.join(base_dir, "sales_clean.csv")
report_xlsx_path = os.path.join(base_dir, "sales_report.xlsx")

clean_df.to_csv(clean_csv_path, index=False, encoding="utf-8-sig")
with pd.ExcelWriter(report_xlsx_path, engine="openpyxl") as writer:
    clean_df.to_excel(writer, sheet_name="CleanData", index=False)
    by_product.to_frame("Revenue").to_excel(writer, sheet_name="ByProduct")
    by_city.to_frame("Revenue").to_excel(writer, sheet_name="ByCity")

print("\n" + "=" * 80)
print("XUẤT SẢN PHẨM NỘP BÀI THÀNH CÔNG:")
print(f"1. File dữ liệu sau làm sạch: {clean_csv_path}")
print(f"2. File báo cáo Excel:         {report_xlsx_path}")
print("=" * 80)
