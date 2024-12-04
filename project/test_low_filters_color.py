import cv2
import matplotlib.pyplot as plt
from linear_filters import mean_filter, gaussian_filter

# Đọc ảnh màu
image = cv2.imread('project\car.jpg', cv2.IMREAD_COLOR)

# Tách các kênh màu BGR
b, g, r = cv2.split(image)

# Áp dụng lọc cho từng kênh , để có thể áp dụng bộ lọc cho ảnh màu cần tách nó thành 3 kênh BGR sau đó ghép, tái tạo lại ảnh
b_filtered = mean_filter(b, kernel_size=3)
g_filtered = mean_filter(g, kernel_size=3)
r_filtered = mean_filter(r, kernel_size=3)

# Ghép lại các kênh sau khi lọc
mean_filtered = cv2.merge([b_filtered, g_filtered, r_filtered])

# Tương tự cho bộ lọc Gauss
b_filtered_gaussian = gaussian_filter(b, kernel_size=3, sigma=1.5)
g_filtered_gaussian = gaussian_filter(g, kernel_size=3, sigma=1.5)
r_filtered_gaussian = gaussian_filter(r, kernel_size=3, sigma=1.5)

# Ghép lại các kênh sau khi lọc Gaussian
gaussian_filtered = cv2.merge([b_filtered_gaussian, g_filtered_gaussian, r_filtered_gaussian])

# Hiển thị kết quả
plt.figure(figsize=(10, 5))

# Hiển thị ảnh gốc
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Đổi từ BGR sang RGB để hiển thị đúng

# Hiển thị ảnh lọc trung bình
plt.subplot(1, 3, 2)
plt.title('Mean Filtered')
plt.imshow(cv2.cvtColor(mean_filtered, cv2.COLOR_BGR2RGB))

# Hiển thị ảnh lọc Gauss
plt.subplot(1, 3, 3)
plt.title('Gaussian Filtered')
plt.imshow(cv2.cvtColor(gaussian_filtered, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()
