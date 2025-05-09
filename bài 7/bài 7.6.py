import os  # Nhập mô-đun os để làm việc với hệ thống tệp, ví dụ như lấy kích thước tệp.

def file_read_from_tail(fname, lines):
    # Hàm này đọc n dòng cuối cùng từ một tệp
    bufsize = 8192  # Kích thước mỗi lần đọc (buffer), 8192 byte (8 KB)
    fsize = os.stat(fname).st_size  # Lấy kích thước của tệp (đơn vị byte)
    iter = 0  # Biến đếm số lần lặp lại (số lần đọc buffer)
    data = []  # Danh sách chứa các dòng đã đọc từ tệp

    with open(fname) as f:  # Mở tệp ở chế độ đọc văn bản
        if bufsize > fsize:  # Nếu tệp nhỏ hơn kích thước buffer, điều chỉnh bufsize cho phù hợp
            bufsize = fsize

        while True:
            iter += 1  # Tăng số lần lặp
            f.seek(fsize - bufsize * iter)  # Dịch con trỏ đọc ngược về cuối tệp (theo từng khối buffer)
            data.extend(f.readlines())  # Đọc tất cả các dòng từ vị trí con trỏ hiện tại đến cuối tệp và thêm vào data

            # Nếu đã đọc đủ số dòng yêu cầu hoặc đã đến đầu tệp, thì dừng lại
            if len(data) >= lines or f.tell() == 0:
                print(''.join(data[-lines:]))  # In ra n dòng cuối cùng từ danh sách data
                break  # Thoát khỏi vòng lặp

# Gọi hàm để đọc 2 dòng cuối cùng từ tệp 'bài 7/test.txt'
file_read_from_tail('bài 7/test.txt', 2)
