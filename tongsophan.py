#tính tổng 1 + 1/2 + 1/3 + ... + 1/n

n = 5
tong_so_phan = 0
print("tổng từ 1 đến 1/{n}")

for i in range (1,n+1):
    gia_tri = 1/i
    tong_so_phan = tong_so_phan + gia_tri
    print(f"+ 1/ {i} = {gia_tri:.3f}. tổng: {tong_so_phan:.3f}")
    
print(f"kết quả cuối cùng: {tong_so_phan:.3f}")