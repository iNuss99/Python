diem = [8.34, 10.5, -1, 6.48, 4.96, 7, 3.21]
ket_qua = []

for d in diem:

    if d < 0:
        d = 0
    elif d > 10:
        d = 10
    d_rounded = round(d, 1)

    if d_rounded >= 8.0:
        loai = "Gioi"
    elif d_rounded >= 6.5:
        loai = "Kha"
    elif d_rounded >= 5.0:
        loai = "Trung binh"
    else:
        loai = "Yeu"

ket_qua.append((d_rounded, loai))
print("Ket qua sau khi xu ly:")
for i in range(len(ket_qua)):
  d, l = ket_qua[i]
  print(f"Điểm gốc: {diem[i]} -> Sau xử lý: {d} -> Xếp loại: {l}")