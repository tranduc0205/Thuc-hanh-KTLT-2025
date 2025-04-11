def sang_nguyen_to(gioi_han):
    # Tạo một danh sách đánh dấu các số là nguyên tố (True)
    sang = [True] * gioi_han
    sang[0:2] = [False, False]  # 0 và 1 không phải là số nguyên tố

    for i in range(2, int(gioi_han ** 0.5) + 1):
        if sang[i]:
            # Đánh dấu các bội số của i là không phải nguyên tố
            for j in range(i * i, gioi_han, i):
                sang[j] = False

    # Trả về tuple các số nguyên tố
    return tuple(i for i, la_nt in enumerate(sang) if la_nt)

# Tạo tuple các số nguyên tố nhỏ hơn 1 triệu
P = sang_nguyen_to(1_000_000)

print(f"Có {len(P)} số nguyên tố nhỏ hơn 1 triệu.")