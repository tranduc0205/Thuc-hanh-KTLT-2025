import os

# Kiểm tra thư mục hiện tại
print("Thư mục hiện tại:", os.getcwd())

# Đường dẫn đến file a.txt
file_path = os.path.join("C:/lt 2025/bài 7", "a.txt")

def file_read_from_head(fname, nlines): 
    try:
        # Mở file để đọc
        with open(fname, "r") as f:  
            for i in range(nlines):
                # Đọc từng dòng và loại bỏ ký tự xuống dòng
                line = f.readline().strip()  
                if line:  # Kiểm tra nếu dòng không rỗng
                    print(line)  # In ra dòng đã đọc
    except FileNotFoundError:
        print(f"File không tìm thấy: {fname}")  # Thông báo nếu file không tồn tại
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")  # Thông báo nếu có lỗi khác

# Gọi hàm với đường dẫn đúng
file_read_from_head(file_path, 2)  # Đọc 2 dòng đầu tiên từ file

print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")
####
