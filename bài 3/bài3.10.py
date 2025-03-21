import math  # Nhập thư viện math để sử dụng giá trị của π

def tinh_hinh_tron():
    try:
        # Mời người dùng nhập bán kính
        r = float(input("Mời bạn nhập bán kính hình tròn (r > 0): "))
        
        # Kiểm tra tính hợp lệ của bán kính
        if r <= 0:
            print("Giá trị bán kính không hợp lệ. Bán kính phải lớn hơn 0.")
            return
        
        # Tính chu vi và diện tích
        chu_vi = 2 * math.pi * r  # Công thức tính chu vi
        dien_tich = math.pi * r**2  # Công thức tính diện tích
        
        # In kết quả ra màn hình
        print(f"Chu vi hình tròn với bán kính {r} là: {chu_vi:.2f}")
        print(f"Diện tích hình tròn với bán kính {r} là: {dien_tich:.2f}")
        
    except ValueError:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số.")

# Gọi hàm để thực hiện
tinh_hinh_tron()
print("sv:tran nguyen viet duc")
print("235752020710013")