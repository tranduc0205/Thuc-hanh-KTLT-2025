# Nhập danh sách tên từ bàn phím, mỗi tên cách nhau bởi dấu phẩy
danh_sach_ten = input("Nhập danh sách họ và tên (các tên cách nhau bởi dấu phẩy): ").split(',')
# split : tách họ và tên từng người thành các chuỗi nhỏ, nếu người dùng nhập nhiều họ tên

# Duyệt từng tên trong danh sách
for cac_ho_ten in danh_sach_ten:
    cac_ho_ten = cac_ho_ten.strip()  # Xóa khoảng trắng thừa ở đầu và cuối
    ho_ten = cac_ho_ten.split()  # Tách họ và tên riêng dựa trên khoảng trắng

    # Kiểm tra xem có đúng 2 phần không (họ và tên riêng)
    if len(ho_ten) == 2:
        ho, ten_rieng = ho_ten  # Gán phần họ và phần tên riêng
        print(f"Họ: {ho}, Tên riêng: {ten_rieng}")
    else:
        print(f"Lỗi: '{cac_ho_ten}' không hợp lệ. Vui lòng nhập đúng định dạng 'Họ Tên'.")
print("tran nguyen viet duc")
print("mssv:23575205020710013")