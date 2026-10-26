import numpy as np
print(np.__version__)

#Tạo 1 mảng với các pt là số 0
arr = np.zeros(5)
print(arr)

#Tạo các mảng với các pt là số 1
arr = np.ones(4)
print(arr)

#Tạo mảng với các pt là số 2
arr = np.full(5, 2)
print(arr)

#Tạo mảng với các pt là số 3
arr = np.full(5, 3)
print(arr)

#Tạo mảng với các pt là số 4
arr = np.ones(5) * 4
print(arr)

#Tạo 1 mảng với arange - tạo 1 dãy số
arr = np.arange(1, 10)
print(arr)

#Tạo 1 dãy số với step: 0 2 4 6 8 10
arr = np.arange(0, 11, 2)
print(arr)

#Tạo 1 dãy số cách đều nhau
arr = np.linspace(0, 10, 5)
print(arr)

#Tạo 1 dãy số nguyên random
arr = np.random.randint(1, 100, size = 5)
print(arr)

#Thao tác với mảng 1 chiều thư viện numpy
arr = np.array([10, 20, 30, 40, 50])
print(arr) #in toàn bộ mảng
print(arr[0]) #truy cập phần tử đầu tiên
print(arr[1]) #truy cập phần tử thứ 2
print(arr[-1]) #truy cập phần tử cuối cùng
print(arr[arr.size -1]) #truy cập phần tử cuối cùng

#Slicing
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4]) #truy cập phần tử từ vị trí 1 đến 3
print(arr[:3])
print(arr[3:])
print(arr[::2])

#modifying elements
arr = np.array([10, 20, 30, 40, 50, 60])
#cập nhật phần tử thứ 2 thành giá trị 99
# arr[1] = 99
# print(arr)

arr[1:4] = 0
print(arr)

#arithmetic operations
arr = np.array([10, 20, 30, 40])
print(arr + 5)
print(arr - 5)
print(arr * 2)
print(arr / 10)
print(arr ** 2)

#useful properties - functions
arr = np.array([10, 20, 30, 40])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

print(np.min(arr))
print(np.max(arr))
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))

#filtering e using condition
scores = np.array([45, 75, 60, 85, 95])
# print(scores >= 7)
# print(scores[(scores >= 70)])

#sắp xếp tăng dần
print(np.sort(scores))
#sắp xep giảm dần
print(np.sort(scores)[::-1])

#tìm điểm từ 60 đến 90
print(scores[(scores >= 60) & (scores <= 90)])

scores[scores < 50] = 50
print(scores)

#tìm theo đk - where
positions = np.where(scores >= 80)
print(positions)
#Phân loại điểm đạt và chưa đạt
results = np.where(scores >= 80, "Pass", "Fail")
print(results)

#đem pt thỏa điều kiện
print(np.sum(scores >= 70))
print(np.count_nonzero(scores >= 70))

#lấy các pt duy nhất unique()
arr = np.array([10, 20, 10, 30, 20, 40, 30])
print(np.unique(arr))

#đem số lần xuất hiện của các pt
values, counts = np.unique(arr, return_counts=True)
print(values)
print(counts)

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])
result = np.concatenate((arr1, arr2))
print(result)

#them 1 pt
arr = np.array([10, 20, 30])
arr = np.append(arr, 50)
print(arr)

# xoa 1 pt
arr = np.array([10, 20, 30, 40, 50])
result = np.delete(arr, 2)
print(result)

# xoa nhieu vij tri
print(np.delete(arr,[0,2]))

# gioi han gia tri clip()

'''
dua cac gia tri nho hon nguong toi thieu en cai nguong do va cac gia tri lon hon nguong toi da xuong nguong do

'''

scores = np.array([-10, 30, 60, 90, 120 ])
result = np.clip(scores, 0, 100)
print(result)

# chuyen doi kieu du lieu 
result = arr.astype(float)
print(result)
print(result.dtype)

# ham lam tron so

arr = np.array([2.345, 3.678, 4.567])
print(np.round(arr,2))
print(np.round(arr))


