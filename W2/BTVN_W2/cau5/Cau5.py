filename = input("Nhap ten tap tin: ")

f_check = open(filename, "r", encoding="utf-8")
old_content = f_check.read()
f_check.close()

f = open(filename, "a", encoding="utf-8")
if len(old_content) > 0 and not old_content.endswith("\n"):
    f.write("\n")

while True:
    line = input("Nhap dong nhap exit de dung: ")
    if line == "exit":
        break
    f.write(line + "\n")

f.close()

print("\nNoi dung tap tin sau khi ghi:")
f = open(filename, "r", encoding="utf-8")
print(f.read())
f.close()
