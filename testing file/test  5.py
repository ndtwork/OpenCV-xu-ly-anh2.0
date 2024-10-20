import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure

# Ma trận X1 và X2 từ dữ liệu trên
X2 = np.array([
    [52, 55, 61, 66, 70, 61, 64, 73],
    [63, 59, 55, 90, 109, 85, 69, 72],
    [62, 59, 68, 113, 144, 104, 66, 73],
    [63, 58, 71, 122, 154, 106, 70, 69],
    [67, 61, 68, 104, 126, 88, 68, 70],
    [79, 65, 60, 70, 77, 68, 58, 75],
    [85, 71, 64, 59, 55, 61, 65, 83],
    [87, 79, 69, 68, 65, 76, 78, 94]
])

X1 = np.array([
    [19, 17, 2, 1, 1, 2, 2, 1],
    [18, 19, 19, 17, 1, 1, 1, 1],
    [17, 18, 19, 17, 1, 2, 1, 1],
    [18, 19, 19, 19, 19, 1, 1, 2],
    [18, 19, 19, 18, 17, 2, 3, 3],
    [19, 19, 19, 18, 18, 2, 2, 1],
    [19, 19, 18, 18, 17, 1, 2, 1],
    [18, 19, 18, 17, 3, 1, 1, 3]
])
#Loc thong thap

from scipy.ndimage import convolve

# Mask lọc trung bình
average_filter = np.ones((3, 3)) / 9

# Lọc trung bình
X2_average_filtered = convolve(X2, average_filter)

plt.subplot(1, 3, 1)
plt.imshow(X2, cmap='gray')
plt.title('Ảnh X2 gốc')

plt.subplot(1, 3, 2)
plt.imshow(X2_average_filtered, cmap='gray')
plt.title('Lọc trung bình trên X2')


from scipy.ndimage import gaussian_filter

# Lọc Gaussian
X2_gaussian_filtered = gaussian_filter(X2, sigma=1)
plt.subplot(1, 3, 3)
plt.imshow(X2_gaussian_filtered, cmap='gray')
plt.title('Lọc Gaussian trên X2')
plt.show()


# Mask lọc làm sắc nét (Sharpening filter)
sharpening_filter = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Lọc làm sắc nét
X2_sharpened = convolve(X2, sharpening_filter)

plt.imshow(X2_sharpened, cmap='gray')
plt.title('Lọc làm sắc nét trên X2')
plt.show()


plt.subplot(1, 3, 1)
plt.hist(X2.ravel(), bins=256, range=(0, 255), color='gray')
plt.title('Histogram của X2')
plt.xlabel('Mức xám')
plt.ylabel('Số lượng pixel')

plt.subplot(1, 3, 2)
plt.hist(X2_average_filtered.ravel(), bins=256, range=(0, 255), color='gray')
plt.title('Histogram của loc trung vi')
plt.xlabel('Mức xám')
plt.ylabel('Số lượng pixel')

plt.subplot(1, 3, 3)
plt.hist(X2_gaussian_filtered.ravel(), bins=256, range=(0, 255), color='gray')
plt.title('Histogram của X2 loc Gaussian')
plt.xlabel('Mức xám')
plt.ylabel('Số lượng pixel')

plt.tight_layout()
plt.show()