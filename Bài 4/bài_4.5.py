ds = input("danh sach: ").split()

print(ds)

# Không cần gọi split() trên ds nữa; ds đã là danh sách các từ
ds.reverse()

# Kết hợp các từ thành một chuỗi duy nhất
dao_ds = ' '.join(ds)
print(dao_ds)