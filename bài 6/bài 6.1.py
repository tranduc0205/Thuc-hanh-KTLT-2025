print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")
#########################
class HinhTron:  # định nghĩa một lớp tên là hình tròn
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh  # Gán bán kính cho đối tượng

    def tinh_dien_tich(self):
        return self.ban_kinh ** 2 * 3.14  # Diện tích = pi * r^2

# Tạo đối tượng hình tròn với bán kính 2
hinh_tron_A = HinhTron(2)

# In ra diện tích của hình tròn
print("Diện tích hình tròn là:", hinh_tron_A.tinh_dien_tich())