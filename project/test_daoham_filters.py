import cv2
import matplotlib.pyplot as plt
from linear_filters_new import sobel_filter, laplace_filter

# Đọc ảnh đầu vào (ảnh màu BGR)
image = cv2.imread('FEMME-NOISE.png', cv2.IMREAD_COLOR)

# Áp dụng Sobel filter theo X, Y và kết hợp
sobel_x = sobel_filter(image, axis=0)
sobel_y = sobel_filter(image, axis=1)
sobel_combined = sobel_filter(image, axis=2)

# Áp dụng Laplace filter
laplace_filtered = laplace_filter(image)

# Hiển thị kết quả
plt.figure(figsize=(10, 15))

# Hiển thị ảnh gốc (chuyển sang RGB)
plt.subplot(3, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Chuyển BGR sang RGB

# Hiển thị Sobel theo X
plt.subplot(3, 2, 2)
plt.title('Sobel X')
plt.imshow(sobel_x, cmap='gray')  # Ảnh Sobel là grayscale

# Hiển thị Sobel theo Y
plt.subplot(3, 2, 3)
plt.title('Sobel Y')
plt.imshow(sobel_y, cmap='gray')  # Ảnh Sobel là grayscale

# Hiển thị Sobel kết hợp
plt.subplot(3, 2, 4)
plt.title('Sobel Combined')
plt.imshow(sobel_combined, cmap='gray')  # Ảnh Sobel là grayscale

# Hiển thị Laplace
plt.subplot(3, 2, 5)
plt.title('Laplace Filtered')
plt.imshow(laplace_filtered, cmap='gray')  # Ảnh Laplacian là grayscale

plt.tight_layout()
plt.show()
