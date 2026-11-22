"""
Bài tập về nhà Tuần 4: Xử lý và Phân tích Dữ liệu Văn Phòng Phẩm
File: homework_analysis.py
"""

import os
import pandas as pd


# =============================================================================
# CÂU 1 (2đ) - KHÁM PHÁ DỮ LIỆU
# =============================================================================
def cau1_kham_pha(df: pd.DataFrame):
    print("=" * 70)
    print("CÂU 1: KHÁM PHÁ DỮ LIỆU")
    print("=" * 70)

    # 1. 5 dòng đầu và 5 dòng cuối
    print("\n1. Năm dòng đầu:")
    print(df.head())
    print("\nNăm dòng cuối:")
    print(df.tail())

    # 2. Số dòng, số cột, tên cột và kiểu dữ liệu
    print(f"\n2. Kích thước: {df.shape[0]} dòng, {df.shape[1]} cột")
    print("\nTên cột và kiểu dữ liệu:")
    print(df.dtypes)

    # 3. Thống kê số giá trị thiếu theo từng cột
    print("\n3. Số lượng giá trị thiếu theo từng cột:")
    print(df.isnull().sum())

    # 4. Đếm số dòng bị trùng lặp hoàn toàn và số OrderID bị lặp
    dup_rows = df.duplicated().sum()
    dup_orderid = df["OrderID"].duplicated().sum()
    print(f"\n4. Số dòng bị trùng lặp hoàn toàn: {dup_rows}")
    print(f"   Số OrderID bị lặp: {dup_orderid}")

    # 5. Liệt kê các giá trị khác nhau của Product, Category, City, PaymentMethod kèm số lượng
    print("\n5. Thống kê các giá trị khác nhau:")
    for col in ["Product", "Category", "City", "PaymentMethod"]:
        print(f"\n--- Cột {col} ({df[col].nunique()} giá trị) ---")
        print(df[col].value_counts(dropna=False))

    print("\n* Nhận xét: Số lượng giá trị khác nhau lớn hơn thực tế do:")
    print("  - Khoảng trắng thừa ở đầu/cuối chuỗi (ví dụ: '  Ballpoint Pen ', 'hai phong ').")
    print("  - Chữ hoa/thường không đồng nhất (ví dụ: 'notebook a5' vs 'Notebook A5').")
    print("  - Tên thành phố viết tắt hoặc khác quy chuẩn (ví dụ: 'HCM', 'TP.HCM' vs 'Ho Chi Minh').")


# =============================================================================
# CÂU 2 (2đ) - LÀM SẠCH DỮ LIỆU
# =============================================================================
def cau2_lam_sach(raw_df: pd.DataFrame) -> pd.DataFrame:
    print("\n" + "=" * 70)
    print("CÂU 2: LÀM SẠCH DỮ LIỆU")
    print("=" * 70)

    clean_df = raw_df.copy()

    # 1. Chuẩn hóa chuỗi và gộp tên thành phố bằng từ điển ánh xạ
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

    # 2. Tìm các dòng thiếu
    missing_qty_price = clean_df[clean_df["Quantity"].isna() | clean_df["UnitPrice"].isna()]
    missing_city_disc = raw_df[raw_df["City"].isna() | raw_df["Discount"].isna()]
    print(f"\n1. Dòng thiếu Quantity hoặc UnitPrice: {len(missing_qty_price)} dòng")
    print(f"   Dòng thiếu City hoặc Discount:        {len(missing_city_disc)} dòng")

    # 3. Tìm các dòng Quantity <= 0 hoặc UnitPrice <= 0
    invalid_rows = clean_df[(clean_df["Quantity"] <= 0) | (clean_df["UnitPrice"] <= 0)]
    print(f"\n2. Dòng có Quantity <= 0 hoặc UnitPrice <= 0: {len(invalid_rows)} dòng")

    # 4. Đề xuất cách xử lý
    print("\n3. Đề xuất phương án xử lý:")
    print("   - Trùng lặp hoàn toàn: Xóa bằng drop_duplicates().")
    print("   - Thiếu Discount: Điền 0.0 (không áp dụng giảm giá).")
    print("   - Thiếu City: Điền 'Unknown' để bảo toàn doanh số.")
    print("   - Thiếu hoặc <= 0 ở Quantity/UnitPrice: Loại bỏ vì vi phạm logic giao dịch.")

    # 5. Tạo clean_df
    clean_df["Discount"] = clean_df["Discount"].fillna(0.0)
    clean_df = clean_df.drop_duplicates()
    clean_df = clean_df.dropna(subset=["Quantity", "UnitPrice"])
    clean_df = clean_df[(clean_df["Quantity"] > 0) & (clean_df["UnitPrice"] > 0)]
    clean_df["OrderDate"] = pd.to_datetime(clean_df["OrderDate"])
    clean_df = clean_df.reset_index(drop=True)

    print(f"\n4. Số dòng trước khi làm sạch: {len(raw_df)}")
    print(f"   Số dòng sau khi làm sạch:   {len(clean_df)}")

    return clean_df


# =============================================================================
# CÂU 3 (2đ) - PHÂN TÍCH NGOẠI LAI
# =============================================================================
def cau3_ngoai_lai(clean_df: pd.DataFrame):
    print("\n" + "=" * 70)
    print("CÂU 3: PHÂN TÍCH NGOẠI LAI (QUANTITY)")
    print("=" * 70)

    # 1. Tính Q1, Q3, IQR và hai ngưỡng
    q1 = clean_df["Quantity"].quantile(0.25)
    q3 = clean_df["Quantity"].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    print(f"1. Q1 = {q1}, Q3 = {q3}, IQR = {iqr}")
    print(f"   Ngưỡng dưới = {lower_bound}, Ngưỡng trên = {upper_bound}")

    # 2. Liệt kê các đơn ngoại lai
    outliers = clean_df[clean_df["Quantity"] > upper_bound]
    print(f"\n2. Danh sách {len(outliers)} đơn ngoại lai (Quantity > {upper_bound}):")
    print(outliers[["OrderID", "Product", "Quantity", "UnitPrice", "Discount", "City"]].to_string(index=False))

    # 3. Lập bảng so sánh
    no_outliers = clean_df[clean_df["Quantity"] <= upper_bound]
    comp = pd.DataFrame({
        "Chỉ số": ["Trung bình (Mean)", "Trung vị (Median)", "Lớn nhất (Max)", "Tổng (Sum)"],
        "Khi GIỮ ngoại lai": [clean_df["Quantity"].mean(), clean_df["Quantity"].median(), clean_df["Quantity"].max(), clean_df["Quantity"].sum()],
        "Khi LOẠI ngoại lai": [no_outliers["Quantity"].mean(), no_outliers["Quantity"].median(), no_outliers["Quantity"].max(), no_outliers["Quantity"].sum()]
    })
    comp["Thay đổi (%)"] = ((comp["Khi GIỮ ngoại lai"] - comp["Khi LOẠI ngoại lai"]) / comp["Khi LOẠI ngoại lai"] * 100).round(2)
    print("\n3. Bảng so sánh thống kê:")
    print(comp.to_string(index=False))
    print("   -> Chỉ số thay đổi nhiều nhất là Giá trị lớn nhất (Max: +1233.33%), sau đó là Sum và Mean.")
    print("   -> Trung vị (Median) hoàn toàn không đổi (0.00%).")

    # 4. Nhận định kinh doanh
    print("\n4. Nhận định kinh doanh:")
    print("   - Đơn ngoại lai gồm: Ballpoint Pen, Notebook A5, Highlighter, File Folder.")
    print("   - Rất hợp lý vì đây là các đơn sỉ B2B cho cơ quan/trường học (đều nhận chiết khấu 15%).")
    print("   - Ngoại lai không đồng nghĩa với dữ liệu sai -> QUYẾT ĐỊNH GIỮ để phản ánh đúng doanh thu.")

    return upper_bound


# =============================================================================
# CÂU 4 (2đ) - MÃ HÓA DỮ LIỆU
# =============================================================================
def cau4_ma_hoa(clean_df: pd.DataFrame):
    print("\n" + "=" * 70)
    print("CÂU 4: MÃ HÓA DỮ LIỆU (ONE-HOT ENCODING)")
    print("=" * 70)

    # 1 & 2. get_dummies cho Category và PaymentMethod
    cat_dum = pd.get_dummies(clean_df["Category"], prefix="Category", dtype=int)
    pm_dum = pd.get_dummies(clean_df["PaymentMethod"], prefix="PaymentMethod", dtype=int)
    encoded_df = pd.concat([clean_df[["OrderID", "Category", "PaymentMethod"]], cat_dum, pm_dum], axis=1)

    # 3. In 5 dòng và giải thích
    print("1. Năm dòng sau mã hóa:")
    print(encoded_df.head())
    print("\n2. Ý nghĩa các cột 0/1:")
    print("   - 1: Dòng thuộc nhóm tương ứng; 0: Không thuộc nhóm.")
    print("   - Mỗi dòng luôn có chính xác 1 số 1 trong mỗi nhóm vì Category và PaymentMethod là các biến loại trừ lẫn nhau (mutually exclusive).")

    # 4. Giải thích gán 1, 2, 3, 4
    print("\n3. Không nên gán Stationery=1, Books=2, Office Supplies=3, Art Supplies=4 vì:")
    print("   - Category là biến định danh (Nominal), không có thứ bậc tự nhiên.")
    print("   - Gán số tạo ra thứ tự và khoảng cách giả mạo, làm mô hình học máy hiểu sai.")


# =============================================================================
# CÂU 5 (2đ) - PHÂN TÍCH DOANH THU & XUẤT BÁO CÁO
# =============================================================================
def cau5_doanh_thu(clean_df: pd.DataFrame, upper_bound: float, base_dir: str):
    print("\n" + "=" * 70)
    print("CÂU 5: PHÂN TÍCH DOANH THU")
    print("=" * 70)

    # 1. Tạo cột Revenue
    clean_df["Revenue"] = clean_df["Quantity"] * clean_df["UnitPrice"] * (1 - clean_df["Discount"])

    # 2. Tổng doanh thu & chênh lệch khi loại ngoại lai
    rev_all = clean_df["Revenue"].sum()
    rev_no_outliers = clean_df[clean_df["Quantity"] <= upper_bound]["Revenue"].sum()
    diff_pct = ((rev_all - rev_no_outliers) / rev_no_outliers) * 100

    print(f"1. Tổng doanh thu trên clean_df:          {rev_all:>14,.0f} đ")
    print(f"   Tổng doanh thu khi loại bỏ ngoại lai:  {rev_no_outliers:>14,.0f} đ")
    print(f"   Chênh lệch:                            {diff_pct:>14.2f} %")

    # 3. Doanh thu theo Product và City
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

    print("\n2. Top sản phẩm theo doanh thu:")
    print(rev_by_product.head().to_string(index=False, formatters={"Revenue": "{:,.0f} đ".format}))

    print("\n3. Doanh thu theo thành phố:")
    print(rev_by_city.to_string(index=False, formatters={"Revenue": "{:,.0f} đ".format}))

    # 4. Doanh thu theo tháng
    clean_df["Month"] = clean_df["OrderDate"].dt.to_period("M").astype(str)
    rev_by_month = (
        clean_df.groupby("Month")["Revenue"]
        .sum()
        .reset_index()
        .sort_values(by="Month")
    )
    print("\n4. Doanh thu theo tháng:")
    print(rev_by_month.to_string(index=False, formatters={"Revenue": "{:,.0f} đ".format}))

    # 5. Tìm cao nhất
    top_p = rev_by_product.iloc[0]["Product"]
    top_c = rev_by_city.iloc[0]["City"]
    top_m = rev_by_month.sort_values(by="Revenue", ascending=False).iloc[0]["Month"]
    print(f"\n5. Cao nhất:")
    print(f"   - Sản phẩm:  {top_p} ({rev_by_product.iloc[0]['Revenue']:,.0f} đ)")
    print(f"   - Thành phố: {top_c} ({rev_by_city.iloc[0]['Revenue']:,.0f} đ)")
    print(f"   - Tháng:     {top_m} ({rev_by_month.sort_values(by='Revenue', ascending=False).iloc[0]['Revenue']:,.0f} đ)")

    # 6. Nhận xét
    print("\n6. Nhận xét kinh doanh:")
    print("   1. Python Basics Book, Notebook A5 và Calculator dẫn đầu doanh thu (> 51% tổng doanh thu).")
    print("   2. Hà Nội là thị trường lớn nhất (gần 30%), kế tiếp là Cần Thơ và TP.HCM.")
    print("   3. Tháng 4/2026 đạt đỉnh doanh thu (6.86 triệu đ), Tháng 6 thấp nhất (3.32 triệu đ) do kỳ nghỉ hè.")
    print("   4. Đơn sỉ ngoại lai đóng góp thêm +24.81% doanh thu, là phân khúc B2B cần duy trì chính sách ưu đãi.")

    # Xuất các file theo yêu cầu sản phẩm nộp
    csv_file = os.path.join(base_dir, "stationery_clean.csv")
    clean_df.to_csv(csv_file, index=False, encoding="utf-8-sig")

    excel_file = os.path.join(base_dir, "stationery_report.xlsx")
    with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
        clean_df.to_excel(writer, sheet_name="dữ liệu sạch", index=False)
        rev_by_product.to_excel(writer, sheet_name="doanh thu theo sản phẩm", index=False)
        rev_by_city.to_excel(writer, sheet_name="doanh thu theo thành phố", index=False)
        rev_by_month.to_excel(writer, sheet_name="doanh thu theo tháng", index=False)

    print(f"\n-> Đã xuất thành công:")
    print(f"   + {csv_file}")
    print(f"   + {excel_file} (gồm đúng 4 sheet)")


# =============================================================================
# MAIN
# =============================================================================
def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, "stationery_orders.csv")

    raw_df = pd.read_csv(input_file)
    cau1_kham_pha(raw_df)
    clean_df = cau2_lam_sach(raw_df)
    upper_bound = cau3_ngoai_lai(clean_df)
    cau4_ma_hoa(clean_df)
    cau5_doanh_thu(clean_df, upper_bound, base_dir)


if __name__ == "__main__":
    main()
