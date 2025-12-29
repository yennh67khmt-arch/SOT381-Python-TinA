#giai phuong trinh bac nhat
a = int(input("nhập số nguyên a:"))
b = int(input("nhập số nguyên b:"))
x = 0
if a == 0 and b == 0:
    print("phương trình có vô số nghiệm")
elif a == 0 and b != 0:
    print("phương trình vô nghiệm")
else:
    print(f"phương trình có một nghiệm x={(-b/a):.2f}")