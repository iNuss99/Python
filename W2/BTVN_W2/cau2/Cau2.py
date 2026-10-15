file_nguon = input("Nhap ten tap tin nguon: ")
file_dich = input("Nhap ten tap tin dich: ")

f_in = open(file_nguon, "r", encoding="utf-8")
noi_dung = f_in.read()
f_in.close()

noi_dung_hoa = noi_dung.upper()

f_out = open(file_dich, "w", encoding="utf-8")
f_out.write(noi_dung_hoa)
f_out.close()

print("Da ghi sang tap tin dich thanh cong!")
