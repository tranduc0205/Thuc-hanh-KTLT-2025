import mymodule

# Nhập số lượng phần tử của danh sách
while True:
    try:
        n = int(input("Nhập số lượng phần tử của danh sách: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Vui lòng nhập một số nguyên dương.")

# Nhập giá trị các phần tử của danh sách
lst = [float(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

# Sử dụng các hàm từ module mymodule
max_value = mymodule.so_lon_nhat(lst)
min_value = mymodule.so_nho_nhat(lst)
sorted_list = mymodule.sap_xep_danh_sach(lst)

# Tìm vị trí của phần tử lớn nhất và nhỏ nhất
max_index = lst.index(max_value)
min_index = lst.index(min_value)

# In kết quả
print(f"Phần tử lớn nhất trong danh sách: {max_value}, Vị trí: {max_index}")
print(f"Phần tử nhỏ nhất trong danh sách: {min_value}, Vị trí: {min_index}")
print(f"Danh sách sau khi sắp xếp: {sorted_list}")

print("trần nguyễn viết đức")
print("mssv:23575205020710013")
