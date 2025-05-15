print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")
print("sv: trần nguyễn viết đức.")
print("mssv: 235752020710013")

def dem_so_dong_trong_tep(tentep):
    try:
        # Mở tệp để đọc (chế độ 'r'), sử dụng mã hóa 'utf-8'
        with open(tentep, 'r', encoding='utf-8') as tep:
            # Đếm số dòng trong tệp bằng cách cộng 1 cho mỗi dòng
            so_dong = sum(1 for dong in tep)
        return so_dong
    except FileNotFoundError:
        # Nếu tệp không tìm thấy, in thông báo lỗi
        print(f"Tệp '{tentep}' không tìm thấy.")
        return None
    except UnicodeDecodeError:
        # Nếu có lỗi mã hóa khi đọc tệp, in thông báo lỗi
        print(f"Lỗi mã hóa, không thể đọc tệp '{tentep}'.")
        return None

# Đường dẫn đến tệp test.txt
ten_tep = 'C:/lt 2025/bài 7/test.txt'  # Sử dụng đường dẫn tuyệt đối

# Gọi hàm và hiển thị kết quả
so_dong = dem_so_dong_trong_tep(ten_tep)

if so_dong is not None:
    print(f"Số dòng trong tệp '{ten_tep}': {so_dong}")
