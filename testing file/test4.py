import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure

# Ma trận X1 và X2 từ dữ liệu trên
X1 = np.array([
    [52, 55, 61, 66, 70, 61, 64, 73],
    [63, 59, 55, 90, 109, 85, 69, 72],
    [62, 59, 68, 113, 144, 104, 66, 73],
    [63, 58, 71, 122, 154, 106, 70, 69],
    [67, 61, 68, 104, 126, 88, 68, 70],
    [79, 65, 60, 70, 77, 68, 58, 75],
    [85, 71, 64, 59, 55, 61, 65, 83],
    [87, 79, 69, 68, 65, 76, 78, 94]
])

X2 = np.array([
    [19, 17, 2, 1, 1, 2, 2, 1],
    [18, 19, 19, 17, 1, 1, 1, 1],
    [17, 18, 19, 17, 1, 2, 1, 1],
    [18, 19, 19, 19, 19, 1, 1, 2],
    [18, 19, 19, 18, 17, 2, 3, 3],
    [19, 19, 19, 18, 18, 2, 2, 1],
    [19, 19, 18, 18, 17, 1, 2, 1],
    [18, 19, 18, 17, 3, 1, 1, 3]
])

# Vẽ histogram của X1 và X2
plt.figure(figsize=(12, 6))

# Histogram cho X1
plt.subplot(1, 2, 1)
plt.hist(X1.ravel(), bins=256, range=(0, 255), color='gray')
plt.title('Histogram của X1')
plt.xlabel('Mức xám')
plt.ylabel('Số lượng pixel')

# Histogram cho X2
plt.subplot(1, 2, 2)
plt.hist(X2.ravel(), bins=256, range=(0, 255), color='gray')
plt.title('Histogram của X2')
plt.xlabel('Mức xám')
plt.ylabel('Số lượng pixel')

plt.tight_layout()
plt.show()

# Cân bằng histogram cho X2
X2_equalized = exposure.equalize_hist(X2)

# Vẽ histogram sau khi cân bằng
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(X2, cmap='gray')
plt.title('Ảnh X2 gốc')

plt.subplot(1, 2, 2)
plt.imshow(X2_equalized, cmap='gray')
plt.title('Ảnh X2 sau khi cân bằng Histogram')

plt.tight_layout()
plt.show()

# Histogram sau khi cân bằng
plt.figure(figsize=(6, 6))
plt.hist(X2_equalized.ravel(), bins=256, range=(0, 1), color='gray')
plt.title('Histogram sau khi cân bằng của X2')
plt.xlabel('Mức xám (Sau khi cân bằng)')
plt.ylabel('Số lượng pixel')
plt.show()


from scipy.ndimage import convolve

# Mask lọc trung bình
average_filter = np.ones((3, 3)) / 9

# Lọc trung bình
X2_average_filtered = convolve(X2, average_filter)

plt.imshow(X2_average_filtered, cmap='gray')
plt.title('Lọc trung bình trên X2')
plt.show()

