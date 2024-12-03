import cv2
import matplotlib.pyplot as plt
from linear_filters import sobel_filter, laplace_filter

# Đọc ảnh đầu vào (ảnh xám)
image = cv2.imread('bagues.jpg', cv2.IMREAD_GRAYSCALE)

# Áp dụng Sobel filter theo X, Y và kết hợp
sobel_x = sobel_filter(image, axis=0)
sobel_y = sobel_filter(image, axis=1)
sobel_combined = sobel_filter(image, axis=2)

# Áp dụng Laplace filter
laplace_filtered = laplace_filter(image)

# Hiển thị kết quả
plt.figure(figsize=(10, 10))

# Hiển thị ảnh gốc
plt.subplot(3, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

# Hiển thị Sobel theo X
plt.subplot(3, 2, 2)
plt.title('Sobel X')
plt.imshow(sobel_x, cmap='gray')

# Hiển thị Sobel theo Y
plt.subplot(3, 2, 3)
plt.title('Sobel Y')
plt.imshow(sobel_y, cmap='gray')

# Hiển thị Sobel kết hợp

plt.subplot(3, 2, 4)
plt.title('Sobel Combined')
plt.imshow(sobel_combined, cmap='gray')

# Hiển thị Laplace
plt.subplot(3, 2, 5)
plt.title('Laplace Filtered')
plt.imshow(laplace_filtered, cmap='gray')

plt.tight_layout()
plt.show()
