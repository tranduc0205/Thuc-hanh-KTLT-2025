s= input(" nhập chuỗi: ")
# ch là một biến tạm thời lưu các giá trị ký tự của chuỗi s qua mỗi lần lặp
for ch in s :
    if ch != ' ' and ch != '\t': 
        # nếu ký tự đó không phải là dấu cách và dấu tab thì lệnh print để in ký tự đó sẽ được thực hiện
           print(ch.upper())
    # in ra từng ký tự mà biến "ch" nhận được qua mỗi vòng lặp, kể cả dấu cách
print("tran nguyen viet duc")
print("mssv:23575205020710013")