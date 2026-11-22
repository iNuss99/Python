import re

# s1 = Python2026
# s2 = python2026
# s3 = Abc1
# s4 = abc

mssv = input("Nhập MSSV: ")
if re.fullmatch(r"\d{10}", mssv):
    print("Hợp lệ")
else:
    print("Không hợp lệ")