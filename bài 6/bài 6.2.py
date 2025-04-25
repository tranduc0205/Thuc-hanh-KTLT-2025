print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")

class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

# Tạo một hình chữ nhật có chiều dài 5 và chiều rộng 3
hcn = HinhChuNhat(5, 3)

# In ra diện tích của hình chữ nhật
print("Diện tích hình chữ nhật là:", hcn.tinh_dien_tich())