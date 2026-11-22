"""
CÂU 1 (2đ) - KHÁM PHÁ DỮ LIỆU
"""

import os
import pandas as pd

# Đường dẫn file dữ liệu
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "stationery_orders.csv")
df = pd.read_csv(DATA_PATH)

print("=" * 70)
print("CÂU 1: KHÁM PHÁ DỮ LIỆU")
print("=" * 70)

# 1. Đọc file, hiển thị 5 dòng đầu và 5 dòng cuối
print("\n--- 1. 5 DÒNG ĐẦU TIÊN ---")
print(df.head())

print("\n--- 5 DÒNG CUỐI CÙNG ---")
print(df.tail())

# 2. Cho biết số dòng, số cột, tên cột và kiểu dữ liệu của từng cột
print("\n--- 2. CẤU TRÚC DỮ LIỆU ---")
print(f"Số dòng: {df.shape[0]}, Số cột: {df.shape[1]}")
print("\nTên cột và kiểu dữ liệu:")
print(df.dtypes)

# 3. Thống kê số giá trị thiếu theo từng cột
print("\n--- 3. THỐNG KÊ GIÁ TRỊ THIẾU ---")
print(df.isnull().sum())

# 4. Đếm số dòng bị trùng lặp hoàn toàn và số OrderID bị lặp
print("\n--- 4. KIỂM TRA TRÙNG LẶP ---")
print(f"Số dòng bị trùng lặp hoàn toàn: {df.duplicated().sum()}")
print(f"Số OrderID bị lặp: {df['OrderID'].duplicated().sum()}")

# 5. Liệt kê các giá trị khác nhau của Product, Category, City và PaymentMethod kèm số lượng
print("\n--- 5. GIÁ TRỊ KHÁC NHAU CỦA CÁC CỘT ĐỊNH LOẠI ---")
for col in ["Product", "Category", "City", "PaymentMethod"]:
    print(f"\n[Cột {col}] ({df[col].nunique()} giá trị khác nhau):")
    print(df[col].value_counts(dropna=False))

print("\n" + "-" * 70)
print("NHẬN XÉT: VÌ SAO SỐ LƯỢNG GIÁ TRỊ KHÁC NHAU LỚN HƠN THỰC TẾ?")
print("""
1. Khoảng trắng thừa (leading/trailing spaces): '  Ballpoint Pen ', 'hai phong '.
2. Chữ hoa/thường không đồng nhất: 'notebook a5' vs 'Notebook A5', 'stationery' vs 'STATIONERY'.
3. Quy chuẩn viết tắt địa danh khác nhau: 'HCM', 'TP.HCM' vs 'Ho Chi Minh'; 'Hanoi' vs 'Ha Noi'.
=> Máy tính phân biệt theo mã ký tự nên các biến thể trên bị tính là các giá trị riêng biệt.
""")
print("=" * 70)

