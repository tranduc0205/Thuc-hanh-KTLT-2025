# Khởi tạo danh sách để lưu các số thỏa mãn điều kiện
result = []

# Duyệt qua khoảng từ 2000 đến 3200
for i in range(2000, 3201):
    # Kiểm tra xem số có chia hết cho 7 và không phải bội số của 5 không
    if i % 7 == 0 and i % 5 !== 0 :
        result.append(str(i))  # Chuyển số thành chuỗi trước khi thêm vào danh sách

# In ra các số thỏa mãn điều kiện, cách nhau bằng dấu phẩy
print(", ".join(result))
