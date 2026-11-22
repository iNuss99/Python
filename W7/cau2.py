import re

# s1 = Có 3 táo, 12 cam và 5 lê
# s2 = Năm 2026 lớp có 40 bạn
cau = input("Nhập một câu: ")
ds_chuoi_so = re.findall(r"\d+", cau)
cac_so = [int(x) for x in ds_chuoi_so]
tong = sum(cac_so)

print(f"Các số: {cac_so}")
print(f"Tổng: {tong}")