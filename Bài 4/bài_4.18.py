# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Tạo danh sách các số Fibonacci nhỏ hơn n
danh_sach_fibo = []
a, b = 0, 1
while a < n:
    danh_sach_fibo.append(a)
    a, b = b, a + b

# In danh sách ra màn hình
print(f"Các số Fibonacci nhỏ hơn {n} là:")
print(danh_sach_fibo)