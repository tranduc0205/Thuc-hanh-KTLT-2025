print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")

# Định nghĩa hàm file_read, nhận đối số là tên tệp (fname)
def file_read(fname):
    # Mở tệp với chế độ ghi ('w'), gán đối tượng file vào biến myfile
    # Nếu tệp chưa tồn tại, Python sẽ tạo mới
    # Nếu tệp đã tồn tại, nội dung cũ sẽ bị xóa
    with open(fname, "w") as myfile:
        # Ghi dòng đầu tiên vào tệp, kèm ký tự xuống dòng
        myfile.write("Python Exercises\n")
        # Ghi dòng thứ hai vào tệp (trên cùng dòng nếu không có \n trước)
        myfile.write("Java Exercises")
    
    # Mở lại tệp ở chế độ đọc ('r') để đọc nội dung vừa ghi
    with open(fname, "r") as txt:
        # Đọc toàn bộ nội dung tệp và in ra màn hình
        print(txt.read())

# Gọi hàm với đối số là tên tệp cần làm việc
file_read('abc.txt')
