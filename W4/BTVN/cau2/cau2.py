"""
CÂU 2 (2đ) - LÀM SẠCH DỮ LIỆU
"""

import os
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "stationery_orders.csv")
df = pd.read_csv(DATA_PATH)

print("=" * 70)
print("CÂU 2: LÀM SẠCH DỮ LIỆU")
print("=" * 70)

# 1. Chuẩn hóa Product, Category, City và PaymentMethod
clean_df = df.copy()

for col in ["Product", "Category", "PaymentMethod"]:
    clean_df[col] = clean_df[col].astype(str).str.strip().str.title()

clean_df["City"] = clean_df["City"].fillna("Unknown").astype(str).str.strip().str.title()
city_map = {
    "Hcm": "Ho Chi Minh",
    "Tp.Hcm": "Ho Chi Minh",
    "Hanoi": "Ha Noi",
    "Danang": "Da Nang",
    "Nan": "Unknown",
}
clean_df["City"] = clean_df["City"].replace(city_map)
print("\n1. Đã chuẩn hóa khoảng trắng, chữ hoa/thường và ánh xạ tên thành phố:")
print(f"   Các thành phố: {clean_df['City'].unique().tolist()}")

# 2. Tìm các dòng thiếu Quantity hoặc UnitPrice; tìm các dòng thiếu City hoặc Discount
missing_qty_price = clean_df[clean_df["Quantity"].isna() | clean_df["UnitPrice"].isna()]
missing_city_disc = df[df["City"].isna() | df["Discount"].isna()]
print(f"\n2. Số dòng thiếu Quantity hoặc UnitPrice: {len(missing_qty_price)} dòng")
print(f"   Số dòng thiếu City hoặc Discount:        {len(missing_city_disc)} dòng")

# 3. Tìm các dòng có Quantity <= 0 và UnitPrice <= 0
invalid_rows = clean_df[(clean_df["Quantity"] <= 0) | (clean_df["UnitPrice"] <= 0)]
print(f"\n3. Số dòng có Quantity <= 0 hoặc UnitPrice <= 0: {len(invalid_rows)} dòng")

# 4. Đề xuất cách xử lý từng trường hợp và giải thích lý do
print("\n4. Đề xuất phương án xử lý:")
print("""
   - Dòng trùng lặp hoàn toàn (4 dòng): Dùng drop_duplicates() để loại bỏ vì là lỗi lặp bản ghi.
   - Thiếu Discount (3 dòng): Điền 0.0 vì không có chiết khấu nghĩa là bán đúng giá gốc (0%).
   - Thiếu City (2 dòng): Điền 'Unknown' để bảo toàn doanh số thực của đơn hàng.
   - Thiếu hoặc <= 0 ở Quantity/UnitPrice: Loại bỏ các dòng này vì Quantity và UnitPrice là cốt lõi để tính Revenue, giá trị <= 0 hoặc NaN vi phạm logic kinh tế.
""")

# 5. Tạo clean_df, không ghi đè dữ liệu gốc; chuyển OrderDate sang kiểu ngày. In số dòng trước và sau
clean_df["Discount"] = clean_df["Discount"].fillna(0.0)
clean_df = clean_df.drop_duplicates()
clean_df = clean_df.dropna(subset=["Quantity", "UnitPrice"])
clean_df = clean_df[(clean_df["Quantity"] > 0) & (clean_df["UnitPrice"] > 0)]
clean_df["OrderDate"] = pd.to_datetime(clean_df["OrderDate"])
clean_df = clean_df.reset_index(drop=True)

print(f"5. Số dòng trước khi làm sạch: {len(df)}")
print(f"   Số dòng sau khi làm sạch:   {len(clean_df)}")
print(f"   Số dòng đã loại bỏ:         {len(df) - len(clean_df)}")

# Xuất file csv sạch
out_csv = os.path.join(os.path.dirname(__file__), "..", "stationery_clean.csv")
clean_df.to_csv(out_csv, index=False, encoding="utf-8-sig")
print(f"   -> Đã lưu dữ liệu sạch vào: {os.path.abspath(out_csv)}")
print("=" * 70)

