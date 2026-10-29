from collections import Counter

arr = [3, 7, 3, 9, 7, 3, 5, 9, 3]
counter = Counter(arr)
unique_vals = list(counter.keys())

max_freq_val, max_freq_count = counter.most_common(1)[0]

print("Các giá trị duy nhất:", unique_vals)
print("Giá trị xuất hiện nhiều nhất:", max_freq_val)   
print("Số lần xuất hiện:", max_freq_count)