n=int(input("nhập số n, với 0<n<10 :"))
giai_thua= 1
for i in (1,n+1):
    giai_thua*= i   
print(f"{n}! giai thừa {n} là:{giai_thua}")