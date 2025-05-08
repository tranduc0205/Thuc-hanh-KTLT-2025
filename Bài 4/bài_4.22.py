# Tạo danh sách chứa các số thỏa mãn điều kiện
danh_sach_so = []

# Duyệt qua từng số trong khoảng từ 1000 đến 3000 (bao gồm 3000)
for so in range(1000, 3001):
    # Chuyển số thành chuỗi để duyệt từng chữ số
    chu_so = str(so)
    # Kiểm tra xem tất cả các chữ số đều là số chẵn
    if all(int(ch) % 2 == 0 for ch in chu_so):
        danh_sach_so.append(chu_so)

# In kết quả trên một dòng, các số cách nhau bằng dấu phẩy
print(",".join(danh_sach_so))