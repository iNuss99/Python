f = open("numbers.txt","r", encoding= "utf-8")
data = f.read()
data = data.split("\n")
sum = 0
for i in data:
    if i != "":
        sum += int(i)
print(sum)
f.close()