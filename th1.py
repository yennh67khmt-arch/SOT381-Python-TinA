so_dien = int(input("Nhập số điện đã dùng: "))
tien = 0
so = so_dien

if so > 350:
    tien += (so - 350) * 2927
    so = 350

if so > 200:
    tien += (so - 200) * 2536
    so = 200

if so > 100:
    tien += (so - 100) * 2014
    so = 100

if so > 50:
    tien += (so - 50) * 1734
    so = 50

tien += so * 1678

print(f"Số điện: {so_dien} số")
print(f"Tiền điện phải trả: {tien:,} VND")