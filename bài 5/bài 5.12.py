print("Trần nguyễn viết đức")
print("MSSV:235752020710013")

import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.])

# Sử dụng lexsort để sắp xếp theo chiều cao (tăng dần)
# Cách sắp xếp: đầu tiên theo chiều cao (student_height), sau đó theo id (student_id)
sorted_indices = np.lexsort((student_height, student_id))

# In chỉ số sắp xếp
print("Chỉ số:")
print(sorted_indices)

# In dữ liệu đã sắp xếp (student_id và student_height theo thứ tự sắp xếp)
print("\nDữ liệu sắp xếp:")
for idx in sorted_indices:
    print(f"{student_id[idx]} \t {student_height[idx]}")
