import re
# BAI 1: Kiem tra ma sinh vien (10 chu so)
print("--- BAI 1 ---")
pattern1 = r"^\d{10}$"
test_msv = ["2500114713", "25001147", "250011471399", "250011471A"]

for msv in test_msv:
    hop_le = bool(re.fullmatch(pattern1, msv))
    print(f"MSV '{msv}': {hop_le}")

# BAI 2: Kiem tra so dien thoai Viet Nam
pattern2 = r"^0\d{9}$"
print("\n--- BAI 2 ---")
test_sdt = ["0901234567", "09012345", "1901234567", "090 123 4567"]

for sdt in test_sdt:
    hop_le = bool(re.fullmatch(pattern2, sdt))
    print(f"SDT '{sdt}': {hop_le}")

# BAI 3: Trich xuat email (.com, .edu, .vn)
print("\n--- BAI 3 ---")
van_ban_email = """
Lien he phong dao tao qua email daotao@vanlang.edu.vn hoac ho tro support@gmail.com.
Email rac test@domain.xyz hoac admin@company.org se bi bo qua.
Ngoai ra con co khoa.dm@sv.edu va contact@shop.vn.
"""
pattern3 = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.(?:com|edu|vn)\b"
emails = re.findall(pattern3, van_ban_email)
print("Cac email hop le trich xuat duoc:", emails)

print("\n--- BAI 4 ---")
def kiem_tra_mat_khau(pw):
    if not (8 <= len(pw) <= 16):
        return False
    if not re.search(r"[A-Z]", pw):
        return False
    if not re.search(r"[a-z]", pw):
        return False
    if not re.search(r"\d", pw):
        return False
    return True

test_pw = ["Abc12345", "abc12345", "ABC12345", "Abcdefgh", "Abc12", "Abc123456789012345"]
for pw in test_pw:
    print(f"Mat khau '{pw}': {kiem_tra_mat_khau(pw)}")

# BAI 5: Trich xuat ngay thang (dd/mm/yyyy)
print("\n--- BAI 5 ---")
van_ban_ngay = "Ngay khai giang la 05/09/2026, thi giua ky vao 20/10/2026 va nghi le 1/1/2027."
pattern5 = r"\b\d{2}/\d{2}/\d{4}\b"
ds_ngay = re.findall(pattern5, van_ban_ngay)
print("Cac ngay dung dinh dang dd/mm/yyyy:", ds_ngay)

# BAI 6: Tim ma buu chinh (dung 5 chu so doc lap)
print("\n--- BAI 6 ---")
van_ban_zip = "Ma buu chinh HCM la 70000, Ha Noi la 10000. So tai khoan 123456789 va ma 1234 khong hop le."
pattern6 = r"\b\d{5}\b"
ds_zip = re.findall(pattern6, van_ban_zip)
print("Cac ma 5 chu so doc lap:", ds_zip)

# BAI 7: Chuan hoa khoang trang
print("\n--- BAI 7 ---")
cau_tho = "   Lap   trinh    Python   voi   RegEx   rat   tien   loi.   "
cau_chuan = re.sub(r"\s+", " ", cau_tho).strip()
print(f"Sau khi chuan hoa: '{cau_chuan}'")

# BAI 8: Tach du lieu theo dau phan cach (, hoac ;)
print("\n--- BAI 8 ---")
chuoi_ten = "Do Minh Khoa, Hoang Khuong Duy; Nguyen Ngoc Tien ,  Khoa123;KhoaJQOK"
ds_ten = [ten.strip() for ten in re.split(r"[,;]", chuoi_ten)]
print("Danh sach ten sau khi tach:", ds_ten)

# BAI 9: Kiem tra ten nguoi
print("\n--- BAI 9 ---")
pattern9 = r"^[a-zA-Z]+(?:\s[a-zA-Z]+)*$"
test_ten = ["Do Minh Khoa", "Khoa", " Do Minh Khoa", "Do Minh Khoa ", "Do Minh Khoa 123", "Khoa@"]

for ten in test_ten:
    hop_le = bool(re.fullmatch(pattern9, ten))
    print(f"Ten '{ten}': {hop_le}")

# BAI 10: Bai toan tong hop - phan tich log
print("\n--- BAI 10 ---")
logs = [
    "[2026-11-27 09:15:30] ERROR - User 2374802010 failed login.",
    "[2026-11-27 10:05:12] INFO - User 2500114713 updated profile.",
    "Dong log bi sai dinh dang khong co timestamp"
]

pattern10 = r"^\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\]\s+([A-Z]+)\s+-\s+User\s+(\d+)\s+(.+)$"

for line in logs:
    match = re.match(pattern10, line)
    if match:
        thoi_gian, muc_log, ma_user, thong_bao = match.groups()
        print(f"Hop le -> Thoi gian: {thoi_gian} | Muc: {muc_log} | User: {ma_user} | Noi dung: {thong_bao}")
    else:
        print(f"Sai dinh dang -> {line}")