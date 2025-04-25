print("Trần nguyễn viết đức")
print("MSSV:235752020710013")

import numpy as np

# Tạo mảng có cấu trúc với các tên, lớp học và chiều cao
data = np.array([('James', 5, 48.5), 
                 ('Nail', 6, 52.5), 
                 ('Paul', 5, 42.1), 
                 ('Pit', 5, 40.11)],
                dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')])

# Sắp xếp mảng theo lớp và chiều cao (nếu lớp bằng nhau)
sorted_data = np.sort(data, order=['class', 'height'])

# In mảng sau khi sắp xếp
print(sorted_data)

import numpy as np

# Tạo mảng có cấu trúc với các tên, lớp học và chiều cao
data = np.array([('James', 5, 48.5), 
                 ('Nail', 6, 52.5), 
                 ('Paul', 5, 42.1), 
                 ('Pit', 5, 40.11)],
                dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')])

# Sắp xếp mảng theo lớp và chiều cao (nếu lớp bằng nhau)
sorted_data = np.sort(data, order=['class', 'height'])

# In mảng sau khi sắp xếp
print(sorted_data)

import numpy as np

# Tạo mảng có cấu trúc với các tên, lớp học và chiều cao
data = np.array([('James', 5, 48.5), 
                 ('Nail', 6, 52.5), 
                 ('Paul', 5, 42.1), 
                 ('Pit', 5, 40.11)],
                dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')])

# Sắp xếp mảng theo lớp và chiều cao (nếu lớp bằng nhau)
sorted_data = np.sort(data, order=['class', 'height'])

# In mảng sau khi sắp xếp
print(sorted_data)