filename = input("Nhap ten tap tin: ")

f = open(filename, "r", encoding="utf-8")
data = f.read()
f.close()

numbers = [int(x) for x in data.split()]

chan = []
le = []

for x in numbers:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)

tong_chan = sum(chan)
tong_le = sum(le)

str_chan = " ".join(str(x) for x in chan)
str_le = " ".join(str(x) for x in le)

f_chan = open("chan.txt", "w", encoding="utf-8")
f_chan.write(str_chan)
f_chan.close()

f_le = open("le.txt", "w", encoding="utf-8")
f_le.write(str_le)
f_le.close()

print("chan.txt:", str_chan, "ong:", str(tong_chan) + " .", "le.txt:", str_le, "Tong:", str(tong_le))

