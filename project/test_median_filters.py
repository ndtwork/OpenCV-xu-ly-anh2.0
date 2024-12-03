import cv2
import numpy as np
import matplotlib.pyplot as plt
from nonlinear_filters import median_filter

# Đọc ảnh
image = cv2.imread('FEMME-NOISE.png', cv2.IMREAD_GRAYSCALE)

# Áp dụng lọc trung vị với kernel size 5
filtered_image = median_filter(image, kernel_size=5)

# Tính toán histogram cho ảnh gốc và ảnh đã lọc
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_filtered = cv2.calcHist([filtered_image], [0], None, [256], [0, 256])

# Hiển thị ảnh và histogram
plt.figure(figsize=(14, 8))

# Hiển thị ảnh gốc
plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

# Hiển thị histogram của ảnh gốc (dùng plt.plot)
plt.subplot(2, 3, 2)
plt.title('Histogram (Plot) - Original Image')
plt.plot(hist_original, color='blue')
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Hiển thị histogram của ảnh gốc (dùng plt.hist)
plt.subplot(2, 3, 3)
plt.title('Histogram (Hist) - Original Image')
plt.hist(image.ravel(), bins=256, range=(0, 256), color='blue', alpha=0.7)
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Hiển thị ảnh đã lọc
plt.subplot(2, 3, 4)
plt.title('Median Filtered Image')
plt.imshow(filtered_image, cmap='gray')
plt.axis('off')

# Hiển thị histogram của ảnh đã lọc (dùng plt.plot)
plt.subplot(2, 3, 5)
plt.title('Histogram (Plot) - Filtered Image')
plt.plot(hist_filtered, color='green')
plt.xlim([0, 256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Hiển thị histogram của ảnh đã lọc (dùng plt.hist)
plt.subplot(2, 3, 6)
plt.title('Histogram (Hist) - Filtered Image')
plt.hist(filtered_image.ravel(), bins=256, range=(0, 256), color='green', alpha=0.7)
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
