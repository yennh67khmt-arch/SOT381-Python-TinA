#b1: quản lý kho hàng

so_luong = [ 15,8,22,5,12,3 ]
ten_sp = [ "áo", "quần", "giày" , "túi", "mũ", "ví"]

print("các sản phẩm cần nhập thêm là (số lượng <10):")

for i in range (len(so_luong)):
    if so_luong[i]<10:
        print(f" {ten_sp[i]} (số lượng:{ so_luong[i]})")