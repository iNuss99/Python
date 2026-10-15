filename = input("Nhap ten tap tin: ")

f = open(filename, "r", encoding="utf-8")
content = f.read()
f.close()

lines = content.splitlines()
so_dong = len(lines)

words = content.split()
so_tu = len(words)

so_ky_tu = sum(len(w) for w in words)

print("Ket qua:", so_dong, "dong .", so_tu, "tu .", so_ky_tu, "ky tu")
