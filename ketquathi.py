# ketqua đậu trượt

toan = float(input("nhập điểm thi môn Toán:"))
ly = float(input("nhập điểm thi môn Lý:"))
hoa = float(input("nhập điểm thi môn Hóa:"))

tong = toan + ly + hoa

if tong>= 15 and ((toan>=4) and (ly>=4) and (hoa>=4)):
    print("đậu")
    if ((toan>5) and (ly>5) and (hoa>5)):
        print("học đều")
    else:
        print("học lệch")
else:
    print("trượt")
