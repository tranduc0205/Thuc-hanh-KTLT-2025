# Nhập chuỗi từ người dùng
chuoi = input("Nhập các số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách
ds_nhiphan = chuoi.split(",")

# Tạo danh sách mới chứa các số chia hết cho 5
ds_chiahet5 = []

for np in ds_nhiphan:
    # Chuyển từ nhị phân sang thập phân
    so_thap_phan = int(np, 2)
    if so_thap_phan % 5 == 0:
        ds_chiahet5.append(np)

# In kết quả
print("Các số nhị phân chia hết cho 5 là:")
print(",".join(ds_chiahet5))