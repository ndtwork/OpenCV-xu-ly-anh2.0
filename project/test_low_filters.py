import cv2
import matplotlib.pyplot as plt
from linear_filters_new import mean_filter, gaussian_filter

# Đọc ảnh đầu vào bằng OpenCV (ảnh màu)
image = cv2.imread('FEMME-NOISE.png', cv2.IMREAD_COLOR)

# Chuyển đổi từ BGR sang RGB để hiển thị đúng màu
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Áp dụng lọc
mean_filtered = mean_filter(image_rgb, kernel_size=3)
gaussian_filtered = gaussian_filter(image_rgb, kernel_size=3, sigma=1.5)

# Hiển thị kết quả
plt.figure(figsize=(10, 3))

# Hiển thị ảnh gốc
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image_rgb)  # Hiển thị ảnh RGB

# Hiển thị ảnh lọc trung bình
plt.subplot(1, 3, 2)
plt.title('Mean Filtered')
plt.imshow(mean_filtered)  # Mean filter sẽ trả về ảnh RGB

# Hiển thị ảnh lọc Gauss
plt.subplot(1, 3, 3)
plt.title('Gaussian Filtered')
plt.imshow(gaussian_filtered)  # Gaussian filter cũng trả về ảnh RGB

plt.tight_layout()
plt.show()
