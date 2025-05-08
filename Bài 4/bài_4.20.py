import math

# Hàm tính tổ hợp C(n, k)
def to_hop(n, k):
    return math.comb(n, k)  # dùng từ Python 3.8 trở lên

# Nhập n từ người dùng
n = int(input("Nhập số dòng n: "))

# In dòng thứ n của tam giác Pascal
dong = [to_hop(n, k) for k in range(n + 1)]
print("Dòng thứ", n, "của tam giác Pascal là:")
print(dong)