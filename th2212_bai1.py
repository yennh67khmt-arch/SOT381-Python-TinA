d = float(input("nhập chiều rộng hcn:"))
r = float(input("nhập chiều dài hcn:"))
while d>=0.0 and r>=0.0:       
 c = (d + r)*2
 s = d*r
 break   
print(f"chu vi hcn là {c:.2f}")
print(f"diện tích hcn là {s:.2f}")