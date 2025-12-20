#bt2: phân loại học sinh

diem_so = [ 8.5,7.0,9.2,6.8,5.5,8.8]

print(" kết quả phân loại học sinh là:")

for i in range (len(diem_so)):
    if diem_so[i] >= 8:
        loai = "giỏi"
    elif diem_so[i] >= 6.5:
        loai = "khá"
    else:
        loai = "trung bình"
    print(f" {diem_so[i]} phân loại {loai}")