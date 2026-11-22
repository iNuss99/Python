import re

# print(r'\b')
# print(re.search(r'python', 'i love python'))

kq = re.search(r"meo", "con meo den")
print(kq.group())
print(kq.span())
if kq:
    print("Tim thay")
else:
    print("Khong tim thay")

#lop ky tu: \d, \w, \s,...
# \d la 1 chu so, findall la tim tat ca trong chuoi va tra ve 1 list
print(re.findall(r'\d', 'Nam 2026'))
# \d+ la 1 day so lien nhau
print(re.findall(r"\d+", "Toi 20 tuoi, cao 170 cm"))
# \w+ de lay tung tu
print(re.findall(r'\w+', "I love, python!"))
# \s la khoang trang
print(re.sub(r'\s', '_', 'lap trinh python'))
# . la bat ky cac ky tu nao
print(re.findall(r'c.t', 'cat cut ct coat'))

# nhom tap ky tu [.....]
# tim nguyen am
print(re.findall(r'[ueoai]', 'Hello world'))

# khoang ky tu [a - z]
print(re.findall(r'A-Z', 'Hoc python tai VLU'))
print(re.findall(r'A-Z', 'Hoc python tai VLU'))
print(re.findall(r'0-9', 'Hoc python tai VLU 2026'))

# phu dinh [^...] de giu lai cac sdt
print(re.sub(r'[^0-9]', '', '090-123 (4567)'))

# luong tu (lap bao nhieu lan)
# vd: * va + khac nhau ntn
print(re.findall(r'ab*', 'a ab abb'))
print(re.findall(r'ab+', 'a ab abb'))

# ? co cung duoc, khong co cung cdc
print(re.findall(r'colou?r', 'color colour'))
# {n} la dung n lan
print(re.findall(r'\d{4}', 'Sinh nam 2007, tot nghiep 2027'))
# {n,m} tu n den m lan
print(re.findall(r'\d{2,3}', '5 47 123 9'))

# Vi tri ^, $, \b
s = 'Xin chao'
print(re.search(r'^Xin', s))
print(re.search(r'^Chao', s))
print(re.search(r'Chao$', s))

# \b tim nuyen 1 tu
s = 'on one gone on'
print(re.findall(r'on', s))
print(re.findall(r'\bon\b', s))

# hoac | va nhom ()
print(re.findall(r'cho | meo', ' Nha toi co mot con cho va mot con meo'))

# nhom () de lay tung phan
kq = re.search(r'(\w+)@(\w+)\.com', 'Email: tien@gmail.com')
print(kq.group())
print(kq.group(1))
print(kq.group(2))
# tach ngay thang nam
kq = re.search(r'(\d{2})/(\d{2})/(\d{4})', 'Hom nay la ngay 20/11/2026')
ngay, thang, nam = kq.groups() # Lúc này tuple có đủ 3 phần tử: ('20', '11', '2026')
print(ngay, thang, nam)        # Kết quả: 20 11 2026
print(kq.group())

# cac ham thuong dung 
# match, search, fullmatch
s = 'abc123'
print(re.match(r'\d+', s))
print(re.search(r'\d+', s))
print(re.fullmatch(r'\d+', s))
print(re.fullmatch(r'\w+', s))

# sub de thay the
print(re.sub(r'\d', '*', 'Ma pin: 1234'))
# sub co the xoa cac khoang trong thuong
s = 'Xin           chao      cac         ban        nha'
print(re.sub(r'\s+',' ', s))

#split de tach theo nhieu dau 
print(re.split(r'[,:]', 'tao, cam: xoai'))
 # kiem tra mssv 10 chu so
def kiem_tra_mssv(s):
    return re.fullmatch(r'\d{10}', s) is not None

print(kiem_tra_mssv("2500113793")) #true
print(kiem_tra_mssv("250011379as3")) #false
print(kiem_tra_mssv("25001137")) #false

def kiem_tra_sdt(s):
    return re.fullmatch(r'0\d{9}', s) is not None 
print(kiem_tra_sdt('033873501')) #true
print(kiem_tra_sdt('0338735ad')) #fasle

text = "Lien he: tien@gmail.com hoac darktim#vlu.edu.vn"
print(re.findall(r'\S+@\S+', text))