#ptrinh tổng với n nhập từ bàn phím
def tong(n):
    S2=0
    for i in range (2,n+1,2):
       S2 = S2+i
    return S2
n = int(input("nhập số tự nhiên n:"))
S=tong(n)
print("kết quả:",S)