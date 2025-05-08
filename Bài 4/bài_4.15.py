# Nhập chuỗi từ bàn phím
chuoi = input("Nhập chuỗi các từ(không viết dấu): ")

# Tách chuỗi thành các từ
danh_sach_tu = chuoi.split()

# Sắp xếp các từ theo thứ tự từ điển
danh_sach_tu.sort()
#.sort(): Sắp xếp các từ trong danh sách theo thứ tự từ điển (alphabet).


# In ra các từ theo thứ tự từ điển
print("Các từ theo thứ tự từ điển:", ", ".join(danh_sach_tu))