n = 10
tong_le = 0
print(f"tổng các số lẻ từ 1 đến {n}:")

for i in range(1, n+1,2):
    tong_le = tong_le+i
    print(f" + {i}")
    
print(f"tổng lẻ từ 1 đến {n}: {tong_le}")