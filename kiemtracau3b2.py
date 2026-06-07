#tong phan tu chia het cho 2 hoac 3
n = int(input("nhập sô lượng:"))
ds=[]
tong= 0
for i in range (n):
    ptu = int(input(f"số thứ {i+1}:"))
    ds.append(ptu)
for i in range (n):
    ptu = ds[i]
    if ptu %3 == 0 or ptu % 2 ==0:
        print(f"phần thử chia hết cho 2 hoặc 3 là: {ptu}"); tong = tong + ptu
print("tổng:", tong)
        
      