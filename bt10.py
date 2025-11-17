# BÀI TẬP THỰC HÀNH 10

tien_gui = float(input("nhập số tiền gửi: "))
lai_suat = float(input("nhập số lãi suất(ptram/năm): "))
so_thang = int(input("nhập số tháng muốn gửi: "))

lai = ( tien_gui * so_thang * so_thang / 12)

print("lãi suất là: ", lai)