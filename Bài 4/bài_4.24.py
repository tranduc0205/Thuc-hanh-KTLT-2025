# Nhập câu từ bàn phím
cau = input("Nhập một câu: ")

# Khởi tạo biến đếm
chu_hoa = 0
chu_thuong = 0

# Duyệt từng ký tự trong câu
for ky_tu in cau:
    if ky_tu.isupper():  # Nếu là chữ in hoa
        chu_hoa += 1
    elif ky_tu.islower():  # Nếu là chữ thường
        chu_thuong += 1

# In kết quả
print(f"Chữ hoa: {chu_hoa}")
print(f"Chữ thường: {chu_thuong}")
 