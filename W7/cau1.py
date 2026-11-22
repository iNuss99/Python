import re


# s1 = Lớp CNTT 2026 có 45 sinh viên
# s2 = Không có số nào 
# s3 = A1B2C3
chuoi = input("Nhập chuỗi: ")

# Tìm tất cả các ký tự chữ số (0-9) riêng lẻ trong chuỗi
cac_chu_so = re.findall(r"\d", chuoi)

# Số lượng chữ số chính là độ dài của danh sách kết quả
so_luong = len(cac_chu_so)

print(f"Số chữ số: {so_luong}")