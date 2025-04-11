# Nhập chuỗi các số, cách nhau bởi dấu phẩy
chuoi_nhap = input("Nhập các số, cách nhau bởi dấu phẩy: ")

# Chuyển chuỗi thành danh sách các số nguyên
danh_sach = [int(x) for x in chuoi_nhap.split(",")]

# Lọc các số lẻ
so_le = [x for x in danh_sach if x % 2 == 1]

# In kết quả, nối lại thành chuỗi cách nhau bởi dấu phẩy
print("Các số lẻ là:", ",".join(map(str, so_le)))