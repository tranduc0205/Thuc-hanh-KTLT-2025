print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")
# Mở tệp a.txt ở chế độ đọc
k = open('C:/lt 2025/bài 7/a.txt', "r")

# Khởi tạo biến đếm
kytu, tu, dong = 0, 0, 0

# Đọc từng dòng trong tệp
for line in k:
    dong += 1  # Tăng số dòng
    kytu += len(line)  # Tăng số ký tự bằng độ dài của dòng
    tu += len(line.split())  # Tăng số từ bằng cách tách dòng thành các từ

# Đóng tệp sau khi đã đọc xong
k.close()

# In ra kết quả
print("Số ký tự là %d\nSố từ là %d\nSố dòng là %d" % (kytu, tu, dong))