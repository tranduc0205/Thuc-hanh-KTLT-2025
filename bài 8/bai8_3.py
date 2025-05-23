import turtle 

# Danh sách các màu
colors = ["red", "green", "blue"]


painter = turtle.Turtle()
painter.pensize(3)  # Đặt độ dày bút vẽ

# Vẽ 12 vòng tròn với các màu khác nhau
for i in range(12):
    color = colors[i % len(colors)]  # Chọn màu theo chỉ số vòng lặp
    painter.pencolor(color)  # Đặt màu viền cho turtle
    painter.circle(100)  # Vẽ vòng tròn có bán kính 100
# Quay 30 độ sang bên phải
    painter.left(30)   # Quay 60 độ sang bên trái
    painter.setposition(0, 0)  # Đặt vị trí turtle về điểm gốc (0, 0)

painter.hideturtle()  # Ẩn con trỏ turtle
turtle.done()  # Giữ cửa sổ mở
print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")
