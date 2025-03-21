def benefit(t, n, k):
    # Chuyển đổi lãi suất từ phần trăm sang số thập phân
    lai_suat = t/100
    
    # Tính số tiền nhận được sau k tháng
    so_tien_nhan_duoc = n*lai_suat*k + n
    
    return so_tien_nhan_duoc

def main():
    try:
        # Nhập lãi suất, số vốn và số tháng
        # kiểu float: kiểu số thực
        t = float(input("Nhập lãi suất tiết kiệm (%/tháng, vd 0.5): "))
        
        n = float(input("Nhập số vốn ban đầu (vnđ): "))
        k = int(input("Nhập số tháng gửi : "))
    
        # Tính số tiền nhận được
        so_tien = benefit(t, n, k)
        
        # In kết quả
        print(f"Số tiền nhận được sau {k} tháng là: {so_tien:.2f} VND")
        
    except ValueError:
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập số.")

# Gọi hàm main để thực hiện
main()
print("sv:tran nguyen viet duc")
print("235752020710013")