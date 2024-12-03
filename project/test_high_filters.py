import cv2
import matplotlib.pyplot as plt
from linear_filters import high_pass_filter

# Đọc ảnh đầu vào (ảnh màu)
image = cv2.imread('car.jpg', cv2.IMREAD_COLOR)

# Áp dụng bộ lọc thông cao
high_pass_filtered = high_pass_filter(image)

# Hiển thị ảnh gốc và ảnh đã lọc
plt.figure(figsize=(10, 5))

# Hiển thị ảnh gốc
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Chuyển từ BGR sang RGB để hiển thị đúng

# Hiển thị ảnh lọc thông cao
plt.subplot(1, 2, 2)
plt.title('High Pass Filtered')
plt.imshow(cv2.cvtColor(high_pass_filtered, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()
