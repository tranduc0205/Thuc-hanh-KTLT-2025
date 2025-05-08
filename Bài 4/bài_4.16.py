# Nhập chuỗi chứa các số nhị phân, cách nhau bởi dấu phẩy
chuoi_nhi_phan = input("Nhập chuỗi các số nhị phân (cách nhau bằng dấu phẩy): ")

# Tách chuỗi thành danh sách các số nhị phân
danh_sach_nhi_phan = chuoi_nhi_phan.split(",")

# In ra từng số nhị phân
print("Các số nhị phân đã nhập:")
for i in danh_sach_nhi_phan:
    print(i.strip())  # Loại bỏ khoảng trắng thừa nếu có
print("sv: tran nguyen viet duc")