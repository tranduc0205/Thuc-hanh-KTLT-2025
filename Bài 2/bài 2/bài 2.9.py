#yêu cầu người dùng nhập vào một chuỗi ký tự từ bàn phím, lưu vào biến str 
str= input ("Enter a String: ")

#khởi tạo một thư viện dictionary rỗng
dict = {}
for n in str :
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1
print(dict)
print("tran nguyen viet duc")
# chương trình đếm số ký tự xuất hiện trong chuỗi