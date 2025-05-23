import turtle  # Nhập mô-đun turtle
import random  # Nhập mô-đun random để chọn màu ngẫu nhiên

# Danh sách các màu
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Tạo đối tượng turtle để vẽ
painter = turtle.Turtle()
painter.pensize(3)  # Đặt độ dày bút vẽ

# Vẽ 10 vòng tròn với màu sắc ngẫu nhiên
for i in range(10):
    color = random.choice(colors)  # Chọn màu ngẫu nhiên từ danh sách
    painter.pencolor(color)  # Đặt màu viền cho turtle
    painter.circle(100)  # Vẽ vòng tròn có bán kính 100
    painter.right(30)  # Quay 30 độ sang bên phải
    painter.left(60)   # Quay 60 độ sang bên trái
    painter.setposition(0, 0)  # Đặt vị trí turtle về điểm gốc (0, 0)

# Hoàn tất vẽ
turtle.done()  # Giữ cửa sổ mở
print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")