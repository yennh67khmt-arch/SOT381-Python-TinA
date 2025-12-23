def tinhS(n):
    TS = 0
    for i in range(1, n + 1):
        TS = TS + i
    gioi_han_mau = int(n / 2)
    MS = 0
    for i in range(1, gioi_han_mau + 1):
        MS = MS + 2 * i
    if MS == 0:
        return 0
        
    S = TS / MS
    return S
n = 20
kq = tinhS(n)
print(f"Kết quả S = {kq}")