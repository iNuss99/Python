# ĐOẠN NHẬN XÉT VỀ CHẤT LƯỢNG DỮ LIỆU, NGOẠI LAI VÀ KẾT QUẢ DOANH THU

## 1. Chất lượng dữ liệu (Data Quality)
- **Tình trạng ban đầu:** Dữ liệu thô gồm 154 dòng, 9 cột, gặp nhiều lỗi thực tế: khoảng trắng thừa ở đầu/cuối chuỗi, định dạng chữ hoa/thường lộn xộn, tên địa phương viết tắt/không đồng nhất (*TP.HCM, HCM, Ho Chi Minh*; *Hanoi, Ha Noi*). Ngoài ra có 4 dòng trùng lặp hoàn toàn, 9 dòng thiếu `Quantity`/`UnitPrice`, 3 dòng thiếu `Discount`, 2 dòng thiếu `City`, và 8 dòng có số lượng hoặc đơn giá $\le 0$.
- **Sau khi làm sạch:** Đã chuẩn hóa chuỗi, gộp tên thành phố bằng từ điển ánh xạ, điền `Discount = 0.0`, điền `City = 'Unknown'`, loại bỏ trùng lặp và các dòng $\le 0$/thiếu ở Quantity và UnitPrice. Bộ dữ liệu sạch `clean_df` còn **133 dòng**, chuyển `OrderDate` sang `datetime64`.

## 2. Phân tích ngoại lai (Outliers)
- **Phương pháp IQR:** $Q_1 = 2.0$, $Q_3 = 8.0$, $IQR = 6.0$, ngưỡng trên là **17.0**.
- **Kết quả:** Phát hiện **6 đơn hàng ngoại lai** (từ 60 đến 200 chiếc) ở các sản phẩm tiêu hao: *Ballpoint Pen, Notebook A5, Highlighter, File Folder*.
- **Ý nghĩa:** Ngoại lai làm tăng vọt giá trị lớn nhất (Max: +1233.33%), Sum (+104.45%) và Mean (+95.23%), nhưng **Trung vị hoàn toàn không đổi (0.00%)**, thể hiện rõ tính kháng nhiễu của Median.
- **Quyết định:** Đây là các đơn mua sỉ B2B thực tế cho trường học/doanh nghiệp với chiết khấu 15%, **không phải lỗi nhập liệu**, nên **giữ lại** trong phân tích doanh thu.

## 3. Kết quả doanh thu (Revenue)
- **Tổng doanh thu:** Đạt **31,259,600 VNĐ** (chênh lệch **+24.81%** nhờ 6 đơn hàng sỉ).
- **Top 1 Sản phẩm:** `Python Basics Book` đạt **5,614,750 VNĐ** (chiếm 17.96%), theo sát là `Notebook A5` (5,551,500 VNĐ - 17.76%) và `Calculator` (5,025,000 VNĐ - 16.08%). Bộ 3 này đóng góp hơn 51.8% tổng doanh thu.
- **Top 1 Thành phố:** `Ha Noi` dẫn đầu với **9,198,100 VNĐ** (chiếm 29.42%), kế tiếp là `Can Tho` (6,298,600 VNĐ - 20.15%) và `Ho Chi Minh` (6,179,500 VNĐ - 19.77%).
- **Top 1 Tháng:** `Tháng 04/2026` đạt đỉnh với **6,861,250 VNĐ** (chiếm 21.95%), sau đó giảm mạnh vào `Tháng 06/2026` (3,324,350 VNĐ) do học sinh, sinh viên bước vào kỳ nghỉ hè.

