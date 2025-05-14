import math

# Hàm tính tổ hợp C(n, k)
def to_hop(n, k):
    return math.comb(n, k)  # Yêu cầu Python 3.8+

# Nhập số dòng từ người dùng
n = int(input("Nhập số dòng n: "))

# In n dòng đầu tiên của tam giác Pascal
print(f"{n} dòng đầu tiên của tam giác Pascal:")
for i in range(n):
    dong = [to_hop(i, k) for k in range(i + 1)]
    print(dong)

print("trần nguyễn viết đức")
print("mssv:23575205020710013")
