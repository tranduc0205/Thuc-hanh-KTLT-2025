# main.py

import mymodule

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập từng phần tử
lst = []
for i in range(n):
    so = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(so)

# In danh sách ban đầu
print("Danh sách ban đầu:", lst)

# Sắp xếp danh sách
lst_sorted = mymodule.sap_xep_danh_sach(lst)
print("Danh sách sau khi sắp xếp:", lst_sorted)

# Tìm phần tử lớn nhất và nhỏ nhất
max_val = mymodule.tim_lon_nhat(lst)
min_val = mymodule.tim_nho_nhat(lst)
print("trần nguyễn viết đức")
print("mssv:23575205020710013")

print("Phần tử lớn nhất:", max_val)
print("Phần tử nhỏ nhất:", min_val)
