# Nhập dãy các từ từ bàn phím
danh_sach_tu = input("Nhập dãy các từ: ").split()

# Tìm độ dài của từ dài nhất
max_length = max(len(tu) for tu in danh_sach_tu)

# Lọc ra tất cả các từ có độ dài bằng với độ dài từ dài nhất
tu_dai_nhat = [tu for tu in danh_sach_tu if len(tu) == max_length]

# In ra các từ dài nhất
print("Các từ dài nhất là:", ", ".join(tu_dai_nhat))