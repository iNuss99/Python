arr2 = [42, 67, 85, 51, 73, 98, 60, 39, 80]

filtered = [x for x in arr2 if x > 50 and x <= 80]

count = len(filtered)
trung_binh = sum(filtered) / count if count > 0 else 0

print("Cac so thoa dieu kien:", filtered)
print("So luong:", count)
print("Trung binh:", trung_binh)