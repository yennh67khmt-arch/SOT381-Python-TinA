temp = float(input("Nhập nhiệt độ: "))
loai = input("Nhập loại (C, F, K): ").upper()

if loai == "C":
    C = temp
    F = C * 9/5 + 32
    K = C + 273.15
elif loai == "F":
    F = temp
    C = (F - 32) * 5/9
    K = C + 273.15
elif loai == "K":
    K = temp
    C = K - 273.15
    F = C * 9/5 + 32
else:
    print("Loại không hợp lệ!")
    exit()

print(f"Nhiệt độ (C): {C:.2f}")
print(f"Nhiệt độ (F): {F:.2f}")
print(f"Nhiệt độ (K): {K:.2f}")
