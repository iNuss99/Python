"""
CÂU 5 (2đ) - PHÂN TÍCH DOANH THU & XUẤT BÁO CÁO EXCEL
"""

import os
import pandas as pd


def get_clean_data():
    clean_path = os.path.join(os.path.dirname(__file__), "..", "stationery_clean.csv")
    if os.path.exists(clean_path):
        df = pd.read_csv(clean_path)
        df["OrderDate"] = pd.to_datetime(df["OrderDate"])
        return df

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
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    return df.reset_index(drop=True)


clean_df = get_clean_data()

print("=" * 70)
print("CÂU 5: PHÂN TÍCH DOANH THU")
print("=" * 70)

# 1. Tạo cột Revenue = Quantity * UnitPrice * (1 - Discount)
clean_df["Revenue"] = clean_df["Quantity"] * clean_df["UnitPrice"] * (1 - clean_df["Discount"])
print("1. Đã tạo cột Revenue. Năm dòng đầu:")
print(clean_df[["OrderID", "Product", "Quantity", "UnitPrice", "Discount", "Revenue"]].head())

# 2. Tính tổng doanh thu trên clean_df, sau đó tính lại khi loại ngoại lai ở Câu 3. Chênh lệch bao nhiêu %?
q1 = clean_df["Quantity"].quantile(0.25)
q3 = clean_df["Quantity"].quantile(0.75)
upper_bound = q3 + 1.5 * (q3 - q1)

rev_all = clean_df["Revenue"].sum()
rev_no_outliers = clean_df[clean_df["Quantity"] <= upper_bound]["Revenue"].sum()
diff_pct = ((rev_all - rev_no_outliers) / rev_no_outliers) * 100

print(f"\n2. Tổng doanh thu trên clean_df:          {rev_all:>14,.0f} VNĐ")
print(f"   Tổng doanh thu khi LOẠI ngoại lai:     {rev_no_outliers:>14,.0f} VNĐ")
print(f"   Chênh lệch:                            {diff_pct:>14.2f} %")

# 3. Tính doanh thu theo Product (sắp xếp giảm dần) và theo City
rev_by_product = (
    clean_df.groupby("Product")["Revenue"]
    .sum()
    .reset_index()
    .sort_values(by="Revenue", ascending=False)
)
rev_by_city = (
    clean_df.groupby("City")["Revenue"]
    .sum()
    .reset_index()
    .sort_values(by="Revenue", ascending=False)
)

print("\n3. Doanh thu theo sản phẩm (sắp xếp giảm dần):")
print(rev_by_product.to_string(index=False, formatters={"Revenue": "{:,.0f} đ".format}))

print("\n   Doanh thu theo thành phố:")
print(rev_by_city.to_string(index=False, formatters={"Revenue": "{:,.0f} đ".format}))

# 4. Tính doanh thu theo tháng dựa trên OrderDate
clean_df["Month"] = clean_df["OrderDate"].dt.to_period("M").astype(str)
rev_by_month = (
    clean_df.groupby("Month")["Revenue"]
    .sum()
    .reset_index()
    .sort_values(by="Month")
)
print("\n4. Doanh thu theo tháng:")
print(rev_by_month.to_string(index=False, formatters={"Revenue": "{:,.0f} đ".format}))

# 5. Tìm sản phẩm, thành phố và tháng có doanh thu cao nhất
top_prod = rev_by_product.iloc[0]
top_city = rev_by_city.iloc[0]
top_month = rev_by_month.sort_values(by="Revenue", ascending=False).iloc[0]

print(f"\n5. Các chỉ tiêu cao nhất:")
print(f"   - Sản phẩm có doanh thu cao nhất:  {top_prod['Product']} ({top_prod['Revenue']:,.0f} đ)")
print(f"   - Thành phố có doanh thu cao nhất: {top_city['City']} ({top_city['Revenue']:,.0f} đ)")
print(f"   - Tháng có doanh thu cao nhất:    {top_month['Month']} ({top_month['Revenue']:,.0f} đ)")

# 6. Viết 3-5 nhận xét dựa trên kết quả
print("\n6. Nhận xét kinh doanh:")
print("""
1. Python Basics Book, Notebook A5 và Calculator dẫn đầu doanh thu, chiếm hơn 51.8% tổng doanh số.
2. Hà Nội là thị trường số một (chiếm 29.42%), kế tiếp là Cần Thơ (20.15%) và TP.HCM (19.77%).
3. Tháng 4/2026 đạt đỉnh doanh thu (6.86 triệu đ), Tháng 6 thấp nhất (3.32 triệu đ) do bắt đầu kỳ nghỉ hè.
4. Đơn ngoại lai mua sỉ mang lại thêm +24.81% doanh thu, đóng vai trò quan trọng trong việc tăng quy mô dòng tiền.
""")

# Xuất báo cáo Excel gồm 4 sheet
excel_path = os.path.join(os.path.dirname(__file__), "..", "stationery_report.xlsx")
with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
    clean_df.to_excel(writer, sheet_name="dữ liệu sạch", index=False)
    rev_by_product.to_excel(writer, sheet_name="doanh thu theo sản phẩm", index=False)
    rev_by_city.to_excel(writer, sheet_name="doanh thu theo thành phố", index=False)
    rev_by_month.to_excel(writer, sheet_name="doanh thu theo tháng", index=False)

print(f"-> Đã lưu báo cáo Excel gồm 4 sheet vào: {os.path.abspath(excel_path)}")
print("=" * 70)

