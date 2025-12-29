n= int(input("nhập sô lượng:"))
dssn=[]
for i in range (n):
    ptu = int(input(f"số thứ {i+1}:"))
    dssn.append(ptu)
for i in range (n):
    ptu = dssn[i]
    if ptu %6 == 0:
        print(f"chia hết cho đồng thời 2 và 3 là:{ptu}")
        
    