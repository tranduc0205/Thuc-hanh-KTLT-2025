a, b = 1, 2
total = 0

print(a, end=" ")  # In số Fibonacci đầu tiên

while a <= 4000000-1:
    if a % 2 == 0:
        total += a
    print(a, end=" ")  # In số hiện tại trước khi cập nhật
    a, b = b, a + b  # Cập nhật giá trị Fibonacci

print("\nSum of even Fibonacci numbers:", total)  # Chỉnh lại thông báo in
print("sv:tran nguyen viet duc")
print("235752020710013")