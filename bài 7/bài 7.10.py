print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")
######
ten_tep = "abc.txt"

try:
    with open(ten_tep, "rb") as tep:
        van_ban = tep.read().decode("utf-8", errors="replace")  # Sử dụng "replace" để bỏ qua các lỗi decode
    cac_tu = van_ban.split()
    tu_dai_nhat = max(cac_tu, key=len)
    cac_tu_dai_nhat = [tu for tu in cac_tu if len(tu) == len(tu_dai_nhat)]
    print(f"Những từ dài nhất trong tệp '{ten_tep}': {cac_tu_dai_nhat}")
except FileNotFoundError:
    print(f"Tệp '{ten_tep}' không tồn tại.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")