import turtle  # import hàm turtle sử dụng để vẽ hình ảnh và tạo đồ họa.
               ### turtle: con rùa, con trỏ
# Tạo cửa sổ vẽ
window = turtle.Screen()
window.bgcolor("lightgreen")  # Màu nền của cửa sổ

# Tạo đối tượng turtle để vẽ
painter = turtle.Turtle()       #Tạo một đối tượng "turtle" mới, gọi là painter, để vẽ.
painter.fillcolor('yellow')  # Màu nền của hình vuông
painter.pencolor('blue')  # Màu viền của hình vuông
painter.pensize(3)  # Độ dày của bút vẽ

def draws(t, s):   # định nghĩa một hàm có tên là drawsq với hai tham số t là turle và s là chiều dài cạnh 
    """Hàm vẽ hình vuông."""
    for i in range(4):
        t.forward(s)  # 
        t.left(90)    # Quay sang trái 90 độ

# Vẽ hình vuông nhiều lần với góc xoay
for i in range(1, 180):
    painter.left(18)  # Quay turtle 18 độ trước khi vẽ hình vuông
    draws(painter, 200)  # Vẽ hình vuông với cạnh dài 200

# Hoàn tất vẽ
window.mainloop()  # Giữ cửa sổ mở
print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")
