import math

class Circle:
    def __init__(self, ban_kinh):
        """Khởi tạo hình tròn với bán kính."""
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        """Tính diện tích của hình tròn."""
        return math.pi * (self.ban_kinh ** 2)

    def tinh_chu_vi(self):
        """Tính chu vi của hình tròn."""
        return 2 * math.pi * self.ban_kinh

# Ví dụ sử dụng
ban_kinh = float(input("Nhập bán kính của hình tròn: "))
hinh_tron = Circle(ban_kinh)

print(f"Diện tích của hình tròn: {hinh_tron.tinh_dien_tich()}")
print(f"Chu vi của hình tròn: {hinh_tron.tinh_chu_vi()}")
print("trần nguyễn viết đức")
print("mssv:23575205020710013")
