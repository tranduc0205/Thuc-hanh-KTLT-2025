so_du = 0

while True:
    dong = input("Nhập giao dịch (D/W số), hoặc nhấn Enter để kết thúc: ")
    if not dong:
        break

    kieu, so = dong.split()
    so = int(so)

    if kieu == 'D':
        so_du += so
    elif kieu == 'W':
        so_du -= so

print("Số dư tài khoản là:", so_du)
