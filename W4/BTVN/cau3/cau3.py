"""
CÂU 3 (2đ) - PHÂN TÍCH NGOẠI LAI (OUTLIERS)
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
print("CÂU 3: PHÂN TÍCH NGOẠI LAI CHO BIẾN QUANTITY")
print("=" * 70)

# 1. Tính Q1, Q3, IQR và hai ngưỡng
q1 = clean_df["Quantity"].quantile(0.25)
q3 = clean_df["Quantity"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(f"1. Các ngưỡng xác định ngoại lai:")
print(f"   Q1 = {q1:.2f}, Q3 = {q3:.2f}, IQR = {iqr:.2f}")
print(f"   Ngưỡng dưới = {lower_bound:.2f}, Ngưỡng trên = {upper_bound:.2f}")

# 2. Liệt kê OrderID, Product và Quantity của các dòng bị đánh dấu ngoại lai
outliers = clean_df[clean_df["Quantity"] > upper_bound]
print(f"\n2. Danh sách {len(outliers)} đơn ngoại lai (Quantity > {upper_bound:.2f}):")
print(outliers[["OrderID", "Product", "Quantity", "UnitPrice", "Discount", "City"]].to_string(index=False))

# 3. Lập bảng so sánh trung bình, trung vị, giá trị lớn nhất và tổng Quantity khi giữ và khi loại ngoại lai
no_outliers = clean_df[clean_df["Quantity"] <= upper_bound]

comp = pd.DataFrame(
    {
        "Chỉ số": ["Trung bình (Mean)", "Trung vị (Median)", "Lớn nhất (Max)", "Tổng số lượng (Sum)"],
        "Khi GIỮ ngoại lai": [clean_df["Quantity"].mean(), clean_df["Quantity"].median(), clean_df["Quantity"].max(), clean_df["Quantity"].sum()],
        "Khi LOẠI ngoại lai": [no_outliers["Quantity"].mean(), no_outliers["Quantity"].median(), no_outliers["Quantity"].max(), no_outliers["Quantity"].sum()],
    }
)
comp["Thay đổi (%)"] = ((comp["Khi GIỮ ngoại lai"] - comp["Khi LOẠI ngoại lai"]) / comp["Khi LOẠI ngoại lai"] * 100).round(2)

print("\n3. Bảng so sánh các chỉ số thống kê:")
print(comp.to_string(index=False))
print("\n-> Chỉ số thay đổi nhiều nhất là: GIÁ TRỊ LỚN NHẤT (Max, +1233.33%), sau đó là Sum và Mean.")
print("-> TRUNG VỊ (Median) hoàn toàn không thay đổi (0.00%) vì có tính bền vững trước ngoại lai.")

# 4. Trả lời các câu hỏi nghiệp vụ
print("\n4. Trả lời câu hỏi nghiệp vụ:")
print("""
a) Các sản phẩm ngoại lai: Ballpoint Pen (120, 200 chiếc), Notebook A5 (80, 150 cuốn), Highlighter (60 chiếc), File Folder (70 chiếc).
b) Tính hợp lý: Rất hợp lý vì đây là văn phòng phẩm tiêu hao, khách hàng tổ chức/cơ quan thường mua sỉ theo lô (B2B) và đều được chiết khấu 15%.
c) Vì sao ngoại lai không đồng nghĩa với dữ liệu sai?
   Ngoại lai chỉ là điểm dị biệt về mặt toán học, nhưng lại phản ánh giao dịch mua sỉ thực tế hợp pháp.
d) Quyết định: GIỮ LẠI trong tập dữ liệu để phân tích đúng doanh thu và dòng tiền thực tế.
""")
print("=" * 70)

