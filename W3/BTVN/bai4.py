ngay_dau = [200, 180, 250]
ngay_cuoi = [0, 220, 270]

doanh_thu = ngay_dau + ngay_cuoi

doanh_thu.pop(3)

doanh_thu.append(300)

tong_dt = sum(doanh_thu)

luy_ke = []
current_sum = 0
for val in doanh_thu:
  current_sum += val
  luy_ke.append(current_sum)
  
  chenh_lech = [
    doanh_thu[i] - doanh_thu[i - 1] for i in range(1, len(doanh_thu))
]
print("Mảng doanh thu sau khi cập nhật:", doanh_thu)
print("Tổng doanh thu:", tong_dt)
print("Doanh thu lũy kế:", luy_ke)
print("Mức tăng/giảm giữa các ngày:", chenh_lech)