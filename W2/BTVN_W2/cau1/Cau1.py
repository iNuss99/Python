import os
from datetime import datetime

filename = input("Nhap ten tap tin: ")

if os.path.exists(filename):
    size = os.path.getsize(filename)
    
    ctime = os.path.getctime(filename)
    created_date = datetime.fromtimestamp(ctime).strftime("%d/%m/%Y %H:%M:%S")
    
    mtime = os.path.getmtime(filename)
    modified_date = datetime.fromtimestamp(mtime).strftime("%d/%m/%Y %H:%M:%S")
    
    print("Thong tin tap tin:")
    print("- Kich thuoc:", size, "byte")
    print("- Ngay tao:", created_date)
    print("- Ngay sua doi gan nhat:", modified_date)
    
    f = open(filename, "r", encoding="utf-8")
    content = f.read()
    print("\nNoi dung tap tin:")
    print(content)
    f.close()
else:
    print("Tap tin khong ton tai!")
