tep_nguon = "danh_sach.txt"
tep_dich = "danh_sach_sao_chep.txt"

try:
    with open(tep_nguon, "r", encoding="utf-8") as tep_doc:
        noi_dung = tep_doc.read()
    with open(tep_dich, "w", encoding="utf-8") as tep_ghi:
        tep_ghi.write(noi_dung)
    print(f"Nội dung đã được sao chép từ '{tep_nguon}' sang '{tep_dich}' thành công.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")