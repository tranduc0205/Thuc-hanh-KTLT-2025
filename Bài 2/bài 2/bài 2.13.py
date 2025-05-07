import math

# Hàm giải phương trình bậc 2
def giai_phuong_trinh_bac_2(a, b, c):
    if a == 0:
        if b == 0:
            return "Phương trình vô nghiệm" if c != 0 else "Phương trình có vô số nghiệm"
        else:
            return f"Nghiệm: {-c / b}"
    
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Có 1 nghiệm kép: x = {x}"
    else:
        return "Phương trình vô nghiệm"

# Nhập hệ số từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Gọi hàm và in kết quả
ket_qua = giai_phuong_trinh_bac_2(a, b, c)
print(ket_qua)
print("sv:tran nguyen viet duc")
print("235752020710013")
    