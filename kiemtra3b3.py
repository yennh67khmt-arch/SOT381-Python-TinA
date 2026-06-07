n = int(input("nhập n:"))
ds = []
for i in range (1, n+1):
    k = len(str(i))
    l = i
    tong=0
    while l>0:
        h = l%10
        tong+= h**k
        l=l//10
    if tong==i:
        ds.append(i)
print(f"các sô armstrong:{ds}")
print(f"số lượng: {len(ds)}")