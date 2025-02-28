import numpy as np
from scipy.ndimage import convolve

# Ảnh gốc
image = np.array([
    [70, 177, 112, 47],
    [11, 81, 97, 125],
    [24, 243, 195, 114],
    [210, 8, 203, 165]
])

# Bộ lọc trung bình 3x3
kernel = np.ones((3, 3)) / 9

# Padding với 0 xung quanh
padded_image = np.pad(image, pad_width=1, mode='constant', constant_values=0)

# Áp dụng phép lọc trung bình
filtered_image = convolve(padded_image, kernel, mode='constant', cval=0)

# Kết quả sau khi lọc (giữ lại kích thước gốc)
filtered_image_trimmed = filtered_image[1:-1, 1:-1]
filtered_image_trimmed
print(filtered_image_trimmed)