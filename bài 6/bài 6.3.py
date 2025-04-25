# Định nghĩa lớp cha
class Nguoi:
    def getGender(self):
        return "Không xác định"

# Định nghĩa lớp con Nam, kế thừa từ Nguoi
class Nam(Nguoi):
    def getGender(self):
        return "Nam"

# Định nghĩa lớp con Nu, kế thừa từ Nguoi
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng và in giới tính
nguoi1 = Nam()
nguoi2 = Nu()


print("Giới tính người 1:", nguoi1.getGender())  # Kết quả: Nam
print("Giới tính người 2:", nguoi2.getGender())  # Kết quả: Nữ