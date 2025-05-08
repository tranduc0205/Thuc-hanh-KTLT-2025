# Nhập câu từ bàn phím
cau = input("Nhập một câu: ")

# Khởi tạo biến đếm
so_chu_cai = 0
so_chu_so = 0

# Duyệt từng ký tự trong câu
for ky_tu in cau:
    if ky_tu.isalpha():  # Nếu là chữ cái
        so_chu_cai += 1
    elif ky_tu.isdigit():  # Nếu là chữ số
        so_chu_so += 1

# In kết quả
print(f"Số chữ cái là {so_chu_cai}, số chữ số là {so_chu_so}")