import math

def khoang_cach(buocdichuyen):
    # Khởi tạo vị trí ban đầu
    x=0 
    y=0

    # Xử lý từng bước di chuyển
    for i in buocdichuyen:  # bắt đầu vòng lặp xử lý từng i trong buocdichuyen
        direction, steps = i.split() # chia chuỗi i thành 2 phần vd :"" up 5" thì up là direction và 5 là steps
        steps = int(steps) 

        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps

    # Tính khoảng cách từ vị trí hiện tại đến (0, 0)
    khoangcach = math.sqrt(x**2 + y**2)

    # Làm tròn khoảng cách và trả về
    return round(khoangcach) 

# Ví dụ di chuyển
buocdichuyen = ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 3"]
result = khoang_cach(buocdichuyen)
print("Khoảng cách từ vị trí hiện tại đến vị trí đầu tiên là:", result)
print("sv:tran nguyen viet duc")
print("235752020710013")