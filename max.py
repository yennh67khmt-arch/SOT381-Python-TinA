a = float(input("nhập cạnh a:"))
b = float(input("nhập cạnh b:"))
c = float(input("nhập cạnh c:"))

max = a
if b> max:
    max = b
if c> max:
    max = c
print(f"số lớn nhất là {max}")
min = a
if b< min:
    min = b
if c< min:
    min = c
print(f"số nhỏ nhất là {min}")