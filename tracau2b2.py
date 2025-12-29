import math 
def tong(x,n):
    S=0
    for i in range (n):
        S= math.sqrt(x+S)
    return S
n = int(input("nhập số:"))
while n<0:
    n=int(input("nhập lại:"))
S4= tong(3,n)
print("kết quả là:", S4)
    
        
        