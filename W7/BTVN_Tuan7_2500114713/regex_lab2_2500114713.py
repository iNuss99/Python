import re

# Bai 1
text_bai1 = "Python was created in 1991, Python 3 came out in 2008, and this lab was written in 2026."
years = re.findall(r"\b\d{4}\b", text_bai1)
print("Bai 1:", years)

# Bai 2
text_bai2 = "Hanoi and Saigon are two big cities in Vietnam"
cap_words = re.findall(r"\b[A-Z][a-z]+\b", text_bai2)
print("Bai 2:", cap_words)

# Bai 3
text_bai3 = "Learning #Python with #regex is fun! #100DaysOfCode # done"
hashtags = re.findall(r"#\w+", text_bai3)
print("Bai 3:", hashtags)

# Bai 4
codes = ["ABC-123", "XYZ-999", "abc-123", "AB-1234", "ABCD-123", "ABC123"]
print("Bai 4:")
for code in codes:
    status = "Valid" if re.fullmatch(r"[A-Z]{3}-\d{3}", code) else "Invalid"
    print(f"{code} {status}")

# Bai 5
phones = ["0912345678", "0387654321", "0123456789", "091234567", "09123456789", "0912 345 678"]
print("Bai 5:")
for phone in phones:
    status = "Valid" if re.fullmatch(r"0[35789]\d{8}", phone) else "Invalid"
    print(f"{phone} {status}")

# Bai 6
text_bai6 = "Hello!!! How are you??? I'm fine, thanks."
cleaned_text = re.sub(r"[^\w\s]", "", text_bai6)
print("Bai 6:", cleaned_text)

# Bai 7
text_bai7 = "apple, banana;orange   grape|mango"
fruits = re.split(r"[,;|\s]+", text_bai7)
print("Bai 7:", fruits) 