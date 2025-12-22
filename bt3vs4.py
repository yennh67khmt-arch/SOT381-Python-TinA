m = float(input("nhập giá trị m:"))
n = float(input("nhập giá trị n:"))
k = float(input("nhập giá trị k:"))

def soln(m,n,k):
    max = m
    if n>max:
        max = n
    if k> max:
        max = k
    return max
lon_nhat=soln(m,n,k)
print(f"số lớn nhất là: {lon_nhat}")

def sonn(m,n,k):
    min = m
    if n<min :
          min = n
    if k<min :
          min = k
    return min
nho_nhat=sonn(m,n,k)
print(f"số nhỏ nhất là: {nho_nhat}")
        