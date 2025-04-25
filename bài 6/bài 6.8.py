print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")
class NganHang:
    loai_tai_khoan = "Tiết kiệm"
    chi_nhanh = "Gurgaon"

    def __init__(self, ten, so_tai_khoan, so_du):
        self.ten = ten
        self.so_tai_khoan = so_tai_khoan
        self.so_du = so_du
        self.loai_tai_khoan = NganHang.loai_tai_khoan
        self.chi_nhanh = NganHang.chi_nhanh

    def __repr__(self):
        print("Chào mừng đến với máy ATM của SBI")
        ma_pin = input("Vui lòng nhập mã PIN của bạn: ")
        if ma_pin != "1234":
            print("❌ Sai mã PIN. Vui lòng thử lại!")
            return self.__repr__()  # gọi lại chính nó
        else:
            self.truy_cap_tai_khoan()

    def truy_cap_tai_khoan(self):
        ma_pin = input("Vui lòng nhập lại mã PIN để xác nhận: ")
        if ma_pin == "1234":
            print(f"🔒 Số thẻ của bạn: XXXX XXXX XXXX 1237")
            print("Bạn muốn thực hiện giao dịch gì?")
            print("""
            1) Xem số dư
            2) Rút tiền
            3) Gửi tiền
            4) Thoát
            """)
            self.giao_dich()
        else:
            print("❌ Sai mã PIN. Vui lòng thử lại!")
            self.truy_cap_tai_khoan()

    def xem_so_du(self):
        print("💰 Số dư hiện tại:", self.so_du, "VND")

    def rut_tien(self):
        so_tien = int(input("Nhập số tiền bạn muốn rút: "))
        if so_tien <= self.so_du:
            self.so_du -= so_tien
            print("✅ Giao dịch thành công.")
            print("💰 Số dư còn lại:", self.so_du, "VND")
        else:
            print("❌ Giao dịch bị hủy do không đủ tiền trong tài khoản.")

    def gui_tien(self):
        so_tien = int(input("Nhập số tiền bạn muốn gửi: "))
        self.so_du += so_tien
        print("✅ Giao dịch thành công.")
        print("💰 Số dư mới:", self.so_du, "VND")

    def giao_dich(self):
        while True:
            lua_chon = input("👉 Nhập lựa chọn của bạn (1-4): ")
            if lua_chon == "1":
                self.xem_so_du()
            elif lua_chon == "2":
                self.rut_tien()
            elif lua_chon == "3":
                self.gui_tien()
            elif lua_chon == "4":
                print("📤 Cảm ơn bạn đã sử dụng máy ATM SBI. Hẹn gặp lại!")
                break
            else:
                print("⚠️ Lựa chọn không hợp lệ. Vui lòng thử lại.")

    # Tạo tài khoản và bắt đầu sử dụng
tai_khoan = NganHang("Nguyen Van A", 123456789, 1000000)
print(tai_khoan)