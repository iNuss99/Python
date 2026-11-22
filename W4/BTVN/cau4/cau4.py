"""
CÂU 4 (2đ) - MÃ HÓA DỮ LIỆU (ONE-HOT ENCODING)
"""

import os
import pandas as pd


def get_clean_data():
    clean_path = os.path.join(os.path.dirname(__file__), "..", "stationery_clean.csv")
    if os.path.exists(clean_path):
        return pd.read_csv(clean_path)

    raw_path = os.path.join(os.path.dirname(__file__), "..", "stationery_orders.csv")
    df = pd.read_csv(raw_path)
    for c in ["Product", "Category", "PaymentMethod"]:
        df[c] = df[c].astype(str).str.strip().str.title()
    df["City"] = df["City"].fillna("Unknown").astype(str).str.strip().str.title()
    df["City"] = df["City"].replace(
        {"Hcm": "Ho Chi Minh", "Tp.Hcm": "Ho Chi Minh", "Hanoi": "Ha Noi", "Danang": "Da Nang", "Nan": "Unknown"}
    )
    df["Discount"] = df["Discount"].fillna(0.0)
    df = df.drop_duplicates().dropna(subset=["Quantity", "UnitPrice"])
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
    return df.reset_index(drop=True)


clean_df = get_clean_data()

print("=" * 70)
print("CÂU 4: MÃ HÓA DỮ LIỆU (ONE-HOT ENCODING)")
print("=" * 70)

# 1. Mã hóa Category bằng pd.get_dummies() (dùng dtype=int để hiển thị 0/1)
cat_dummies = pd.get_dummies(clean_df["Category"], prefix="Category", dtype=int)
print("1. Các cột sinh ra từ Category:")
print(cat_dummies.columns.tolist())

# 2. Mã hóa PaymentMethod bằng pd.get_dummies()
pm_dummies = pd.get_dummies(clean_df["PaymentMethod"], prefix="PaymentMethod", dtype=int)
print("\n2. Các cột sinh ra từ PaymentMethod:")
print(pm_dummies.columns.tolist())

# Ghép vào DataFrame
encoded_df = pd.concat([clean_df[["OrderID", "Category", "PaymentMethod"]], cat_dummies, pm_dummies], axis=1)

# 3. In 5 dòng sau mã hóa và giải thích ý nghĩa các cột 0/1
print("\n3. Năm dòng đầu sau khi mã hóa:")
print(encoded_df.head())

print("\n--- GIẢI THÍCH Ý NGHĨA CÁC CỘT 0/1 ---")
print("- Số 1: Đơn hàng thuộc danh mục hoặc hình thức thanh toán của cột đó.")
print("- Số 0: Đơn hàng không thuộc danh mục hoặc hình thức thanh toán đó.")
print(
    f"- Trong mỗi nhóm cột, mỗi dòng có chính xác: "
    f"Category={cat_dummies.sum(axis=1).unique().tolist()} số 1, "
    f"PaymentMethod={pm_dummies.sum(axis=1).unique().tolist()} số 1."
)
print("  LÝ DO: Category và PaymentMethod là các biến loại trừ lẫn nhau (mutually exclusive); một đơn hàng chỉ thuộc đúng 1 ngành hàng và 1 phương thức thanh toán tại thời điểm mua.")

# 4. Giải thích vì sao không nên gán Stationery = 1, Books = 2, Office Supplies = 3, Art Supplies = 4
print("\n4. VÌ SAO KHÔNG NÊN GÁN SỐ NGUYÊN (1, 2, 3, 4) CHO CATEGORY?")
print("""
1. Category là biến định danh (Nominal Variable): Giữa các danh mục không có thứ bậc ưu tiên hay quan hệ lớn nhỏ.
2. Gây hiểu sai cho mô hình Machine Learning:
   - Gán 1, 2, 3, 4 sẽ tạo ra một thứ tự giả mạo (ví dụ hiểu nhầm Art Supplies > Stationery).
   - Mô hình tuyến tính/khoảng cách sẽ hiểu sai khoảng cách toán học giữa các nhóm.
=> Dùng One-Hot Encoding giúp mọi danh mục độc lập và công bằng.
""")
print("=" * 70)

