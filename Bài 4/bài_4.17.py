
import math

def tong_uoc_so_khong_ke_chinh_no(so):
    tong = 1  # 1 luôn là ước số của mọi số nguyên dương (trừ 1)
    can = int(math.sqrt(so))
    for i in range(2, can + 1):
        if so % i == 0:
            tong += i
            uoc_kem = so // i
            if uoc_kem != i:  # tránh cộng trùng nếu i là căn bậc hai
                tong += uoc_kem
    return tong

def la_so_du_thua(so):
    return tong_uoc_so_khong_ke_chinh_no(so) > so

# Nhập n từ người dùng
n = int(input("Nhập số nguyên dương n: "))

print(f"Tổng các ước lớn hơn chính số đó {n} là:")
for so in range(2, n):  # bắt đầu từ 2 vì 1 không có ước số nhỏ hơn nó
    if la_so_du_thua(so):
        print(so, end=' ')
