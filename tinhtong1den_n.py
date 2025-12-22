#tính tổng từ 1 đến n (khác bài số lẻ)

n = 10
tong= 0
print(f" tổng từ 1 đến {n}")

for i in range (1, n+1,2):
    tong = tong+i
    print(f"{tong}")