ten = input("Nhập tên học sinh: ")
toan = float(input("Điểm Toán: "))
ly = float(input("Điểm Lý: "))
hoa = float(input("Điểm Hóa: "))

tb = (toan + ly + hoa) / 3

if tb >= 8:
    loai = "Giỏi"
elif tb >= 6.5:
    loai = "Khá"
elif tb >= 5:
    loai = "Trung bình"
else:
    loai = "Yếu"

print("===== KẾT QUẢ =====")
print(f"Học sinh: {ten}")
print(f"Điểm trung bình: {tb:.2f}")
print(f"Xếp loại: {loai}")
