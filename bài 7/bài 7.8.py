print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")
####
danh_sach = ["Học Python cơ bản", "Làm việc với tệp", "chúc bạn may mắn"]
ten_tep = "danh_sach.txt"

try:
    with open(ten_tep, "w", encoding="utf-8") as tep:
        for phan_tu in danh_sach:
            tep.write(phan_tu + "\n")
    print(f"Nội dung đã được ghi vào tệp '{ten_tep}' thành công.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")