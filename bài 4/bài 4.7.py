# Nhập chuỗi từ bàn phím
chuoi_goc = input("Nhập chuỗi: ")

# Loại bỏ tất cả chữ số (0-9) bằng cách dùng list comprehension
chuoi_moi = "".join(i for i in chuoi_goc if not i.isdigit())
# chọn và lấy các phần tử trong chuỗi gốc nếu nó không phải là số
# join: nối các chuỗi nhỏ thành một chuỗi duy nhất

# In chuỗi sau khi loại bỏ chữ số
print("Chuỗi sau khi loại bỏ chữ số:", chuoi_moi)
print("tran nguyen viet duc")
print("mssv:23575205020710013")