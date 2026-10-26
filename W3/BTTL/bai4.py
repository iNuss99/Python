
# 4. Bài 4 — Nối và cập nhật
# Tạo hai mảng [1, 2, 3] và [4, 5, 6]. Nối hai mảng, thêm số 7 vào mảng kết quả và xóa phần tử tại index 2.

array1 = [1, 2, 3]
array2 = [4, 5, 6]

result = array1 + array2

result.append(7)
print("Sau khi noi va them 7:", result)  

del result[2]  

print("Ket qua cuoi cung:", result)  
