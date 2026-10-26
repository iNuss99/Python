import pandas as pd 
# pyrefly: ignore[missing-import]
import numpy as np

# print(pd.__version__)

df = pd.read_csv("data.csv", encoding="utf-8")
# print(df)

#xem 5 dong dau tien
print(df.head())

# xem 5 dong cuoi cung

print(df.tail())

# xem kich thuoc du lieu

print(df.shape)

# Xem ten cot
print(df.columns)

# xem thong tin tong quan
print(df.info())

# xem kieu du lieu
print(df.dtypes)
print(df.describe())

#phat hien du lieu bi thieu
print(df.isna().sum().sum())

# loc cac dong bi thieu
missing_rows =  df[df.isna().any(axis=1)]
print(missing_rows)

# xoa dong du lieu bi thieu
df_drop =  df.dropna()
print(df_drop)

#thay the du lieu bi thieu
df["Python"] = df["Python"].fillna(
    df["Python"].mean()
)
print(df)

# phat hien du lieu sai - du lieu bat thuong

'''
    Tuoi sv: 16 - 100
    diem python & pandas: 0 - 100
    Chuyen can: 0 - 100
'''
invalid_age = df[
    ((df["Age"] < 16) | (df ["Age"] > 100))
]
print(invalid_age)

# tim kiem khong hop le - pandas
invalid_pandas = df[
    ((df["Pandas"] < 0) | (df["Pandas"] > 100))
]
print(invalid_pandas)

# tim diem ko hop le - attendance
invalid_attendance = df[
    ((df["Attendance"] < 0) | (df["Attendance"] > 100))
]
print(invalid_attendance)

# lam sach du lieu bi sao
df.loc[
    (df["Age"] < 16) | (df["Age"] > 100), "Age"
] = np.nan

df.loc[
    (df["Python"] < 0) | (df["Python"] > 100), "Python"
] = np.nan

df.loc[
    (df["Pandas"] < 0) | (df["Pandas"] > 100), "Pandas"
] = np.nan

df.loc[
    (df["Attendance"] < 0) | (df["Attendance"] > 100), "Attendance"
] = np.nan

print(df.isna().sum())
# chuan hoa du lieu
df["Name"] = df["Name"].str.strip()
print(df["Name"])

# Chuan hoa ten lop
df["Class"] = df["Class"].str.strip().str.upper()
print(df["Class"].unique())

# Kiem tra mssv bi trung ko
print(df[df.duplicated(subset=["StudentID"],keep=False)])

# xu ly du lieu bi thieu sau khi lam sach
# chuen gia tri NaN sang 1 gia tri thay the

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Python"] = df["Python"].fillna(df["Python"].median())
df["Pandas"] = df["Pandas"].fillna(df["Pandas"].median())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].median())

# Kiem tra lai
print(df.isna().sum())

#tinh toan va phan tich

df["Average"] = (df["Python"] + df["Pandas"]) / 2
print(df)

# phan loai ket qua

df["Result"] = df["Average"].apply(
    lambda score: "Pass" if score >= 70 else "Fail"
)
print(df)

# loc cac sinh vien dat
passed = df[df["Result"] == "Pass"]
print(passed)

# sap xep theo diem trung binh

df_sorted = df.sort_values(by='Average',ascending=False)
print(df_sorted)

# thong ke tong quan

print("Average Python:", df["Python"].mean())
print("Average Pandas:", df["Pandas"].mean())
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())
