print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")

import os

# Kiểm tra thư mục hiện tại
print("Current Directory:", os.getcwd())

def file_read_from_head(fname, nlines): 
    from itertools import islice  
    with open(fname) as f:  
        for line in islice(f, nlines):  
            print(line) 

# Gọi hàm với đường dẫn đúng
file_read_from_head("bài 7/a.txt", 2)