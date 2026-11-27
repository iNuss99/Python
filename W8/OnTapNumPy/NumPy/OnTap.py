import numpy as np

# BAI 1: Tao va mo ta mang so nguyen

print("--- Bai 1 ---")
arr1 = np.arange(5,20)
print("Mang:", arr1)
print("So Chieu:", arr1.ndim)
print("Hinh Dang:", arr1.shape)
print("So Phan Tu:", arr1.size)
print("Kieu du lieu", arr1.dtype)

# BAI 2: Truy cap phan tu va slicing
print("\n---Bai 2 ---")
arr2 = np.arange(10,20)
print("Mang:", arr2)
print("Phan tu dau tien:", arr2[0])
print("Phan tu cuooi cung:", arr2[-1])
print("5 Phan tu dau", arr2[:5])
print("5 Phan tu cuoi:", arr2[-5:])
print("Cac phan tu o vi tri chan index 0, 2, 4,..:", arr2[::2])

# BAI 3: Tinh toan tren mang
print("\n---Bai 3---")
diem = np.array([6.5, 7.0, 8.5, 9.0, 5.5, 7.5])
diem_moi = diem + 0.5

diem_moi = np.clip(diem_moi, 0, 10)

print("Diem sau khi cong 0.5:", diem_moi)
print("Tong diem:", np.sum(diem_moi))
print("Diem trung binh:", round(np.mean(diem_moi),2))

# BAI 4: Thong ke du lieu
print("\n--- Bai 4 ---")
nhiet_do = np.array([28.5, 30.0, 31.2, 29.8, 27.5, 32.0, 33.1, 30.5, 29.0, 28.0])
print("Nhiet do 10 ngay:", nhiet_do)
print("Thap nhat:", np.min(nhiet_do))
print("Cao nhat:", np.max(nhiet_do))
print("Trung binh:", round(np.mean(nhiet_do), 2))
print("Do lech chuan:", round(np.std(nhiet_do),2))

# BAI 5: Mang 2 chieu va truy cap
print("\n--- Bai 5 ---")
matran = np.arange(1,13). reshape(3, 4)
print("Ma tran 3 x 4:\n", matran)

print("Phan tu hang 2 cot 3:", matran[1, 2])
print("Hang dau tien:", matran[0, :1])
print("Cot cuoi cung:", matran[:, -1])
print("Vung con 2 x 2 (2 hang dau, 2 cot dau):", matran[:2, :2])

# BAI 6: Reshape
print("\n --- Bai 6 ---")
arr6 = np.arange(1, 25)
print("Shape ban dau:", arr6.shape)

mt_4x6 = arr6.reshape(4, 6)
print("Shape sau khi chuyen 4x6:", mt_4x6.shape)

mt_3x8 = mt_4x6.reshape(3, 8)
print("Shape sau khi chuyen 3x8:", mt_3x8.shape)

# BAI 7: Loc du lieu bang dieu kien
print("\n--- BAI 7 ---")
diem_sv = np.array([4.5, 8.0, 6.5, 9.2, 3.0, 7.5, 5.5, 8.5, 6.0, 7.9, 4.0, 10.0])
print("Diem >= 8:", diem_sv[diem_sv >= 8])
print("Diem < 5:", diem_sv[diem_sv < 5])
print("Diem tu 6 den duoi 8:", diem_sv[(diem_sv >= 6) & (diem_sv < 8)])

# BAI 8: Tinh toan theo axis
bang_diem = np.array([
    [7.0, 8.0, 6.5],
    [9.0, 8.5, 9.5],
    [5.5, 6.0, 7.0],
    [8.0, 7.5, 8.0]
])
print("Tong diem tung sinh vien:", np.sum(bang_diem, axis = 1))
print("Diem TB tung sinh vien:", np.round(np.mean(bang_diem, axis = 1), 2))
print("Diem TB tung mon:", np.round(np.mean(bang_diem, axis = 0), 2))

# BAI 9: Ghep va tach mang
print("\n--- BAI 9 ---")
nhom1 = np.array([7.5, 8.0, 6.5])
nhom2 = np.array([9.0, 5.5, 8.5])

mang_chung = np.concatenate((nhom1, nhom2))
print("Mang sau khi ghep:", mang_chung)

phan1, phan2 = np.split(mang_chung, 2)
print("Phan 1 sau khi tach:", phan1)
print("Phan 2 sau khi tach:", phan2)

# BAI 10: Bai toan tong hop - phan tich diem
print("\n--- BAI 10 ---")
diem_tong_hop = np.array([
    [8.0, 7.5, 9.0, 8.5],
    [4.5, 6.0, 5.5, 7.0],
    [9.5, 9.0, 8.5, 10.0],
    [6.5, 7.0, 4.0, 6.0],
    [7.5, 8.0, 7.5, 8.5]
])
tb_sv = np.mean(diem_tong_hop, axis=1)
tb_mon = np.mean(diem_tong_hop, axis=0)
sv_cao_nhat = np.argmax(tb_sv)
so_diem_duoi_5 = np.sum(diem_tong_hop < 5)
print("Diem TB tung sinh vien:", np.round(tb_sv, 2))
print("Diem TB tung mon:", np.round(tb_mon, 2))
print(f"Sinh vien co diem TB cao nhat: Sinh vien thu {sv_cao_nhat + 1} (index {sv_cao_nhat}) voi TB = {tb_sv[sv_cao_nhat]}")
print("So luong diem duoi 5:", so_diem_duoi_5)\

