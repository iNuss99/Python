f = open("numbers.txt","r", encoding= "utf-8")
data = f.read()
data = data.split("\n")
total = 0
for i in data:
    if i != "":
        total += int(i)
print(total)
f.close()