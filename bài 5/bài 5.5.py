# main.py

import mymodule  # Nhập module mymodule chứa các hàm tùy chỉnh

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử trong danh sách: "))  # Yêu cầu người dùng nhập số lượng phần tử

# Khởi tạo danh sách rỗng để lưu trữ các phần tử
lst = []
for i in range(n):  # Lặp từ 0 đến n-1
    so = float(input(f"Nhập phần tử thứ {i+1}: "))  # Nhập phần tử và chuyển đổi thành số thực
    lst.append(so)  # Thêm phần tử vào danh sách lst

# In danh sách ban đầu
print("Danh sách ban đầu:", lst)  # Hiển thị danh sách các phần tử đã nhập

# Sắp xếp danh sách
lst_sorted = mymodule.sap_xep_danh_sach(lst)  # Gọi hàm sap_xep_danh_sach từ mymodule để sắp xếp danh sách

# In danh sách sau khi sắp xếp
print("Danh sách sau khi sắp xếp:", lst_sorted)  # Hiển thị danh sách đã sắp xếp

# Tìm phần tử lớn nhất và nhỏ nhất
max_val = mymodule.so_lon_nhat(lst)  # Gọi hàm so_lon_nhat để tìm phần tử lớn nhất
min_val = mymodule.so_nho_nhat(lst)  # Gọi hàm so_nho_nhat để tìm phần tử nhỏ nhất

# In phần tử lớn nhất và nhỏ nhất
print("Phần tử lớn nhất:", max_val)  # Hiển thị phần tử lớn nhất
print("Phần tử nhỏ nhất:", min_val)  # Hiển thị phần tử nhỏ nhất

print("trần nguyễn viết đức")
print("mssv:23575205020710013")
